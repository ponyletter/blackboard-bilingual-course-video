# Fixed Male Voice and Sentence-Synchronous Caption Contract

## Voice identity lock

Use a named **male** `voice_profile` for every course. Store the profile in each language configuration and copy it into `asset_manifest.json`. The profile must include `provider`, `provider_model`, `voice_id`, `voice_name`, `gender: "male"`, `language_code`, `speed_multiplier`, `style_prompt`, and a stable `profile_id`.

Use the same provider, provider model, voice ID, speed, and style prompt for every scene in a language. If one licensed multilingual male voice supports both Chinese and English, keep one shared `profile_id` across the bilingual course. If that is impossible, use one pinned male profile per language and label the limitation; do not claim that two unrelated provider voices are the same speaker.

Generate and retain a short `voice_reference.wav` and `voice_profile.json` per profile. The JSON must include a SHA-256 hash of the reference audio and the exact non-secret TTS parameters. Never place API keys in the profile. If the provider removes or changes a voice/model, stop and request approval for a controlled re-baseline; do not silently substitute another voice.

## Sentence audio contract

Split each scene narration into semantically complete short sentences before TTS. Prefer one readable thought per sentence; avoid sentence fragments, artificial word-level splits, and subtitle lines that remain on screen longer than the spoken thought.

Generate one final, tempo-adjusted WAV per sentence:

```text
audio/sentences/scene01/sentence01.wav
audio/sentences/scene01/sentence02.wav
…
audio/scene01.wav
```

Measure every final sentence WAV with `ffprobe`; do not derive duration from text length, a TTS estimate, or manual timing. Concatenate the measured sentence WAVs in order to create the scene delivery WAV. Do not insert an untracked silence gap. If intentional silence is required, generate it as an explicit WAV segment and include it in the timeline.

## Timeline contract

Start at `0.000` seconds for the first sentence. For every later sentence, set `start_seconds` to the previous segment’s measured `end_seconds`; set `end_seconds = start_seconds + ffprobe_duration`. Build scene start/end from the first and last sentence in that scene. Build the video duration from the final sentence end.

Generate **SRT, VTT, and ASS** from the same sentence timeline. Each subtitle event must use the sentence text and exactly match its sentence audio segment. SRT/VTT use millisecond formatting. ASS uses its native centisecond time format derived from the same measured timeline; its formatting quantization is at most 10 ms and is not a manual estimate.

## Caption appearance

Render in-video subtitles from the sentence timeline, not from one static scene narration string. Keep the fixed subtitle safe zone at `bottom: 48px`. Use the available NotoSansSC font family for Chinese and an approved fallback for English. External ASS should be styled for white text, black outline, centered alignment, and 1920×1080 video.

## Verification gates

| Gate | Required result |
|---|---|
| Voice lock | Every sentence records the expected `profile_id`; all profile fields match the language configuration. |
| Male voice | `gender` is explicitly `male`; no automatic voice fallback is allowed. |
| Duration source | Every sentence record has a final file, ffprobe duration, and SHA-256 hash. |
| Timeline | Each start equals the prior end within 1 ms; scene audio duration equals the sum of its sentence files. |
| Captions | SRT, VTT, and ASS have one event per spoken sentence, in identical order and from the same timeline. |
| Manifest | Sentence-level records map text, audio, start, end, duration, and voice profile. |

## Required configuration shape

Use `voice_profile` at the top level and `sentences` inside every scene. See `templates/course_config.example.json`. The legacy scene-level `narration` and one-scene-one-caption model is not sufficient for new productions.
