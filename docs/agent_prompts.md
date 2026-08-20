# Ready-to-Use Agent Prompts

## 1. New bilingual course

```text
Read AGENTS.md, skill/SKILL.md, docs/production_contract.md, docs/voice_caption_contract.md, and templates/course_request.md in this repository.

Create a bilingual Chinese-and-English blackboard-classroom technical teaching video for this topic:
[TOPIC]

Chinese cover question: [EXACT CHINESE QUESTION]
English cover question: [EXACT ENGLISH QUESTION]
Required decision angle: [WHAT THE COURSE MUST EXPLAIN]
Sources to use or verify: [URLS / PAPERS / NOTES]
Preferred TTS provider/model/voice ID: [OPTIONAL]
One multilingual male voice required across Chinese and English: [YES / NO / PROVIDER-DEPENDENT]
Must include: [ITEMS]
Must avoid: [ITEMS]

Before creating final media, report whether web research, a pinned adult-male TTS voice, image generation, HTML-to-video rendering, FFmpeg, and Git publishing are available. Then select and lock a male voice_profile for each language. Split every narration scene into short complete sentences, generate one final WAV per sentence, measure every final WAV with ffprobe, and use cumulative measured durations to generate in-video captions, SRT, VTT, ASS, sentence_timeline.json, and asset_manifest.json. A subtitle may appear only while its corresponding sentence WAV plays. Create separate Chinese and English assets. Use the question-led cover rule, fixed blackboard safe layout, and run validation before delivery.
```

## 2. Revise an existing course

```text
Read AGENTS.md and skill/SKILL.md. Revise the existing course project at [PROJECT PATH].

Requested revision: [FOR EXAMPLE: make the cover question more compelling / replace scene 4 / add English version / fix a title overlap / switch to a pinned male voice / make captions sentence-synchronous].

Preserve the blackboard visual contract, fixed male voice_profile, nine-scene mapping, fonts, question-led cover hierarchy, and all unaffected deliverables. For every changed language, regenerate changed sentence WAVs, remeasure them with ffprobe, rebuild cumulative sentence timelines, in-video captions, SRT/VTT/ASS, scene delivery WAVs, manifests, scene PNGs, contact sheets, social posts, and light ZIP packages. Validate layout, voice profile, timeline, caption counts, media specs, and package exclusions before delivery.
```

## 3. Capability-gap check on a new platform

```text
Read AGENTS.md and docs/platform-portability.md in this repository. Do not start production yet.

List whether this environment can perform: authoritative web research; TTS with a stable, named adult-male voice ID for Chinese; the same for English; reference-audio retention; image generation with accurate question text; 1920×1080 HTML-to-video rendering; ffprobe; FFmpeg concatenation; and GitHub publishing. For each unavailable capability, state the exact configured provider, local tool, API, or human input required to complete the workflow without changing the production contract.
```

## 4. Manus skill install request

```text
Install the attached blackboard-bilingual-course-video skill. Read its SKILL.md and voice_caption_contract.md. For all new videos, use a pinned adult male voice profile and sentence-synchronous captions derived from final sentence WAV durations measured by ffprobe. Keep user-supplied fonts and voice reference audio private.
```
