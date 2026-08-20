# 通用黑白教室教学视频母版：安全布局与二次发布规范

## 一、固定视觉与字体规则

视频使用黑白教室、黑板、吊灯、白色边框和无连接线分区画布。中文优先加载用户提供的 `NotoSansSC` 字体；优先字重为 Regular、SemiBold、Bold、Black。字体保留在本地工程的 `assets/fonts/` 供渲染使用，但发布压缩包必须排除 `assets/fonts/*`，避免增大下载体积。

## 二、不可重叠的垂直安全区

| 区域 | 固定位置与规则 |
|---|---|
| 标题 | `top: 180px`，独立于支持说明和主体内容。 |
| 支持说明 | `top: 272px` 左右，独立于标题和主题卡片。 |
| 中心主题卡片 | 仅用于一个主题定义；其下方必须至少留出 `36px` 空隙。 |
| 单行分区卡片 | 当出现中心主题时，固定从 `top: 500px` 开始；不与中心主题同一垂直带重叠。 |
| 多行网格 | 从 `top: 370px–400px` 开始；不可与中心主题同时使用，除非专门设置独立区域。 |
| 小总结 | 固定 `bottom: 205px`，位于黑板下沿以上、字幕区之外；不得压住黑板框。 |
| 同步字幕 | 固定 `bottom: 48px` 左右，作为最底部独立区域。 |

> 中心主题卡片与分区卡片不允许以层叠方式表达关系。关系应依靠顺序、分组、标题和留白表达，不使用连接线。

## 三、逐段图片与音频映射

每个旁白场景必须导出一张 1920×1080 PNG，PNG 文件名只使用英文、小写、数字、连字符和下划线，并按音频顺序编号。示例：

```text
scenes/
  01_problem-hook.png
  02_core-definition.png
  03_workflow-loop.png
  04_context-layer.png
  05_tools-layer.png
  06_control-layer.png
  07_feedback-boundaries.png
  08_tradeoffs.png
  09_summary.png
```

每个项目必须同时输出 `exports/asset_manifest.json`，为每个场景记录开始时间、结束时间、音频路径、PNG 路径和英文场景名称。PNG 数量必须与音频段数、字幕提示条数一致；打包前执行数量校验。

## 四、交付与压缩包规则

压缩包应包含成片、SRT、VTT、英文逐段 PNG、联系表、素材清单、社交文案 JSON/Markdown、旁白脚本、研究笔记和 HTML 源码。压缩包必须排除 `node_modules/`、`.git/` 和 `assets/fonts/`；字体不作为下载包内容交付。
