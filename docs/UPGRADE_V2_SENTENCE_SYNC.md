# v2 Upgrade: Fixed Male Voice and Sentence-Synchronous Captions

This upgrade replaces the prior **one scene = one long narration = one static subtitle** approach. New courses must use a pinned male voice profile, one final WAV per short complete sentence, and a cumulative timeline built from the actual durations reported by `ffprobe`.

## Modified files

| File | Required change |
|---|---|
| `skill/SKILL.md` | Adds the fixed male voice lock, per-sentence audio workflow, ffprobe timing, in-video sentence captions, SRT/VTT/ASS, and validation gates. |
| `AGENTS.md` | Makes the same rules mandatory for Claude, Codex, and other repository-aware agents. |
| `README.md` | Revises the human-facing input, output, migration, and quality-gate guidance. |
| `docs/production_contract.md` | Replaces scene-level subtitle requirements with sentence-level assets, timeline data, and verification rules. |
| `docs/agent_prompts.md` | Adds explicit prompts for selecting and pinning male voice profiles and for sentence-level ffprobe timing. |
| `templates/course_request.md` | Adds user input fields for fixed male voice, provider/model/voice ID, reference sentence, and SRT/VTT/ASS. |
| `templates/course_config.example.json` | Replaces legacy scene-level narration timing fields with `voice_profile` plus per-scene `sentences` audio records. |
| `templates/blackboard_course_template.example.html` | Removes static scene narration subtitle blocks and renders only the active sentence from `SENTENCE_TIMELINE`. |
| `skill/scripts/validate_course_package.py` | Validates male voice metadata, sentence audio presence, ffprobe durations, cumulative timing, and SRT/VTT/ASS event parity. |

## New files

| File | Purpose |
|---|---|
| `docs/voice_caption_contract.md` | Defines the fixed male voice profile, short-sentence audio layout, cumulative timing algorithm, ASS rules, and acceptance gates. |
| `templates/voice_profile.example.json` | Stable, non-secret metadata template for a pinned male voice. |
| `templates/sentence_subtitle_overlay.example.js` | Exact GSAP subtitle binding example: caption appears at sentence start and disappears at sentence end. |
| `skill/scripts/build_sentence_timeline.py` | Uses ffprobe on final sentence WAVs to produce `voice_profile.json`, `sentence_timeline.json`, SRT, VTT, ASS, and `asset_manifest.json`. |
| `skill/templates/blackboard_course_template.example.html` | Same sentence-synchronous renderer included inside the installable skill. |

## Removed file

| File | Reason |
|---|---|
| `skill/scripts/make_subtitles_from_config.py` | Removed because it generated one subtitle per scene from manually supplied scene start/end times and cannot guarantee sentence-level audio synchronization. |

## New per-course output structure

```text
voice_profile.json
voice_reference.wav
audio/sentences/scene01/sentence01.wav
…
audio/scene01.wav
…
<language>_subtitles.srt
<language>_subtitles.vtt
<language>_subtitles.ass
sentence_timeline.json
asset_manifest.json
```

Do not put `voice_reference.wav`, sentence WAVs, fonts, raw audio, keys, or `.env` files into a public Git repository. A private delivery ZIP may include the final sentence WAVs and reference audio when the user requests editable voice assets; otherwise package them separately in a private audio archive.
