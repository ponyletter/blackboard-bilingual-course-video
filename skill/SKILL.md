---
name: blackboard-bilingual-course-video
description: Create, revise, and package high-information-density Chinese and English technical teaching videos in a fixed monochrome blackboard-classroom style. Use when a user requests blackboard explainer videos, a stable fixed male voice, sentence-synchronous SRT/VTT/ASS captions, bilingual/i18n video versions, question-led technical covers, per-scene social images, or reusable HyperFrames-style video production workflows.
---

# Blackboard Bilingual Course Video

Create a 1920×1080 monochrome blackboard-classroom explainer. Default to **nine scenes**. In bilingual mode, create independent Chinese and English audio, timing, subtitles, covers, social copy, manifests, and scene PNGs. Use a pinned male voice profile and generate subtitles from measured sentence audio, never from estimated scene durations.

## Read First

Read `references/production_contract.md` and `references/voice_caption_contract.md` before creating or revising a course. Read `references/platform-portability.md` for a non-Manus environment and `references/social_post_contract.md` before Chinese social copy. Use `templates/course_request.md`, `templates/voice_profile.example.json`, `templates/course_config.example.json`, and `templates/blackboard_course_template.example.html` as intake, data, and render contracts.

Do not distribute user-supplied fonts unless redistribution rights are confirmed. Use supplied NotoSansSC Regular, SemiBold, and Bold locally; exclude fonts from public repositories and delivery ZIPs by default.

## Creation Workflow

1. **Establish scope and capability.** Confirm topic, languages, platforms, duration, source limits, and whether the request is new or a revision. Before final production, identify the available research, TTS, image, render, FFmpeg, and Git capabilities.

2. **Pin the voice.** Select one named male voice profile per language before narration. Record `provider`, `provider_model`, `voice_id`, `voice_name`, `gender: male`, language, speed, and style prompt. Use those exact non-secret values for every sentence in that language. Reuse one multilingual male profile across both languages only if the provider explicitly supports it; otherwise declare the two pinned language profiles. Do not silently substitute an unavailable voice.

3. **Research and script.** Collect authoritative sources before narration. Write a nine-scene course that opens with a question or tension rather than a generic course label. Adapt English for natural international comprehension rather than translating word for word.

4. **Split narration before TTS.** Divide every scene into short, semantically complete sentences. A subtitle event equals one spoken sentence. Do not create word-by-word fragments or use one long static subtitle for an entire scene.

5. **Generate and measure sentence audio.** Generate one final, tempo-adjusted WAV per sentence using the pinned male profile. Name files `audio/sentences/sceneNN/sentenceNN.wav`. Measure each final WAV with `ffprobe`. Concatenate sentence WAVs into `audio/sceneNN.wav` only after measurement. Do not calculate times from text length or provider estimates.

6. **Build the timeline and captions.** Run `scripts/build_sentence_timeline.py` with the course config and project root. It must derive all start/end times cumulatively from ffprobe durations and emit SRT, VTT, ASS, `sentence_timeline.json`, and `asset_manifest.json`. Render in-video captions from this sentence timeline, with only the currently spoken sentence visible.

7. **Create visuals and covers.** Use six independent grid cards per scene and no connecting lines. Every cover needs an exact question as its most prominent text. Use only black, charcoal, off-white, and white.

8. **Build the composition.** Follow fixed safe zones exactly: title `top: 176–180px`; support `top: 272px`; grid `top: 370px`; takeaway `bottom: 205px`; sentence subtitle `bottom: 48px`; desk at `bottom: 0`, `height: 48px`. Bind the video’s sentence subtitle layer to the generated timeline. Never overlap title, support, cards, takeaway, or subtitles.

9. **Validate and render.** Run layout, runtime, motion, and contrast checks. Render 1920×1080, 30fps, H.264 + AAC. Verify media with ffprobe. Run `scripts/validate_course_package.py` before delivery; it must confirm the pinned male profile, sentence files, cumulative timing, captions, and required assets.

10. **Deliver reusable assets.** Per language provide the MP4, question-led cover, nine scene WAVs, all final sentence WAVs, nine scene PNGs, contact sheet, SRT, VTT, ASS, sentence timeline, manifest, social JSON/Markdown, and a light ZIP. Exclude fonts, dependencies, VCS files, raw pre-tempo audio, and secrets.

## Mandatory Quality Gates

| Gate | Pass condition |
|---|---|
| Voice identity | Every sentence declares the expected pinned male `profile_id`; no fallback voice is used. |
| Sentence timing | Each subtitle start/end comes from the final sentence WAV measured by ffprobe; every start equals the previous end within 1 ms. |
| Caption parity | SRT, VTT, and ASS have one event per spoken sentence in identical order. |
| Visual template | Monochrome blackboard classroom; no colorful elements, arrows, connector lines, or overlapping cards. |
| Question cover | An exact question is the most prominent cover text, not merely a subject label. |
| Bilingual parity | Versions share decision logic but use independently generated native narration, timing, captions, covers, and social posts. |
| Video integrity | H.264 + AAC, 1920×1080, 30fps; duration is verified by ffprobe. |
| Reuse assets | Per language: 9 scene PNGs, 9 scene WAVs, all sentence WAVs, SRT, VTT, ASS, timeline, contact sheet, posts, and manifest. |
| Lightweight packaging | ZIP excludes `assets/fonts/*`, `node_modules/`, `.git/`, `audio/*_raw.wav`, and secrets. |

## Platform Routing

Use HyperFrames plus available media-generation capabilities when present. On another platform, retain the contracts but configure equivalent TTS, image, and deterministic render providers. A skill supplies workflow and scripts; it does not provide provider credentials, voice licenses, media APIs, browser access, or GitHub authorization.

## Final Delivery

Deliver language videos first, then ZIPs, covers, SRT/VTT/ASS captions, voice profiles, sentence timelines, manifests, contact sheets, social posts, and scene PNGs. State verified video specs, pinned voice profile IDs, subtitle event counts, and any unavailable external capability.
