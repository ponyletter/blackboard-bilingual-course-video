# Production Contract

## Fixed visual system

Render at 1920×1080, 30fps, landscape. Use a monochrome blackboard classroom: black, charcoal, off-white, and white only. Use no connecting lines, arrows, colored symbols, logos, people, or visual clutter. Use NotoSansSC Regular, SemiBold, and Bold when supplied by the user.

| Element | Required position |
|---|---:|
| Title | `top: 176–180px` |
| Support line | `top: 272px` |
| Six-card grid | `top: 370px` |
| Sentence-synchronous subtitle | `bottom: 48px` |
| Takeaway | `bottom: 205px` |
| Desk | `bottom: 0`, `height: 48px` |

Use six independent grid cards. If a central theme card is necessary, place it in a separate zone; do not overlap the grid. English titles may use a smaller title size than Chinese but must remain in the title zone.

## Question-led cover

Create one 16:9 cover per language. The cover must contain an exact, readable main question, a smaller related sub-question, and six independent lower cards. The main question must be the largest element. Do not use a generic noun-only heading such as “CI/CD Explained.”

## Bilingual and voice contract

Use the same nine-scene reasoning structure in Chinese and English, but generate and measure both languages independently. Pin one named male `voice_profile` per language before TTS. Keep its provider, model, voice ID, speed, and style prompt unchanged across every sentence. Do not silently use a fallback voice. For a multilingual provider voice, keep one shared `profile_id`; otherwise explicitly retain one male profile per language.

Read `voice_caption_contract.md` for the exact required profile metadata, sentence WAV layout, cumulative timeline, and verification gates.

## Sentence asset contract

Per language, use these names:

```text
voice_profile.json
voice_reference.wav
audio/sentences/scene01/sentence01.wav …
audio/scene01.wav … audio/scene09.wav
scenes/01_<english_slug>.png … scenes/09_<english_slug>.png
contact-sheet.png
<language>_subtitles.srt
<language>_subtitles.vtt
<language>_subtitles.ass
sentence_timeline.json
asset_manifest.json
```

Split narration into short complete sentences before TTS. Generate one final WAV per sentence. Measure every final WAV using `ffprobe`; derive sentence starts and ends by cumulative addition of those actual durations. Do not use text length, estimated speech rate, or manually entered timestamps. Each SRT, VTT, and ASS event maps one-to-one to the sentence audio segment.

The manifest must include scene data plus `voice_profile`, sentence ID, sentence text, sentence audio path, SHA-256 hash, ffprobe duration, start, end, and subtitle index.

## Technical validation contract

Run layout, runtime, motion, and contrast checks before rendering. Verify final media with ffprobe: one H.264 1920×1080 30fps video stream and one AAC audio stream. Verify every sentence WAV with ffprobe. Confirm no timeline gap or overlap above 1 ms. Confirm SRT, VTT, and ASS event counts equal the sentence record count. The ZIP package must omit font files, dependency folders, VCS metadata, raw pre-tempo audio, and all secret material.

## Reusable outputs

Each language requires an MP4, question-led cover, SRT, VTT, ASS, `voice_profile.json`, `voice_reference.wav`, `sentence_timeline.json`, nine scene PNGs, contact sheet, manifest, nine delivery scene WAVs, all final sentence WAVs, JSON and Markdown social posts, narration/research materials, and a light ZIP package.
