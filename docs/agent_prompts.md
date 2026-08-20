# Ready-to-Use Agent Prompts

## 1. New bilingual course

```text
Read AGENTS.md, skill/SKILL.md, docs/production_contract.md, and templates/course_request.md in this repository.

Create a bilingual Chinese-and-English blackboard-classroom technical teaching video for this topic:
[TOPIC]

Chinese cover question: [EXACT CHINESE QUESTION]
English cover question: [EXACT ENGLISH QUESTION]
Required decision angle: [WHAT THE COURSE MUST EXPLAIN]
Sources to use or verify: [URLS / PAPERS / NOTES]
Must include: [ITEMS]
Must avoid: [ITEMS]

Before creating final media, report which of web research, TTS, image generation, HTML-to-video rendering, FFmpeg, and Git publishing are available in this environment. Then follow the skill workflow exactly. Create separate Chinese and English narration, timing, subtitles, covers, scene images, social posts, manifests, and light ZIP packages. Use the question-led cover rule and the fixed blackboard safe layout. Run validation before delivery.
```

## 2. Revise an existing course

```text
Read AGENTS.md and skill/SKILL.md. Revise the existing course project at [PROJECT PATH].

Requested revision: [FOR EXAMPLE: make the cover question more compelling / replace scene 4 / add English version / fix a title overlap].

Preserve the blackboard visual contract, nine-scene asset mapping, fonts, question-led cover hierarchy, and all unaffected deliverables. Re-render only the language versions affected by the change. Recreate subtitles, scene PNGs, contact sheet, manifests, social posts, and light ZIP packages for every changed language. Validate layout, media specs, and package exclusions before delivery.
```

## 3. Capability-gap check on a new platform

```text
Read AGENTS.md and docs/platform-portability.md in this repository. Do not start production yet.

List whether this environment can perform: authoritative web research, Chinese TTS, English TTS, image generation with accurate question text, 1920×1080 HTML-to-video rendering, FFmpeg processing, and GitHub publishing. For each unavailable capability, state the exact configured provider, local tool, API, or human input required to complete the workflow without changing the production contract.
```

## 4. Manus skill install request

```text
Install the attached blackboard-bilingual-course-video skill. Then read its SKILL.md and use it for a new bilingual technical teaching video. Keep user-supplied fonts private and follow the output and validation gates in the skill.
```
