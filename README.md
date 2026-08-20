# Blackboard Bilingual Course Video Workflow

这个仓库将已验证的黑白黑板课堂视频流程拆成可迁移的**技能包、模板、校验脚本和平台代理入口**。它不绑定某一个视频主题，适用于技术科普、架构解释、工具比较和工程决策类课程。

> **关键边界：**仓库与技能负责保存流程、布局和质量标准；视频生成仍需要目标平台实际具备研究、TTS、图片生成、HTML-to-video 渲染、FFmpeg 和 Git 凭据等能力。仅把仓库 URL 发给其他代理，并不能自动获得这些能力或密钥。

## 本次工作中实际使用的组件

| 组件 | 本次作用 | 是否属于可迁移工作流 |
|---|---|---|
| HyperFrames | HTML 黑板课堂页面的检查和 MP4 渲染。 | 是；需 Node.js、HyperFrames 与 FFmpeg 环境。 |
| Web research | 核验技术概念、工具定位与数据来源。 | 是；需替代平台具备浏览器或搜索能力。 |
| TTS | 生成每场独立的中文、英文旁白。 | 是；需连接具体语音服务。 |
| Image generation | 生成中英文问句式封面。 | 是；需连接具体图像模型。 |
| NotoSansSC 字体 | 页面和视频的主要中英文字体。 | 是，但默认不随公开仓库分发；须自行放入 `assets/fonts/`。 |
| FFmpeg / Python | 加速音频、导出场景图、生成九宫格、字幕、清单和 ZIP。 | 是；已附带可移植脚本。 |

## 仓库结构

| 路径 | 用途 |
|---|---|
| `skill/` | 可安装的 Manus 技能包副本。 |
| `AGENTS.md` | 跨平台代理的主执行契约。 |
| `CLAUDE.md` / `CODEX.md` | Claude 与 Codex 的薄适配入口。 |
| `templates/` | 新主题输入模板和场景数据结构。 |
| `docs/` | 固定视觉规范、社交文案规范与跨平台边界。 |
| `assets/fonts/` | 私有字体放置位置；仓库只保留 `.gitkeep`。 |

## 你需要输入什么

复制并填写 [`templates/course_request.md`](templates/course_request.md) 的内容。最低限度需要提供主题、中文与英文封面的准确问句、目标平台、关键角度、必须包含/避免的内容，以及可信来源或允许代理检索的范围。

```text
请读取 AGENTS.md 和 skill/SKILL.md。
按 templates/course_request.md 为主题“[主题]”制作中英文双版本黑白黑板课堂教学视频。
先完成研究与九场景脚本；封面必须使用我给出的问句。
生成两个独立的成片、旁白、字幕、场景 PNG、社交图文、清单和轻量 ZIP。
开始前先报告本环境缺少哪些研究、TTS、图像、渲染或 Git 能力。
```

## 你会得到什么

每种语言都会得到 1920×1080、30fps、H.264 + AAC 的 MP4，一张问句式封面、九段交付旁白、九张英文命名场景 PNG、九宫格预览、SRT、VTT、`asset_manifest.json`、社交文案 JSON/Markdown 以及不含字体和依赖目录的轻量 ZIP。中文与英文版本的时间线、字幕、封面和社交文案是独立生成的，不能相互替代。

## 迁移到新 Manus 账号

将本仓库或其中的 `skill/` 保存到新账号的项目文件。导入技能时，使用 `skill/SKILL.md` 对应的安装包；随后把仓库作为同一任务的参考文件，并将自己的字体放入 `assets/fonts/`。新账号仍需要具备视频、语音和图像生成权限；技能无法转移账户权限或额度。

## 迁移到 GitHub 与其他代理

先创建**私有** GitHub 仓库。不要上传未经确认可再分发的字体、用户上传素材或包含敏感信息的 API 配置。完成首次检查后执行以下命令：

```bash
git init
git add .
git commit -m "feat: add blackboard bilingual course workflow"
git branch -M main
git remote add origin https://github.com/<YOUR-ACCOUNT>/blackboard-bilingual-course-video-workflow.git
git push -u origin main
```

之后，把 GitHub URL 和上面的标准提示词发给 Claude、Codex 或其他代理。让其先读 `AGENTS.md`，再报告能力差异。若目标环境没有 HyperFrames，可使用符合固定布局的 Remotion、Playwright 截图管线或其他 HTML-to-video 渲染器，再由 FFmpeg 进行编码和导出。

## 首次安装字体

将你有权使用的字体复制为下列路径：

```text
assets/fonts/NotoSansSC-Regular.ttf
assets/fonts/NotoSansSC-SemiBold.ttf
assets/fonts/NotoSansSC-Bold.ttf
```

可选的 Black、Medium 等权重只在需要时加入。交付 ZIP 与公开仓库默认都应排除字体。

## 质量门槛

在交付前，必须通过布局和对比度检查，使用 ffprobe 核验成片规格，并运行：

```bash
python skill/scripts/validate_course_package.py <你的课程项目目录>
```

该脚本会检查 9 段音频、9 张场景图、封面、字幕、视频、清单及其基本映射是否完整。
