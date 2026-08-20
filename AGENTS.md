# Agent Operating Contract: Blackboard Bilingual Course Video

Use this repository to create or revise high-information-density technical teaching videos in a fixed monochrome blackboard-classroom visual system. Read `skill/SKILL.md`, `docs/production_contract.md`, `docs/voice_caption_contract.md`, and `templates/course_request.md` before beginning work.

## Required capability check

Before final media, identify whether the environment can perform web research, pinned-voice TTS, image generation, HTML-to-video rendering, FFmpeg processing, and Git operations. If a capability is absent, state the substitution required. Do not imply that an instruction file creates credentials, voice licenses, or media-generation access.

## Required outputs per language

| Asset | Requirement |
|---|---|
| Video | 1920×1080, 30fps, H.264 video and AAC audio. |
| Cover | Monochrome blackboard design with an exact question as the largest text. |
| Voice | One pinned adult male `voice_profile.json`, one `voice_reference.wav`, and one final WAV per complete short sentence. |
| Scene audio | Nine delivery scene WAVs concatenated from the measured sentence WAVs. |
| Captions | SRT, VTT, and ASS; one event per spoken sentence; all timings must come from final sentence WAV ffprobe durations. |
| Visual assets | Nine English-named scene PNGs plus a 3×3 contact sheet. |
| Reuse metadata | `sentence_timeline.json` and `asset_manifest.json`, including profile ID, sentence audio, hashes, text, start, end, and duration. |
| Social posts | Chinese JSON/Markdown matching the fixed length contract, plus native English JSON/Markdown with parallel meaning. |
| Archive | A light ZIP excluding fonts, dependencies, VCS folders, raw pre-tempo audio, and secrets. |

## Voice and caption hard gates

Pin a named **male** voice per language before narration. Keep provider, model, voice ID, speed multiplier, and style prompt unchanged across all sentence generations. Do not silently fall back to another voice. Split each scene into short, complete sentences before TTS. Generate one final WAV per sentence, measure it with `ffprobe`, and calculate every later subtitle start from the previous measured end. The subtitle may appear only during that sentence’s audio interval; do not use scene-long static subtitles or estimated timings.

## Hard visual constraints

Use only black, charcoal, off-white, and white. Use no connecting lines, arrows, bright colors, people, logos, or overlapping cards. Position title at `top: 176–180px`, support at `top: 272px`, cards at `top: 370px`, takeaway at `bottom: 205px`, sentence subtitles at `bottom: 48px`, and desk at the bottom. Use six independent cards per scene.

## Bilingual rule

Use equivalent decision logic but generate each language independently. Never reuse Chinese audio, timing, captions, cover wording, scene images, or social post copy as the English version. A shared multilingual male profile is permitted only if the provider supports the same named voice in both languages; otherwise preserve and disclose separate pinned male profiles.

## Validation rule

Validate layout and text contrast before render. Verify final media with ffprobe. Run `skill/scripts/validate_course_package.py <project-directory>` before delivery. It must confirm the male voice profile, every sentence WAV, no cumulative timeline gap/overlap above 1 ms, and equal SRT/VTT/ASS event counts. Keep user-supplied fonts private unless redistribution rights are explicitly confirmed.
