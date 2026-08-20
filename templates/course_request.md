# Blackboard Course Request

```text
Create a bilingual blackboard-classroom teaching video.

Topic: [one precise question or technical decision]
Chinese audience/platforms: [for example: Bilibili, WeChat Video, Xiaohongshu]
English audience/platforms: [for example: YouTube, LinkedIn, X]
Target languages: Chinese + English / [other]
Requested duration per language: [for example: 3–4 minutes]
Main question for Chinese cover: [exact question]
Main question for English cover: [exact question]
Required angle: [comparison, decision framework, architecture, failure analysis, etc.]
Must include: [tools, examples, current facts, citations]
Must avoid: [claims, brands, visual elements, opinions]
Source materials: [URLs, papers, notes]
Font assets available: [path or no]

Voice lock:
- Voice requirement: fixed adult male voice
- Preferred provider/model/voice ID: [if known; otherwise ask agent to select and pin one]
- One multilingual male voice required across Chinese and English: yes / no / provider-dependent
- Speed multiplier: [for example: 1.28]
- Reference sentence for voice check: [one short sentence]

Caption contract:
- Split narration into short complete sentences before TTS: required
- Generate one final sentence WAV and one subtitle event per short sentence: required
- Measure final sentence WAV duration with ffprobe and build cumulative timing: required
- Deliver SRT + VTT + ASS + sentence_timeline.json: required

Deliver per language:
- 1920×1080 H.264/AAC MP4 at 30fps
- Question-led cover image
- `voice_profile.json` and `voice_reference.wav`
- 9 scene delivery WAVs and all measured sentence WAVs
- 9 scene PNGs with English filenames and a 3×3 contact sheet
- SRT, VTT, ASS, `sentence_timeline.json`, and `asset_manifest.json`
- Social post JSON and Markdown
- Light ZIP excluding fonts, node_modules, .git, raw audio, and secrets
```

Use this request as a contract. If the target platform cannot pin a male voice or measure sentence WAVs with ffprobe, state the gap before creating any final media.
