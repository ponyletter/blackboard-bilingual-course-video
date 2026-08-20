---
name: blackboard-bilingual-course-video
description: Create, revise, and package high-information-density Chinese and English technical teaching videos in a fixed monochrome blackboard-classroom style. Use when a user requests blackboard explainer videos, synchronized narration and captions, bilingual/i18n video versions, question-led technical covers, per-scene social images, or reusable HyperFrames-style video production workflows.
---

# Blackboard Bilingual Course Video

Create a classroom explainer in a fixed 1920×1080 monochrome blackboard style. Default to **nine scenes**, Mandarin plus English when bilingual output is requested, nine matching audio files, nine scene PNGs, external SRT/VTT captions, validated social copy, two question-led covers, asset manifests, and light ZIP packages.

## Read First

Read `references/production_contract.md` before writing a new course. Read `references/platform-portability.md` when the workflow must run outside Manus. Read `references/social_post_contract.md` before generating Chinese social copy. Use `templates/course_request.md` as the intake structure and `templates/course_config.example.json` as the scene-data contract.

Do not distribute user-supplied fonts in public repositories or ZIP packages unless the user has confirmed redistribution rights. Use `assets/fonts/NotoSansSC-Regular.ttf`, `NotoSansSC-SemiBold.ttf`, and `NotoSansSC-Bold.ttf` when the user has supplied them; otherwise document the replacement font used.

## Creation Workflow

1. **Establish scope.** Confirm the topic, target languages, intended platforms, required duration, and whether the result is a new course or a revision. Assume Chinese and English deliverables when the user asks for i18n; create separate audio, timestamps, captions, covers, social copy, manifests, and scene PNGs for each language.

2. **Research before scripting.** Collect current, authoritative sources for technical claims. Treat “framework” and “tool” precisely. Save short research notes with source URLs before drafting the narration. Do not turn popular but unsupported opinions into facts.

3. **Write a nine-scene course.** Start with a question or tension, not a label such as “course introduction.” Make each scene answer a different decision-relevant question. Keep the conclusion conditional and practical. Adapt English narration for a natural overseas audience instead of translating Chinese word for word.

4. **Create visual scene data.** Use six independent grid cards per scene. Do not draw connecting lines. Keep a short title, a support line, six card labels, a one-line takeaway, and a complete scene subtitle. Use the supplied scene-data JSON contract.

5. **Generate narration.** Generate one audio file per scene and language. Use a clear informative voice. Use natural-language directing instructions in English before a colon, followed by spoken text in the target language. Measure actual rendered audio durations; never estimate timings mentally. Apply the chosen tempo only after generation, then compute scene starts and ends from measured durations.

6. **Generate covers.** Every cover must lead with an exact, readable question. Put the question in the largest hierarchy in the upper-center or center; put a smaller sub-question below it. Use only black, charcoal, off-white, and white. Add six independent lower cards. Avoid logos, people, bright colors, arrows, connecting lines, dense code, and generic concept-only headings.

7. **Build the blackboard composition.** Use the template rules exactly: title at `top: 176–180px`; support at `top: 272px`; card grid at `top: 370px`; takeaway at `bottom: 205px`; subtitle at `bottom: 48px`; desk at `bottom: 0` and `height: 48px`. Keep any central theme card separate from a grid; never overlap cards. Bind every audio file to its measured scene start and duration.

8. **Validate before rendering.** Run the composition checker. Resolve every layout error, contrast error, and runtime error. If an English title wraps into the support zone, shorten it or reduce only the English title size; do not allow overlap.

9. **Render and verify.** Render 1920×1080 at 30fps with H.264 video and AAC audio. Verify dimensions, codec, fps, audio, and duration with ffprobe. Use a representative in-scene timestamp for every scene PNG, then create a 3×3 contact sheet.

10. **Create reusable delivery assets.** Generate language-specific SRT and VTT from measured starts and ends. Create an `asset_manifest.json` mapping scene number, audio, image, caption, and time range. Produce Chinese social posts matching the supplied length contract; produce English social posts with the same semantic structure and native English wording. Create ZIP packages excluding fonts, dependencies, version-control folders, and raw pre-tempo audio.

## Mandatory Quality Gates

| Gate | Pass condition |
|---|---|
| Visual template | Monochrome blackboard classroom; no colored elements, arrows, connector lines, or overlapping cards. |
| Question cover | An exact question is the most prominent text, not merely a subject label. |
| Bilingual parity | Both versions cover the same decision logic, but each has independent native narration, timing, captions, cover, scene PNGs, and social post. |
| Text safety | Layout checker reports zero errors and contrast checks pass. |
| Video integrity | H.264 + AAC, 1920×1080, 30fps; expected duration is confirmed by ffprobe. |
| Reuse assets | Nine English-named scene PNGs, nine delivery audio files, SRT, VTT, contact sheet, social posts, and manifest are present per language. |
| Lightweight packaging | ZIP excludes `assets/fonts/*`, `node_modules/`, `.git/`, and `audio/*_raw.wav`. |

## Platform Routing

Use HyperFrames and the platform media-generation capabilities when available. On another platform, preserve the contracts and outputs but replace unavailable integrations: another TTS provider for narration, another image model for covers, and a deterministic HTML-to-video/FFmpeg or Remotion-compatible renderer for final video. A skill contains instructions and templates; it does **not** itself supply voice, image, browser, video-rendering, or repository credentials.

## Final Delivery

Deliver both videos first, followed by the two lightweight ZIP packages, covers, captions, social posts, manifests, contact sheets, and all scene PNGs. State the verified video specifications and identify any external requirement the target platform cannot provide.
