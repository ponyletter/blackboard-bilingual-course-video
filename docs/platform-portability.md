# Platform Portability

## What transfers unchanged

The following assets are platform-neutral and should live in Git: the scene-data schema, blackboard CSS/layout contract, question-led cover rules, narration plan, subtitle/manifest scripts, social-post contract, scene filenames, validation rules, package exclusions, and prompt templates.

## What does not transfer by itself

A skill is an instruction package, not a runtime. It cannot add a video renderer, browser research access, an image model, a TTS provider, API keys, or a GitHub login to another agent. The target platform must provide or be connected to equivalent capabilities.

| Capability | Manus route | Claude/Codex or another agent route |
|---|---|---|
| Research | Built-in web retrieval and browser | Browser/search connector or user-provided sources |
| TTS | Platform speech generation | ElevenLabs, Azure Speech, OpenAI-compatible TTS, or another configured provider |
| Cover image | Platform image generation | Configured image API or a human-designed cover |
| Video render | HyperFrames + FFmpeg | HyperFrames where available, Remotion, Playwright screenshot pipeline, or another deterministic renderer plus FFmpeg |
| Caption / manifest | Python + FFmpeg | Same Python + FFmpeg scripts |
| Publish to GitHub | Authenticated GitHub session | `git` plus authenticated GitHub CLI/token or manual push |

## Recommended repository strategy

Create a private Git repository unless all fonts, templates, images, and scripts can legally be public. Keep user-supplied Noto Sans files out of the repository by default. Commit `assets/fonts/.gitkeep` and a font setup note instead. Use Git LFS for large approved media only if you want to retain full rendered videos; otherwise keep final videos in release assets, cloud storage, or local archives.

## Agent adapters

Store `AGENTS.md` as the platform-neutral operating contract. Store `CLAUDE.md` and `CODEX.md` as thin adapters pointing to `AGENTS.md`. On a new platform, give the agent the repository URL and a precise instruction such as: “Read AGENTS.md and the blackboard-bilingual-course-video skill. Create a bilingual technical teaching video using the production contract. Before beginning, report any unavailable rendering, TTS, image, or research capability.”

## First-run checklist

Install Node.js 22+, FFmpeg 6+, Python 3.11+, and a supported HTML-to-video renderer. Place NotoSansSC Regular, SemiBold, and Bold files in `assets/fonts/`. Configure a TTS provider and an image-generation provider. Run the validator before producing the first final video. Render a short preview first when the visual system is being changed.

## Current instruction loading notes

Claude Code documents project-level skills as directories containing a required `SKILL.md` and optional supporting files. Use the same skill directory stored in this repository, and install or copy it into the skill location supported by the target Claude Code environment. Codex reads `AGENTS.md` before work begins and layers repository guidance from the project root toward the working directory; therefore the root `AGENTS.md` in this repository is the primary Codex entrypoint.[1] [2]

[1]: https://code.claude.com/docs/en/skills "Extend Claude with skills | Claude Code Docs"
[2]: https://learn.chatgpt.com/docs/agent-configuration/agents-md "Custom instructions with AGENTS.md | ChatGPT Learn"
