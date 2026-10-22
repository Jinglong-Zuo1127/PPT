# LLM Agent代表性工作演进路线：参考资料与核实记录

制作与访问日期：2026-10-22。交付为**一页**、16:9、可编辑PowerPoint；选择原图中9项工作，没有新增原图之外的论文。

## 1. 原图来源核实及阅读范围

**Azib Farooq, Shaina Raza, Nazmul Karim, Hasan Iqbal, Athanasios V. Vasilakos, Christos Emmanouilidis.** *Evaluating and regulating agentic AI: A study of benchmarks, metrics, and regulation.* **Information Fusion 136 (2026), 104444.**

- DOI：<https://doi.org/10.1016/j.inffus.2026.104444>
- 出版商入口：<https://www.sciencedirect.com/science/article/pii/S1566253526003246>
- 作者官方仓库：<https://github.com/itsazibfarooq/agenticEvaluation>
- 作者发布的时间轴：<https://github.com/itsazibfarooq/agenticEvaluation/blob/main/static/images/timeline.png>
- 作者网页源文件及上下文：<https://github.com/itsazibfarooq/agenticEvaluation/blob/main/index.html>
- 作者提供的TechRxiv预印本：<https://www.techrxiv.org/doi/full/10.36227/techrxiv.176186841.18883348/v1>

已实际读取作者仓库README、网页源文件及时间轴图片。作者README中的书目信息与用户DOI一致，其时间轴与提供图片**内容、分组和相对布局相同**，但分辨率与留白不同，不宣称两文件逐像素相同。作者网页将图置于“Timeline of the Agentic AI papers”小节；README图注为：

> Illustrative timeline of representative agentic AI systems from 2023 to 2025, highlighting major architectural paradigms and emerging research directions.

相邻摘要将该文定位为围绕benchmarks、metrics和governance的评估综述；本图属于代表性系统的示意归纳，不是实验结果或穷尽式历史。**本环境对DOI、出版商、TechRxiv及arXiv正文请求返回代理403，未能逐字读取正式版PDF，因而不能独立确认“Figure 1”的正式编号及期刊版完整图注。** 来源身份已由作者官方发布材料交叉确认；上述英文引文来自实际读到的作者README，不冒充期刊PDF图注。

## 2. 时间口径

- 所有页面日期统一精确到**月份**。论文取其首次预印本v1所属月份；AutoGPT取官方2023-03-30公开演示所属月份。两种口径在页面与备注明确区分。
- arXiv年月编号、作者项目记录与交叉书目核对月份。未将无法直接读取的arXiv提交历史声称为已逐字查验，也不虚构日级日期。
- 正式会议年份另列，不替代预印本年份；MetaGPT的2023.08指论文v1，不是项目最早代码时间。
- 同月工作依有据日期组织：AutoGPT官方演示2023-03-30在前，CAMEL交叉书目记录2023-03-31在后；页面只展示月份。
- 横轴为按顺序排列的代表节点，**非等比例时间刻度**。能力维度长期并行，不表示严格先后或线性替代。

| 工作 | 页面首次公开月 | 时间口径 | 后续发表/说明 |
|---|---|---|---|
| ReAct | 2022.10 | 论文v1 | ICLR 2023 |
| AutoGPT | 2023.03 | 官方演示 | 开源项目；官方演示2023-03-30 |
| CAMEL | 2023.03 | 论文v1 | NeurIPS 2023 |
| Generative Agents | 2023.04 | 论文v1 | UIST 2023 |
| MetaGPT | 2023.08 | 论文v1 | ICLR 2024；本页用论文v1时间，非项目最早代码时间 |
| Mixture-of-Agents | 2024.06 | 论文v1 | 本页采用2024年预印本口径 |
| VideoMind | 2025.03 | 论文v1 | 作者技术报告2025-03-17；后续会议时间不作本页年份 |
| BrowseMaster | 2025.08 | 论文v1 | 2025年预印本；不是BrowserMaster或通用GUI点击模型 |
| Tool-R1 | 2025.09 | 论文v1 | 2025年预印本；不是VTool-R1 |

## 3. 逐项研究贡献与来源

### 1. ReAct — 2022.10

**ReAct: Synergizing Reasoning and Acting in Language Models**

