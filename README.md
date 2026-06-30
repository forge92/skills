# Skills

Codex / Claude Code 技能集合，通过 CC-Switch 管理。

## 已收录技能

### enhanced-investment-research

增强版投资研究 — 基于多 Agent 协作，融合价值投资大师方法论（巴菲特、芒格、段永平、李录）与现代科学投研实践。支持上市公司深度分析、财务估值、行业筛选、持仓管理及投资决策辅助。

**5 项核心能力**：深度公司研究 · 严谨财务分析 · 行业市场筛选 · 持仓风险管理 · 投资思维工具

**结构：**

```
enhanced-investment-research/
├── SKILL.md                  ← Codex 优化版（YAML 元数据 + Agent 协作）
├── scripts/
│   ├── anti_bias_check.py
│   ├── data_validator.py
│   ├── example.py
│   └── financial_calculator.py
├── references/
│   ├── api_reference.md
│   ├── industry_analysis_frameworks.md
│   ├── investment_masters_principles.md
│   └── valuation_models.md
└── templates/
    ├── checklist_template.md           ← 巴菲特买入前六关 + 镜子测试
    ├── research_report_template.md     ← 15 章完整研报模板
    └── example_template.txt
```

## 使用方式

在 CC-Switch 中添加仓库 `forge92/skills`，即可自动加载所有技能。
