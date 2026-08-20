# CI/CD 双语课程研究笔记

## 已核验基础概念

| 主题 | 可用于课程的事实表述 | 课程表达边界 | 来源 |
|---|---|---|---|
| CI/CD 的含义 | GitHub 将 CI/CD 描述为通过自动化构建、测试和部署改善软件开发、实现更快且更可靠交付的一组实践和工具。 | 不能把 CI/CD 缩减为一段部署脚本；自动化要覆盖可验证的交付过程。 | [GitHub][1] |
| CI | CI 自动构建、测试并将变更集成到共享仓库。 | 重点是频繁集成与快速反馈，而不只是触发一次命令。 | [GitHub][1] |
| 持续交付与持续部署 | 持续交付可将变更自动交付到生产就绪环境、等待批准；持续部署则在通过所需测试后自动面向客户发布。 | 二者都可属于 CI/CD；持续部署并非成熟度的唯一终点。 | [GitHub][1] |
| 流水线组成 | GitLab 的示例将流水线表示为阶段与作业：阶段决定执行顺序，作业执行编译、测试、部署等任务。 | “写脚本”可以是流水线作业的一部分，但脚本本身不等于完整 CI/CD。 | [GitLab][2] |
| 运行器与变量 | GitLab Runner 执行作业；CI/CD 变量可以将配置与敏感信息传递给作业，并提供受保护、掩码等安全控制。 | 大团队依赖的重点还包括可重复运行环境、密钥管理、审计与访问控制。 | [GitLab][2] |
| 可复用流水线组件 | GitLab 将 CI/CD component 定义为可复用的流水线配置单元，以降低重复、提升可维护性和跨项目一致性。 | 大团队使用 CI/CD 的价值，在于把工程规范产品化并可复用。 | [GitLab][2] |

## 待补充工具分类

课程中将把“主流框架”精确表述为**工具链与平台类别**：

1. 代码托管一体化流水线：GitHub Actions、GitLab CI/CD。
2. 可自建自动化服务器：Jenkins。
3. 云托管流水线服务：CircleCI 等。
4. Kubernetes GitOps 持续交付：Argo CD、Flux 等。
5. 可组合的云原生流水线构建块：Tekton 等。

这些类别可组合使用；例如 Jenkins 或 GitHub Actions 负责构建、测试和制品，Argo CD 负责将 Git 中声明的期望状态同步至 Kubernetes。因此不应将工具名称当作互斥的“框架阵营”。

## References

[1]: https://github.com/resources/articles/ci-cd "What is CI/CD? · GitHub"
[2]: https://docs.gitlab.com/ci/ "Get started with GitLab CI/CD | GitLab Docs"

## 工具类别补充

| 工具类别 | 可核验定位 | 视频中应怎样解释 | 来源 |
|---|---|---|---|
| Jenkins | Jenkins Pipeline 是一组插件，用于在 Jenkins 中实现并集成持续交付流水线；其 Jenkinsfile 可版本化、评审并保留审计轨迹。 | Jenkins 的确可以“写脚本”，但生产级 Pipeline-as-Code 还包含阶段、执行节点、构件、测试、审批、权限与可观测性等工程边界。 | [Jenkins][3] |
| Argo CD | Argo CD 是 Kubernetes 的声明式 GitOps 持续交付工具，以 Git 仓库为期望应用状态的事实来源，并将目标状态自动或手动同步到环境。 | Argo CD 通常偏向部署与运行状态同步，不必单独承担全部编译与测试职责；它可与 CI 工具组合。 | [Argo CD][4] |

## 课程中的发布成熟度表述

“手动发版”不必然错误。小团队可能在变更频率低、风险可控、测试覆盖尚未完善、基础设施能力有限时，保留人工发布或人工批准。但如果只依赖某台机器上的个人脚本，常会缺少环境一致性、版本可追溯、测试门禁、密钥治理、回滚路径和审计记录。合理的演进路径是先把脚本纳入版本控制和可重复执行环境，再逐步增加构建、测试、制品、部署审批、观察与回滚能力，而不是一开始追求复杂的平台。

[3]: https://www.jenkins.io/doc/book/pipeline/ "Pipeline | Jenkins"
[4]: https://argo-cd.readthedocs.io/en/stable/ "Argo CD - Declarative GitOps CD for Kubernetes"