贡献：交替组织推理与行动，利用观察更新决策。

日期与证据：作者ReAct仓库说明ICLR 2023并链接arXiv:2210.03629；编号确认2022年10月预印本，不能把ICLR 2023当作首次公开年。

论文：<https://arxiv.org/abs/2210.03629>

官方项目：<https://github.com/ysymyth/ReAct>

### 2. AutoGPT — 2023.03

**Auto-GPT: An Autonomous GPT-4 Experiment（原始项目README标题）**

贡献：任务分解与工具调用，支持连续自主执行。

日期与证据：官方v0.1.0 README明确标注“Demo (30/03/2023)”；官方2023年3月提交历史可核对连续执行实现。本页取项目公开演示月，不声称这是仓库最早提交时间。

官方项目：<https://github.com/Significant-Gravitas/AutoGPT>

原始版本说明：<https://github.com/Significant-Gravitas/AutoGPT/blob/v0.1.0/README.md>；历史提交：<https://github.com/Significant-Gravitas/AutoGPT/commits/master/?until=2023-03-30&since=2023-03-01>。

### 3. CAMEL — 2023.03

**CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society**

贡献：通过角色扮演式对话，探索多智能体合作。

日期与证据：作者仓库链接arXiv:2303.17760并提供NeurIPS 2023引用；BAAI-Agents/GPA-LM交叉书目列2023/03/31。本页精确到2023年3月。

论文：<https://arxiv.org/abs/2303.17760>

官方项目：<https://github.com/camel-ai/camel>

### 4. Generative Agents — 2023.04

**Generative Agents: Interactive Simulacra of Human Behavior**

贡献：用记忆、反思与规划，模拟虚拟角色行为。

日期与证据：作者仓库链接arXiv:2304.03442并给出UIST 2023正式引用；BAAI-Agents/GPA-LM列2023/04/07。本页精确到2023年4月。

论文：<https://arxiv.org/abs/2304.03442>

官方项目：<https://github.com/joonspk-research/generative_agents>

### 5. MetaGPT — 2023.08

**MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework**

贡献：以标准流程组织分工，实现协作式软件开发。

日期与证据：作者仓库正式引用为ICLR 2024；arXiv:2308.00352的v1月份为2023年8月，BAAI-Agents/GPA-LM及agent4code书目列2023/08/01。本页取论文v1时间，不等于代码项目最早发布时间。

论文：<https://arxiv.org/abs/2308.00352>

官方项目：<https://github.com/FoundationAgents/MetaGPT>

### 6. Mixture-of-Agents — 2024.06

**Mixture-of-Agents Enhances Large Language Model Capabilities**

贡献：分层聚合多模型回答，以协作改善生成结果。

日期与证据：作者Together AI仓库链接arXiv:2406.04692并解释多层响应聚合；本页使用2024年6月预印本月份，不填入未核定的正式会议日期。

论文：<https://arxiv.org/abs/2406.04692>

官方项目：<https://github.com/togethercomputer/MoA>

范围：MoA主要聚合多个LLM的响应，不必涉及真实外部环境行动；将其置于“多模型协作”节点，不把它等同于通用自主任务Agent。

### 7. VideoMind — 2025.03

**VideoMind（当前作者项目标题：A Chain-of-LoRA Agent for Temporal-Grounded Video Reasoning）**

贡献：结合规划、定位验证，实现时序定位推理。

日期与证据：作者README的News明确记录2025.03.17技术报告上线、2025.03.21代码/模型/数据集发布；arXiv:2503.13444。本页取报告月，而不是2026年正式会议时间。

论文：<https://arxiv.org/abs/2503.13444>

官方项目：<https://github.com/yeliudev/VideoMind>

### 8. BrowseMaster — 2025.08

**BrowseMaster: Towards Scalable Web Browsing via Tool-Augmented Programmatic Agent Pair**

贡献：规划与执行模块分工，结合代码化网页搜索。

日期与证据：作者sjtu-sai-agents/Browse-Master仓库链接arXiv:2508.09129，并描述Planner–Executor与code-based search；YunjiaXi搜索智能体书目同样列2025.8。

论文：<https://arxiv.org/abs/2508.09129>

官方项目：<https://github.com/sjtu-sai-agents/Browse-Master>

