#!/usr/bin/env python3
"""Build exact sentence-level SRT/VTT/ASS captions from final WAV durations measured by ffprobe."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


def duration_seconds(path: Path) -> float:
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', str(path)],
        check=True, text=True, capture_output=True,
    )
    value = float(result.stdout.strip())
    if value <= 0:
        raise ValueError(f'Non-positive duration from ffprobe: {path}')
    return value


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def stamp(value: float, separator: str) -> str:
    milliseconds = round(value * 1000)
    hours, rest = divmod(milliseconds, 3_600_000)
    minutes, rest = divmod(rest, 60_000)
    seconds, millis = divmod(rest, 1000)
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}{separator}{millis:03d}'


def ass_stamp(value: float) -> str:
    centiseconds = round(value * 100)
    hours, rest = divmod(centiseconds, 360_000)
    minutes, rest = divmod(rest, 6_000)
    seconds, centis = divmod(rest, 100)
    return f'{hours}:{minutes:02d}:{seconds:02d}.{centis:02d}'


def ass_text(text: str) -> str:
    return text.replace('\\', r'\\').replace('{', r'\{').replace('}', r'\}').replace('\n', r'\N')


def required_profile(profile: dict) -> None:
    required = ['profile_id', 'provider', 'provider_model', 'voice_id', 'voice_name', 'gender', 'language_code', 'speed_multiplier', 'style_prompt', 'reference_audio']
    missing = [key for key in required if not profile.get(key)]
    if missing:
        raise ValueError(f'voice_profile missing required fields: {", ".join(missing)}')
    if profile['gender'].lower() != 'male':
        raise ValueError('voice_profile.gender must be "male".')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('config', type=Path, help='Course config containing exactly 9 scenes and sentence audio paths.')
    parser.add_argument('--project-root', type=Path, default=Path('.'), help='Root resolving audio and reference paths.')
    parser.add_argument('--output-dir', type=Path, default=None, help='Defaults to project root.')
    parser.add_argument('--prefix', default=None, help='Subtitle basename; defaults to <language>_subtitles.')
    parser.add_argument('--verify-scene-audio', action='store_true', help='Also require each delivery scene WAV to exist.')
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding='utf-8'))
    root = args.project_root.resolve()
    out = (args.output_dir or root).resolve()
    out.mkdir(parents=True, exist_ok=True)
    language = config['language']
    profile = config['voice_profile']
    required_profile(profile)
    scenes = config['scenes']
    if len(scenes) != 9:
        raise SystemExit('Expected exactly 9 scenes.')

    reference = root / profile['reference_audio']
    if not reference.is_file():
        raise SystemExit(f'Missing voice reference audio: {reference}')
    profile = dict(profile)
    profile['reference_audio_sha256'] = sha256(reference)

    cursor = 0.0
    subtitle_index = 1
    timeline: list[dict] = []
    scene_records: list[dict] = []
    srt: list[str] = []
    vtt: list[str] = ['WEBVTT', '']
    ass_events: list[str] = []

    for expected_scene, scene in enumerate(scenes, 1):
        if int(scene.get('scene', 0)) != expected_scene:
            raise SystemExit(f'Scene sequence must be 1–9; expected {expected_scene}.')
        sentences = scene.get('sentences', [])
        if not sentences:
            raise SystemExit(f'Scene {expected_scene} has no sentence records.')
        if args.verify_scene_audio and not (root / scene['delivery_audio']).is_file():
            raise SystemExit(f'Missing delivery scene audio: {scene["delivery_audio"]}')
        scene_start = cursor
        sentence_records: list[dict] = []
        for expected_sentence, sentence in enumerate(sentences, 1):
            if int(sentence.get('sentence', 0)) != expected_sentence:
                raise SystemExit(f'Scene {expected_scene} sentence sequence must start at 1 and be consecutive.')
            text = sentence.get('text', '').strip()
            if not text:
                raise SystemExit(f'Scene {expected_scene} sentence {expected_sentence} has no text.')
            audio_path = root / sentence['audio']
            if not audio_path.is_file():
                raise SystemExit(f'Missing final sentence audio: {audio_path}')
            duration = duration_seconds(audio_path)
            start, end = cursor, cursor + duration
            record = {
                'subtitle_index': subtitle_index,
                'scene': expected_scene,
                'sentence': expected_sentence,
                'sentence_id': f'scene{expected_scene:02d}_sentence{expected_sentence:02d}',
                'text': text,
                'audio': sentence['audio'],
                'audio_sha256': sha256(audio_path),
                'ffprobe_duration_seconds': duration,
                'start_seconds': start,
                'end_seconds': end,
                'voice_profile_id': profile['profile_id'],
            }
            timeline.append(record)
            sentence_records.append(record)
            srt.extend([str(subtitle_index), f'{stamp(start, ",")} --> {stamp(end, ",")}', text, ''])
            vtt.extend([str(subtitle_index), f'{stamp(start, ".")} --> {stamp(end, ".")}', text, ''])
            ass_events.append(f'Dialogue: 0,{ass_stamp(start)},{ass_stamp(end)},Default,,0,0,0,,{ass_text(text)}')
            cursor = end
            subtitle_index += 1
        scene_records.append({
            'scene': expected_scene,
            'slug': scene['slug'],
            'start_seconds': scene_start,
            'end_seconds': cursor,
            'duration_seconds': cursor - scene_start,
            'delivery_audio': scene['delivery_audio'],
            'image': scene['image'],
            'sentences': sentence_records,
        })

    prefix = args.prefix or f'{language}_subtitles'
    srt_name, vtt_name, ass_name = f'{prefix}.srt', f'{prefix}.vtt', f'{prefix}.ass'
    (out / srt_name).write_text('\n'.join(srt), encoding='utf-8')
    (out / vtt_name).write_text('\n'.join(vtt), encoding='utf-8')
    ass_header = '''[Script Info]
Title: Sentence-Synchronous Blackboard Course Captions
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Default,Noto Sans SC,42,&H00FFFFFF,&H000000FF,&H00101010,&H96000000,1,0,0,0,100,100,0,0,1,3,0,2,120,120,48,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
'''
    (out / ass_name).write_text(ass_header + '\n'.join(ass_events) + '\n', encoding='utf-8')
    (out / 'voice_profile.json').write_text(json.dumps(profile, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (out / 'sentence_timeline.json').write_text(json.dumps({
        'language': language, 'voice_profile_id': profile['profile_id'], 'total_duration_seconds': cursor, 'sentences': timeline,
    }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    manifest = {
        'title': config.get('title', ''),
        'language': language,
        'video': {**config.get('video', {}), 'total_duration_seconds': cursor},
        'voice_profile': profile,
        'cover': config.get('cover', ''),
        'contact_sheet': config.get('contact_sheet', 'contact-sheet.png'),
        'subtitle_files': {'srt': srt_name, 'vtt': vtt_name, 'ass': ass_name},
        'sentence_timeline': 'sentence_timeline.json',
        'scenes': scene_records,
        'sentence_count': len(timeline),
        'package_exclusions': ['assets/fonts/*', 'node_modules/', '.git/', 'audio/*_raw.wav', '.env', '.env.*'],
    }
    (out / 'asset_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Wrote {len(timeline)} sentence events and {srt_name}, {vtt_name}, {ass_name}, sentence_timeline.json, voice_profile.json, and asset_manifest.json.')


if __name__ == '__main__':
    main()
