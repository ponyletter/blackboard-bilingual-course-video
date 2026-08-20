#!/usr/bin/env python3
"""Validate a completed sentence-synchronous nine-scene blackboard-course project."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def ffprobe_json(path: Path) -> dict:
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=codec_type,codec_name,width,height,r_frame_rate', '-of', 'json', str(path)],
        check=True, text=True, capture_output=True,
    )
    return json.loads(result.stdout)


def duration(path: Path) -> float:
    return float(ffprobe_json(path)['format']['duration'])


def nonblank_event_count(path: Path, kind: str) -> int:
    text = path.read_text(encoding='utf-8-sig')
    if kind == 'srt':
        return sum(1 for line in text.splitlines() if '-->' in line)
    if kind == 'vtt':
        return sum(1 for line in text.splitlines() if '-->' in line)
    if kind == 'ass':
        return sum(1 for line in text.splitlines() if line.startswith('Dialogue:'))
    raise ValueError(kind)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    args = parser.parse_args()
    root = args.project.resolve()
    failures: list[str] = []

    images = sorted((root / 'scenes').glob('[0-9][0-9]_*.png'))
    scene_audios = sorted((root / 'audio').glob('scene[0-9][0-9].wav'))
    if len(images) != 9:
        failures.append(f'Expected 9 scene PNGs, found {len(images)}.')
    if len(scene_audios) != 9:
        failures.append(f'Expected 9 delivery scene WAV files, found {len(scene_audios)}.')
    for filename in ['contact-sheet.png', 'asset_manifest.json', 'sentence_timeline.json', 'voice_profile.json']:
        if not (root / filename).is_file():
            failures.append(f'Missing {filename}.')
    if not list(root.glob('*.srt')) or not list(root.glob('*.vtt')) or not list(root.glob('*.ass')):
        failures.append('Missing SRT, VTT, or ASS captions.')
    if not list((root / 'cover').glob('*.png')):
        failures.append('Missing a PNG cover under cover/.')

    videos = list((root / 'renders').glob('*.mp4'))
    if len(videos) != 1:
        failures.append(f'Expected one MP4 under renders/, found {len(videos)}.')
    else:
        info = ffprobe_json(videos[0])
        streams = info['streams']
        video_stream = next((s for s in streams if s['codec_type'] == 'video'), {})
        audio_stream = next((s for s in streams if s['codec_type'] == 'audio'), {})
        if (video_stream.get('codec_name'), video_stream.get('width'), video_stream.get('height'), video_stream.get('r_frame_rate')) != ('h264', 1920, 1080, '30/1'):
            failures.append(f'Unexpected video spec: {video_stream}.')
        if audio_stream.get('codec_name') != 'aac':
            failures.append(f'Expected AAC audio, found {audio_stream.get("codec_name")}.')

    timeline_path = root / 'sentence_timeline.json'
    manifest_path = root / 'asset_manifest.json'
    profile_path = root / 'voice_profile.json'
    sentence_count = 0
    if profile_path.is_file():
        profile = json.loads(profile_path.read_text(encoding='utf-8'))
        if profile.get('gender', '').lower() != 'male':
            failures.append('voice_profile.json must explicitly set gender to male.')
        for key in ['profile_id', 'provider', 'provider_model', 'voice_id', 'voice_name', 'language_code', 'reference_audio_sha256']:
            if not profile.get(key):
                failures.append(f'voice_profile.json missing {key}.')
    if timeline_path.is_file():
        timeline = json.loads(timeline_path.read_text(encoding='utf-8'))
        sentences = timeline.get('sentences', [])
        sentence_count = len(sentences)
        if sentence_count == 0:
            failures.append('sentence_timeline.json contains no sentences.')
        expected_profile = timeline.get('voice_profile_id')
        cursor = 0.0
        for index, item in enumerate(sentences, 1):
            try:
                audio_path = root / item['audio']
                actual = duration(audio_path)
                recorded = float(item['ffprobe_duration_seconds'])
                start, end = float(item['start_seconds']), float(item['end_seconds'])
                if not audio_path.is_file():
                    failures.append(f'Missing sentence audio: {item.get("audio")}')
                    continue
                if abs(actual - recorded) > 0.001:
                    failures.append(f'Sentence {index} recorded duration differs from ffprobe by over 1 ms.')
                if abs(start - cursor) > 0.001:
                    failures.append(f'Sentence {index} start is not cumulative from prior end within 1 ms.')
                if abs((end - start) - recorded) > 0.001:
                    failures.append(f'Sentence {index} end does not match its duration within 1 ms.')
                if item.get('voice_profile_id') != expected_profile:
                    failures.append(f'Sentence {index} has an unexpected voice profile.')
                cursor = end
            except (KeyError, ValueError, subprocess.CalledProcessError) as exc:
                failures.append(f'Invalid sentence {index}: {exc}')
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        if len(manifest.get('scenes', [])) != 9:
            failures.append('Manifest does not map exactly 9 scenes.')
        if manifest.get('sentence_count') != sentence_count:
            failures.append('Manifest sentence_count differs from sentence timeline.')

    for pattern, kind in [('*.srt', 'srt'), ('*.vtt', 'vtt'), ('*.ass', 'ass')]:
        files = list(root.glob(pattern))
        if files and nonblank_event_count(files[0], kind) != sentence_count:
            failures.append(f'{kind.upper()} event count does not equal sentence count.')

    if failures:
        print('FAIL')
        print('\n'.join(f'- {item}' for item in failures))
        raise SystemExit(1)
    print(f'PASS — fixed male voice and {sentence_count} sentence-synchronous caption events validated.')


if __name__ == '__main__':
    main()
