# Blackboard Bilingual Course Video Workflow

这个仓库将已验证的黑白黑板课堂视频流程拆成可迁移的**技能包、模板、校验脚本和平台代理入口**。它不绑定某一个视频主题，适用于技术科普、架构解释、工具比较和工程决策类课程。

> **关键边界：**仓库与技能负责保存流程、布局和质量标准；视频生成仍需要目标平台实际具备研究、可锁定音色的 TTS、图片生成、HTML-to-video 渲染、FFmpeg 和 Git 凭据等能力。仅把仓库 URL 发给其他代理，并不能自动获得这些能力、音色许可或密钥。

## 本次工作中实际使用的组件

| 组件 | 本次作用 | 是否属于可迁移工作流 |
|---|---|---|
| HyperFrames | HTML 黑板课堂页面的检查和 MP4 渲染。 | 是；需 Node.js、HyperFrames 与 FFmpeg 环境。 |
| Web research | 核验技术概念、工具定位与数据来源。 | 是；需替代平台具备浏览器或搜索能力。 |
| Pinned TTS | 用固定男声音色生成每条短句的中文、英文旁白。 | 是；需连接可指定稳定 voice ID 的语音服务。 |
| Image generation | 生成中英文问句式封面。 | 是；需连接具体图像模型。 |
| NotoSansSC 字体 | 页面和视频的主要中英文字体。 | 是，但默认不随公开仓库分发；须自行放入 `assets/fonts/`。 |
| FFmpeg / Python | 实测每条短句音频、生成时间轴、字幕、清单、场景图、九宫格和 ZIP。 | 是；已附带可移植脚本。 |

## 仓库结构

| 路径 | 用途 |
|---|---|
| `skill/` | 可安装的 Manus 技能包副本。 |
| `AGENTS.md` | 跨平台代理的主执行契约。 |
| `CLAUDE.md` / `CODEX.md` | Claude 与 Codex 的薄适配入口。 |
| `templates/` | 新主题输入、固定音色、逐句字幕和页面结构模板。 |
| `docs/` | 固定视觉规范、音色/字幕契约、社交文案规范与跨平台边界。 |
| `assets/fonts/` | 私有字体放置位置；仓库只保留 `.gitkeep`。 |

## 你需要输入什么

复制并填写 [`templates/course_request.md`](templates/course_request.md)。除主题、双语封面问句、目标平台、内容角度和可信来源外，还要明确“固定成年男声”、首选语音服务/模型/voice ID、是否要求两种语言同一多语音色，以及语速。若没有指定 voice ID，代理必须先选择、报告并锁定一个男声音色，不能在不同场景自动换声。

```text
请读取 AGENTS.md 和 skill/SKILL.md。
按 templates/course_request.md 为主题“[主题]”制作中英文双版本黑白黑板课堂教学视频。
先锁定每种语言的男性 voice_profile，再完成研究与九场景短句脚本。
每条短句必须单独生成最终 WAV，由 ffprobe 测得时长后累计生成视频时间轴和 SRT/VTT/ASS。
封面必须使用我给出的问句；视频内字幕只能在其对应短句音频期间显示。
生成两个独立的成片、音色档案、短句音频、字幕、场景 PNG、社交图文、清单和轻量 ZIP。
开始前先报告本环境缺少哪些研究、固定 TTS、图像、渲染或 Git 能力。
```

## 你会得到什么

每种语言都会得到 1920×1080、30fps、H.264 + AAC 的 MP4，一张问句式封面、一个固定男声 `voice_profile.json` 和 `voice_reference.wav`、9 段交付场景 WAV、全部短句 WAV、九张英文命名场景 PNG、九宫格预览、逐句同步的 SRT、VTT、ASS、`sentence_timeline.json`、`asset_manifest.json`、社交文案 JSON/Markdown 以及不含字体和依赖目录的轻量 ZIP。中文与英文版本的音色配置、短句音频、时间线、字幕、封面和社交文案独立生成，不能相互替代。

## 迁移到新 Manus 账号

将本仓库或其中的 `skill/` 保存到新账号的项目文件。导入技能时，使用 `skill/SKILL.md` 对应的安装包；随后把仓库作为同一任务的参考文件，并将自己的字体放入 `assets/fonts/`。新账号仍需要具备视频、固定音色语音和图像生成权限；技能无法转移账户权限、额度或第三方语音服务的 voice ID。

## 迁移到 GitHub 与其他代理

先创建**私有** GitHub 仓库。不要上传未经确认可再分发的字体、用户上传素材、参考音频、成片、短句音频或包含敏感信息的 API 配置。完成首次检查后执行以下命令：

```bash
git init
git add .
git commit -m "feat: add sentence-synchronous blackboard video workflow"
git branch -M main
git remote add origin https://github.com/<YOUR-ACCOUNT>/blackboard-bilingual-course-video-workflow.git
git push -u origin main
```

之后，把 GitHub URL 和上面的标准提示词发给 Claude、Codex 或其他代理。让其先读 `AGENTS.md`，再报告能力差异。若目标环境没有 HyperFrames，可使用符合固定布局的 Remotion、Playwright 截图管线或其他 HTML-to-video 渲染器，再由 FFmpeg 进行编码和导出；但不可省略固定 voice profile 与 ffprobe 实测短句时间轴。

## 首次安装字体

将你有权使用的字体复制为下列路径：

```text
assets/fonts/NotoSansSC-Regular.ttf
assets/fonts/NotoSansSC-SemiBold.ttf
assets/fonts/NotoSansSC-Bold.ttf
```

可选的 Black、Medium 等权重只在需要时加入。交付 ZIP 与公开仓库默认都应排除字体。

## 质量门槛

在交付前，必须通过布局和对比度检查，使用 ffprobe 核验成片规格和每条最终短句 WAV，并运行：

```bash
python skill/scripts/validate_course_package.py <你的课程项目目录>
```

该脚本会检查 9 段场景音频、短句音频、固定男声音色档案、连续无估算的时间轴、SRT/VTT/ASS 事件数、9 张场景图、封面、视频和清单是否完整。
