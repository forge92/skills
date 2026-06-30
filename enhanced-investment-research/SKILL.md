# Enhanced Investment Research - Claude Code 适配版

**描述**：提供一套基于多Agent协作、融合价值投资大师方法论与现代科学投研实践的增强版投资研究指令集。用于对上市公司进行深度分析、财务估值、行业筛选、持仓管理及投资决策辅助。

**使用场景**：当您需要对特定公司进行深度投资研究、财务估值、行业分析或风险管理时，可以使用本指令集。

## 概述

本指令集旨在通过整合多位价值投资大师（如巴菲特、芒格、段永平、李录）的智慧，并结合现代科学投资分析方法论（如因果推理、量化与质性分析结合），构建一个更科学、更全面的投资研究框架。它利用脚本和结构化输出，模拟专业投研团队的工作流程，提供深度、严谨且可解释的投资分析报告，帮助您做出更明智的投资决策。

## 核心能力

### 1. 深度公司研究

-   **多视角综合分析**：从商业模式、财务估值、竞争格局、管理层、长期确定性等多个维度，结合四位投资大师的视角进行全面评估。
-   **因果推理与护城河分析**：深入挖掘公司业务的本质和驱动因素，识别并评估其竞争优势和护城河。
-   **结构化反偏见机制**：内置信息丰富度评级、芒格式逆向检验、快速否决清单等机制，减少认知偏差。

### 2. 严谨财务分析

-   **关键数据交叉验证**：对市值、估值指标等关键财务数据进行多源交叉验证，并使用精确计算工具确保准确性。
-   **多情景估值模型**：提供乐观、中性、悲观情景下的估值分析，并进行反向 DCF 估值。

### 3. 行业与市场筛选

-   **产业链全景扫描**：从投资主题出发，构建产业链逻辑链，识别上下游投资机会。
-   **行业漏斗筛选**：通过多阶段筛选，从海量公司中精选优质标的。

### 4. 持仓与风险管理

-   **投资论文追踪**：买入后持续跟踪投资逻辑是否被证伪，及时调整策略。
-   **组合管理与优化**：提供仓位、集中度、再平衡等组合管理建议。

## 工作流程示例

### 深度公司研究工作流

**指令格式**：`/enhanced-investment-research analyze <公司名称或股票代码>`

**执行步骤**：

1.  **数据收集**：首先，您需要手动或通过其他工具获取公司的概况、财务数据、SEC 文件等基础信息。例如，可以使用 `stock-analysis` 技能或手动从雅虎财经、SEC 官网获取。
2.  **数据验证**：使用 `scripts/data_validator.py` 对关键财务数据进行交叉验证，确保数据准确性。例如：
    ```python
    # 假设您已获取到不同来源的市值数据
    data_points = [
        {'source': 'Yahoo Finance', 'value': 4.65e12},
        {'source': '公司年报', 'value': 4.64e12}
    ]
    # 在您的 Claude Code 环境中运行此脚本
    # python scripts/data_validator.py <data_points_json_string>
    ```
3.  **多维度分析**：
    -   **商业模式分析 (段永平视角)**：分析公司生意本质、护城河、竞争优势。参考 `references/investment_masters_principles.md`。
    -   **财务估值分析 (巴菲特视角)**：进行财务数据分析、估值计算、安全边际评估。使用 `scripts/financial_calculator.py` 进行精确计算，参考 `references/valuation_models.md`。
    -   **风险与竞争分析 (芒格视角)**：进行逆向思考，识别潜在风险、竞争威胁。使用 `scripts/anti_bias_check.py` 中的 `perform_reverse_thinking` 函数。
    -   **长期确定性分析 (李录视角)**：评估公司长期发展趋势、管理层文化、文明趋势。参考 `references/investment_masters_principles.md`。
4.  **反偏见检查**：使用 `scripts/anti_bias_check.py` 中的 `check_quick_veto` 和 `assess_information_richness` 函数进行快速否决和信息丰富度评级。
5.  **综合报告生成**：根据上述分析结果，结合 `templates/research_report_template.md` 模板，生成结构化的投资研究报告。报告应包含结论、评分、风险提示和建议。

### 行业筛选工作流

**指令格式**：`/enhanced-investment-research screen industry <行业名称或主题>`

**执行步骤**：

1.  **产业链分析**：构建投资逻辑链，绘制产业链全景图。参考 `references/industry_analysis_frameworks.md`。
2.  **市场扫描与粗筛**：根据预设指标（如活跃度、涨幅、市值）从全市场筛选出初步标的。
3.  **精细分析与终选**：对粗筛后的公司进行详细分析，结合组合互补性选出最终推荐标的。
4.  **输出**：行业研究报告，包含产业链分析、推荐组合及操作信号。

## 资源文件

本指令集依赖以下资源文件，请确保它们与此 `enhanced-investment-research.md` 文件处于同一目录下，或根据您的实际情况调整路径。

### `scripts/` 目录

-   `financial_calculator.py`：用于精确计算关键财务指标（如 DCF、PE、PB、市值校验）。
-   `anti_bias_check.py`：实现反偏见机制的脚本，如芒格式逆向检验、快速否决清单。
-   `data_validator.py`：用于多源数据交叉验证的脚本。

### `references/` 目录

-   `investment_masters_principles.md`：详细阐述巴菲特、芒格、段永平、李录的投资哲学和分析框架。
-   `valuation_models.md`：各种估值模型的理论与实践指南。
-   `industry_analysis_frameworks.md`：行业分析的理论框架和方法。

### `templates/` 目录

-   `research_report_template.md`：结构化投资研究报告的 Markdown 模板。
-   `checklist_template.md`：巴菲特买入前 Checklist 的模板。

## 安装指南

1.  **克隆或下载**：将此指令集所在的整个文件夹 `enhanced-investment-research-claude-code` 下载到您的本地计算机。
2.  **放置指令文件**：将 `enhanced-investment-research.md` 文件放置到 Claude Code 的 Custom Commands 目录中（具体路径请参考您的 Claude Code 文档）。
3.  **调整脚本路径**：在您调用 Python 脚本时，请确保使用正确的相对路径（例如 `python scripts/financial_calculator.py`）。

**请注意**：在 Claude Code 中，您可能需要手动执行每个步骤，并根据脚本的输出进行下一步的判断和指令输入。Manus 的 Skill 能够更自动化地协调这些步骤。
