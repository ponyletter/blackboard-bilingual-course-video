#!/usr/bin/env python3
"""Validate a completed nine-scene blackboard-course project directory."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def probe(video: Path) -> dict:
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries',
         'format=duration:stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels',
         '-of', 'json', str(video)],
        check=True, text=True, capture_output=True,
    )
    return json.loads(result.stdout)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    args = parser.parse_args()
    root = args.project.resolve()
    failures: list[str] = []

    images = sorted((root / 'scenes').glob('[0-9][0-9]_*.png'))
    audios = sorted((root / 'audio').glob('scene[0-9][0-9].wav'))
    if len(images) != 9:
        failures.append(f'Expected 9 scene PNGs, found {len(images)}.')
    if len(audios) != 9:
        failures.append(f'Expected 9 delivery WAV files, found {len(audios)}.')
    for filename in ['contact-sheet.png', 'asset_manifest.json']:
        if not (root / filename).is_file():
            failures.append(f'Missing {filename}.')
    if not list(root.glob('*.srt')) or not list(root.glob('*.vtt')):
        failures.append('Missing SRT or VTT captions.')
    if not list((root / 'cover').glob('*.png')):
        failures.append('Missing a PNG cover under cover/.')

    videos = list((root / 'renders').glob('*.mp4'))
    if len(videos) != 1:
        failures.append(f'Expected one MP4 under renders/, found {len(videos)}.')
    else:
        info = probe(videos[0])
        streams = info['streams']
        video_stream = next((s for s in streams if s['codec_type'] == 'video'), {})
        audio_stream = next((s for s in streams if s['codec_type'] == 'audio'), {})
        if (video_stream.get('codec_name'), video_stream.get('width'), video_stream.get('height'), video_stream.get('r_frame_rate')) != ('h264', 1920, 1080, '30/1'):
            failures.append(f'Unexpected video spec: {video_stream}.')
        if audio_stream.get('codec_name') != 'aac':
            failures.append(f'Expected AAC audio, found {audio_stream.get("codec_name")}.')

    manifest_path = root / 'asset_manifest.json'
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        if len(manifest.get('scenes', [])) != 9:
            failures.append('Manifest does not map exactly 9 scenes.')
        for scene in manifest.get('scenes', []):
            for key in ('audio', 'image'):
                if not (root / scene.get(key, '')).is_file():
                    failures.append(f"Manifest scene {scene.get('scene')} has missing {key}: {scene.get(key)}")

    if failures:
        print('FAIL')
        print('\n'.join(f'- {item}' for item in failures))
        raise SystemExit(1)
    print('PASS — completed blackboard-course project satisfies core delivery checks.')


if __name__ == '__main__':
    main()
