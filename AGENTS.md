# Agent Operating Contract: Blackboard Bilingual Course Video

Use this repository to create or revise high-information-density technical teaching videos in a fixed monochrome blackboard-classroom visual system. Read `skill/SKILL.md`, `docs/production_contract.md`, and `templates/course_request.md` before beginning work.

## Required capability check

Before producing final media, identify whether the environment can perform web research, TTS, image generation, HTML-to-video rendering, FFmpeg processing, and Git operations. If a capability is absent, state the substitution required. Do not imply that an instruction file creates credentials or media-generation access.

## Required outputs per language

| Asset | Requirement |
|---|---|
| Video | 1920×1080, 30fps, H.264 video and AAC audio. |
| Cover | Monochrome blackboard design with an exact question as the largest text. |
| Audio | Nine measured scene WAV files. |
| Visual assets | Nine English-named scene PNGs plus a 3×3 contact sheet. |
| Captions | Independent SRT and VTT generated from measured timings. |
| Reuse metadata | `asset_manifest.json` mapping each scene, audio, image, caption, and time range. |
| Social posts | Chinese JSON/Markdown matching the fixed length contract, plus native English JSON/Markdown with parallel meaning. |
| Archive | A light ZIP excluding fonts, dependencies, VCS folders, and raw pre-tempo audio. |

## Hard visual constraints

Use only black, charcoal, off-white, and white. Use no connecting lines, arrows, bright colors, people, logos, or overlapping cards. Position title at `top: 176–180px`, support at `top: 272px`, cards at `top: 370px`, takeaway at `bottom: 205px`, subtitles at `bottom: 48px`, and desk at the bottom. Use six independent cards per scene.

## Bilingual rule

Use equivalent decision logic but generate each language independently. Never reuse Chinese audio, timing, captions, cover wording, scene images, or social post copy as the English version. Adapt the English story for a natural international audience.

## Validation rule

Validate layout and text contrast before render. Verify final media with ffprobe. Run `skill/scripts/validate_course_package.py <project-directory>` before delivery. Keep user-supplied fonts private unless their redistribution rights are explicitly confirmed.
