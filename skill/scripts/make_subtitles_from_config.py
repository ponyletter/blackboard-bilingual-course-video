#!/usr/bin/env python3
"""Generate SRT, VTT, and a scene asset manifest from a measured course config JSON."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def stamp(value: float, separator: str) -> str:
    milliseconds = round(value * 1000)
    hours, rest = divmod(milliseconds, 3_600_000)
    minutes, rest = divmod(rest, 60_000)
    seconds, millis = divmod(rest, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}{separator}{millis:03d}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('config', type=Path, help='Course configuration JSON with measured start/end times.')
    parser.add_argument('--output-dir', type=Path, default=Path('.'), help='Directory for output files.')
    parser.add_argument('--prefix', default=None, help='Output basename; default is course language.')
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding='utf-8'))
    language = config['language']
    scenes = config['scenes']
    if len(scenes) != 9:
        raise SystemExit('Expected exactly 9 scenes.')
    if any(float(s['end_seconds']) <= float(s['start_seconds']) for s in scenes):
        raise SystemExit('Each scene needs measured end_seconds greater than start_seconds.')

    args.output_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.prefix or f"{language}_subtitles"
    srt, vtt = [], ['WEBVTT', '']
    records = []
    for number, scene in enumerate(scenes, 1):
        start, end = float(scene['start_seconds']), float(scene['end_seconds'])
        narration = scene['narration'].strip()
        srt.extend([str(number), f"{stamp(start, ',')} --> {stamp(end, ',')}", narration, ''])
        vtt.extend([str(number), f"{stamp(start, '.')} --> {stamp(end, '.')}", narration, ''])
        records.append({
            'scene': number,
            'slug': scene['slug'],
            'start_seconds': start,
            'end_seconds': end,
            'duration_seconds': round(end - start, 3),
            'audio': scene['audio'],
            'image': scene['image'],
            'caption': narration,
        })

    srt_name, vtt_name = f'{prefix}.srt', f'{prefix}.vtt'
    (args.output_dir / srt_name).write_text('\n'.join(srt), encoding='utf-8')
    (args.output_dir / vtt_name).write_text('\n'.join(vtt), encoding='utf-8')
    manifest = {
        'title': config.get('title', ''),
        'language': language,
        'video': config.get('video', {}),
        'cover': config.get('cover', ''),
        'contact_sheet': config.get('contact_sheet', 'contact-sheet.png'),
        'subtitle_files': {'srt': srt_name, 'vtt': vtt_name},
        'voice': config.get('voice', {}),
        'scenes': records,
        'package_exclusions': ['assets/fonts/*', 'node_modules/', '.git/', 'audio/*_raw.wav'],
    }
    (args.output_dir / 'asset_manifest.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
    )
    print(f'Wrote {srt_name}, {vtt_name}, and asset_manifest.json for {language}.')


if __name__ == '__main__':
    main()
