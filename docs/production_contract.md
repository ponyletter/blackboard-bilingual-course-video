# Production Contract

## Fixed visual system

Render at 1920×1080, 30fps, landscape. Use a monochrome blackboard classroom: black, charcoal, off-white, and white only. Use no connecting lines, arrows, colored symbols, logos, people, or visual clutter. Use NotoSansSC Regular, SemiBold, and Bold when supplied by the user.

| Element | Required position |
|---|---:|
| Title | `top: 176–180px` |
| Support line | `top: 272px` |
| Six-card grid | `top: 370px` |
| Takeaway | `bottom: 205px` |
| Synchronized subtitle | `bottom: 48px` |
| Desk | `bottom: 0`, `height: 48px` |

Use six independent grid cards. If a central theme card is necessary, place it in a separate zone; do not overlap the grid. English titles may use a smaller title size than Chinese but must remain in the title zone.

## Question-led cover

Create one 16:9 cover per language. The cover must contain an exact, readable main question, a smaller related sub-question, and six independent lower cards. The main question must be the largest element. Do not use a generic noun-only heading such as “CI/CD Explained.”

## Bilingual contract

Use the same nine-scene reasoning structure in Chinese and English. Do not reuse Chinese audio, timestamps, subtitles, or social post copy for English. Generate and measure them independently. Translate intent, examples, and tone rather than mechanically translating every sentence.

## Scene asset contract

Per language, use the following names:

```text
audio/scene01.wav … audio/scene09.wav
scenes/01_<english_slug>.png … scenes/09_<english_slug>.png
contact-sheet.png
<language>_subtitles.srt
<language>_subtitles.vtt
asset_manifest.json
```

The manifest must map scene number, English slug, start time, end time, duration, narration/audio file, scene image, and caption text. Export the scene image at a representative timestamp inside the scene rather than during a fade.

## Technical validation contract

Run layout, runtime, motion, and contrast checks before rendering. Verify final media with ffprobe: one H.264 1920×1080 30fps video stream and one AAC audio stream. The ZIP package must omit font files, dependency folders, VCS metadata, and raw pre-tempo audio.

## Reusable outputs

Each language requires an MP4, cover, SRT, VTT, nine PNGs, contact sheet, manifest, nine delivery audio files, JSON and Markdown social posts, narration/research materials, and a light ZIP package.