名称纠正：原图是 **BrowseMaster**，不是BrowserMaster。其核心是搜索规划与执行的配对，不据此宣称通用浏览器GUI点击能力。

### 9. Tool-R1 — 2025.09

**Tool-R1: Sample-Efficient Reinforcement Learning for Agentic Tool Use**

贡献：用样本高效强化学习，优化多步工具使用。

日期与证据：作者YBYBZhang/Tool-R1仓库给出同名论文标题；Adaptation of Agentic AI综述配套书目及AgentsMeetRL同时链接arXiv:2509.12867与该官方仓库，列2025.09。当前官方README极短，故仅陈述论文题名支持的样本高效强化学习与工具使用，不加入未经复核的性能数字或训练细节。

论文：<https://arxiv.org/abs/2509.12867>

官方项目：<https://github.com/YBYBZhang/Tool-R1>

身份区分：这里是arXiv:2509.12867，**不是**VTool-R1（2505.19255）；本页没有提供未经验证的GAIA分数、增益或训练预算。

## 4. 相对原图的主要日期调整

| 工作 | 参考原图位置 | 本页处理 |
|---|---|---|
| ReAct | <2023 | 明确为2022.10，不用ICLR 2023作为首次公开年 |
| CAMEL | 2023年7—12月 | 更正为2023.03 |
| Generative Agents | 2023年7—12月 | 更正为2023.04 |
| MetaGPT | 2024年8—12月 | 更正为2023.08（论文v1），正式会议为ICLR 2024 |
| VideoMind | 2025年1—4月 | 细化为2025.03报告；不使用2026正式会议年份 |
| BrowseMaster | 2025年8月 | 保留8月并纠正任务/名称解释 |
| Tool-R1 | 2025年9月 | 保留9月，核对具体论文身份 |

其他未入选工作不因留在原图中就被认为其日期已全部核实。为保证单页投影可读性，本页没有纳入EvolveSearch等其他节点。

## 5. 原图节点转录（不代表逐篇日期均已核实）

- <2023：ReAct；LLM as zero shot reasoner。
- 2023年1—6月：Chain-of-Thought；AutoGPT；Multi-Agent Collaboration。
- 2023年7—12月：Generative Agents；BabyAGI；Voyager；ChemCrow；ToolLLM；CAMEL。
- 2024年1—7月：AutoAgents；Mixture-of-Agents；TaskGen；Recursive Introspection。
- 2024年8—12月：Self-Controller；CodeTree；MetaGPT；SMoA。
- 2025年1—4月：MAS-GPT；RAIDER；VideoMind。
- 2025年5—7月：EvolveSearch；TaskCraft；MUPA；AURA；R2D2。
- 2025年8月：Video Object Segmentation Agent；Agentic-R1；BrowseMaster；GeoSR；PyVision。
- 2025年9月：ToolBrain；MapAgent；SceneWeaver；WebExplorer；Tool-R1；Astra；TUMIX。
- 2025年10月：AudioToolAgent；ACON；GuruAgents；OrcaLoca；THOR。

## 6. 使用的真实图像素材

无专属Logo的ReAct、Mixture-of-Agents、BrowseMaster、Tool-R1使用可编辑文字标识，没有以随机图片代替。

| 页面对象 | 使用文件 | 原始来源 | 处理 |
|---|---|---|---|
| AutoGPT | assets/autogpt_official_logo.png | <https://raw.githubusercontent.com/Significant-Gravitas/AutoGPT/master/autogpt_platform/frontend/public/autogpt-logo-light-bg.png> | 原始透明PNG等比缩放；为当前官方品牌标识，不声称是2023首发标识 |
| CAMEL | assets/camel_icon.png | <https://raw.githubusercontent.com/camel-ai/camel/v0.1.0/misc/logo.png> | 从原始官方Logo裁出骆驼图案；原始文件camel_original.png保留 |
| Generative Agents | assets/generative_agents_icon.png | <https://raw.githubusercontent.com/joonspk-research/generative_agents/main/environment/frontend_server/static_dirs/assets/characters/profile/Isabella_Rodriguez.png> | 项目角色Isabella头像，非项目Logo；32×32像素按最近邻放大至128×128；原始文件保留。角色美术在原仓库致谢中归于ぴぽ（@pipohi） |
| MetaGPT | assets/metagpt_icon.png | <https://raw.githubusercontent.com/FoundationAgents/MetaGPT/main/docs/resources/MetaGPT-new-log.png> | 去除白边，保留原始metagpt_logo.png；这是官方项目Logo，不用OpenAI随机图片替代 |
| VideoMind | assets/videomind_icon.png | <https://raw.githubusercontent.com/yeliudev/VideoMind/main/.github/logo.png> | 从官方完整文字标识中裁出灯泡图案；原始videomind_logo.png保留 |

