
import json

def check_quick_veto(company_info):
    """
    执行快速否决清单检查。
    :param company_info: 包含公司信息的字典
    :return: (bool, str) 是否通过否决，以及否决理由
    """
    veto_reasons = []

    # 示例否决规则：管理层诚信污点
    if company_info.get("management_integrity_issue"): # 假设 company_info 中有此字段
        veto_reasons.append("管理层存在诚信污点，一票否决。")

    # 示例否决规则：商业模式不清晰
    if not company_info.get("business_model_clarity"): # 假设 company_info 中有此字段
        veto_reasons.append("商业模式不清晰，无法理解其盈利逻辑，一票否决。")

    # 可以添加更多否决规则

    if veto_reasons:
        return False, "; ".join(veto_reasons)
    return True, "通过快速否决清单检查。"

def perform_reverse_thinking(company_name, potential_risks):
    """
    执行芒格式逆向思考：思考公司可能失败的场景。
    :param company_name: 公司名称
    :param potential_risks: 潜在风险列表
    :return: 逆向思考结果字符串
    """
    if not potential_risks:
        return f"对 {company_name} 进行逆向思考：目前未识别到明显的失败场景。"

    analysis = [f"对 {company_name} 进行逆向思考：思考其可能失败的场景。"]
    for i, risk in enumerate(potential_risks):
        analysis.append(f"  {i+1}. 如果 {risk} 发生，公司将面临巨大挑战。")
    return "\n".join(analysis)

def assess_information_richness(data_sources):
    """
    评估信息丰富度（A/B/C级）。
    :param data_sources: 包含数据来源和质量的列表
    :return: (str, str) 评级和说明
    """
    reliable_sources_count = sum(1 for source in data_sources if source.get("reliability") == "high")
    total_sources = len(data_sources)

    if reliable_sources_count >= 3 and total_sources >= 5:
        return "A", "信息丰富度高，数据来源广泛且可靠，置信度强。"
    elif reliable_sources_count >= 1 and total_sources >= 3:
        return "B", "信息丰富度中等，部分数据来源可靠，但仍需谨慎。"
    else:
        return "C", "信息丰富度低，数据来源有限或可靠性存疑，推算指标需标注置信度。"

# 示例用法
if __name__ == "__main__":
    company_data = {
        "management_integrity_issue": False,
        "business_model_clarity": True
    }
    passed, reason = check_quick_veto(company_data)
    print(f"快速否决检查: {passed}, 理由: {reason}")

    risks = [
        "市场竞争加剧导致份额下降",
        "核心技术被颠覆",
        "监管政策发生重大不利变化"
    ]
    reverse_analysis = perform_reverse_thinking("拼多多", risks)
    print(reverse_analysis)

    sources = [
        {"name": "公司年报", "reliability": "high"},
        {"name": "行业研究报告", "reliability": "medium"},
        {"name": "新闻报道", "reliability": "low"},
        {"name": "券商研报", "reliability": "high"},
        {"name": "第三方数据平台", "reliability": "high"}
    ]
    richness_rating, richness_desc = assess_information_richness(sources)
    print(f"信息丰富度评级: {richness_rating}, 说明: {richness_desc}")