裁剪仅改变留白/取景，未重新绘制或生成图标。各图均为独立PowerPoint图片对象，可替换。

## 7. 参考PPT版式分析与取舍

已完整读取《LLM演化路线PPT.pptx》，并实际导出查看其单页。尺寸13.333333×7.5英寸（16:9）。标题为微软雅黑40pt、#2E5696；蓝色重叠方块约位于(0.256,0.520)/(0.524,0.811)英寸，细线y=1.173。原红色横轴约从x=0.666至12.655、y=4.924，配红色竖线和圆形节点，项目图与名称上下错落。原节点约10pt、说明约9pt，页面外围有蓝色虚线边框，底部有蓝色总结条。

本页保留蓝色标题、重叠方块、细横线、红色主轴/节点/竖线、黑色贡献、独立图标和蓝色总结条；将轴移到y=4.0，使上方名称和下方贡献均有空间；移除原国内/国际分类与虚线外框，改为9项研究的统一路线。标题31pt，项目名18.5—20.5pt，贡献正文16pt，红色贡献关键词16pt，日期14pt；小字仅用于来源与时间口径。保留原参考的视觉语言，同时提升单页投影可读性。

## 8. 实际访问记录与交叉书目

已实际获取官方README、作者图示、原项目早期README和公开提交记录；未使用AI生成图标。以下交叉书目用于检查年月、条目身份及arXiv编号，不替代作者材料：

- <https://github.com/BAAI-Agents/GPA-LM>：CAMEL、Generative Agents与MetaGPT的日期条目。
- <https://github.com/JiaruQian/awesome-llm-based-agent4code>：MetaGPT日期交叉检查。
- <https://github.com/YunjiaXi/Awesome-Search-Agent-Papers>：BrowseMaster月份与名称。
- <https://github.com/pat-jj/Awesome-Adaptation-of-Agentic-AI>：Tool-R1对应论文与官方项目。
- <https://github.com/thinkwee/AgentsMeetRL>：Tool-R1的独立条目核对。

正文只呈现机制贡献，无编造实验数据、性能提升或“首次解决”结论。兼容性和渲染检查见validation_report.json；本机未安装Microsoft PowerPoint，不将LibreOffice验证等同于真实PowerPoint客户端测试。

作者综述仓库本次读取版本：`8a4c418d4806f5d80d539f608004cd03efe34e89`。

### 图像文件SHA256

- `autogpt_official_logo.png`：`660bfcaca774793921b164ef8b2165bd1043139a80c71e7cc632f312a8929372`
- `camel_icon.png`：`0cd5922adb376716aaf3e7c0e85df371b31911c8447efd18ba1cfbf9a1db46f6`
- `camel_original.png`：`7463dc0dffba77df6d9c1959be7a0b89b67b400ddcf13315c6314158373cad19`
- `generative_agents_character.png`：`2f04daac15a8d33a43a3d4c5f73b69878ee864a33dccc00017a5ef43eed3d233`
- `generative_agents_icon.png`：`1cd704d3c36a1faf0ba6e3dd7ee0e17eb70c38ad6fdfc418a190164cd9425c37`
- `metagpt_icon.png`：`ff0e1554395d681d26bbd22f727f64d2bcb3a5d412b8e000c1d18352fb18302d`
- `metagpt_logo.png`：`e31b117b94fea3cb6bd7d8eccb773f469e80c499b9d49082e4b4b0ddb4accbca`
- `videomind_icon.png`：`61c26d68cbcc34750e9bada5d0bd1e4eb66934286ae4692361d7fc633325e322`
- `videomind_logo.png`：`0aaf7ba6ce13d4b13d78fa5f7d6e22d55e207ba55d8a3bdff41414d8c2422825`
