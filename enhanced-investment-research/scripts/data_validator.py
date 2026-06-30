
import decimal

def cross_validate_data(data_points, tolerance=0.01):
    """
    对多个数据点进行交叉验证，检查它们之间的一致性。
    :param data_points: 包含多个数据源的列表，每个元素是一个字典，包含 'source' 和 'value'。
                        例如：[{'source': '财报', 'value': 100}, {'source': '券商报告', 'value': 101}]
    :param tolerance: 允许的最大相对偏差 (例如 0.01 表示 1%)
    :return: (bool, str) 是否通过验证，以及验证结果说明
    """
    if not data_points or len(data_points) < 2:
        return True, "数据点不足，无法进行交叉验证。"

    D = decimal.Decimal
    first_value = D(str(data_points[0]['value']))

    for i in range(1, len(data_points)):
        current_value = D(str(data_points[i]['value']))
        if first_value == 0:
            if current_value != 0:
                return False, f"数据源 '{data_points[0]['source']}' 为0，但数据源 '{data_points[i]['source']}' 不为0。"
        else:
            deviation = abs(current_value - first_value) / first_value
            if deviation > D(str(tolerance)):
                return False, f"数据源 '{data_points[0]['source']}' ({first_value}) 与 '{data_points[i]['source']}' ({current_value}) 偏差过大 ({deviation:.2%})，超出容忍度 {tolerance:.2%}。"

    return True, "所有数据点之间一致性良好，通过交叉验证。"

# 示例用法
if __name__ == "__main__":
    # 示例 1: 数据一致性良好
    data1 = [
        {'source': '公司年报', 'value': 4.65e12},
        {'source': '券商报告A', 'value': 4.64e12},
        {'source': '第三方数据', 'value': 4.66e12}
    ]
    passed, message = cross_validate_data(data1, tolerance=0.005) # 0.5% 容忍度
    print(f"验证结果: {passed}, 说明: {message}")

    # 示例 2: 数据偏差过大
    data2 = [
        {'source': '公司年报', 'value': 4.65e12},
        {'source': '券商报告B', 'value': 4.80e12} # 偏差超过 1%
    ]
    passed, message = cross_validate_data(data2, tolerance=0.01) # 1% 容忍度
    print(f"验证结果: {passed}, 说明: {message}")

    # 示例 3: 只有一个数据点
    data3 = [
        {'source': '公司年报', 'value': 100}
    ]
    passed, message = cross_validate_data(data3)
    print(f"验证结果: {passed}, 说明: {message}")

    # 示例 4: 零值情况
    data4 = [
        {'source': '公司年报', 'value': 0},
        {'source': '券商报告C', 'value': 0}
    ]
    passed, message = cross_validate_data(data4)
    print(f"验证结果: {passed}, 说明: {message}")

    data5 = [
        {'source': '公司年报', 'value': 0},
        {'source': '券商报告D', 'value': 100}
    ]
    passed, message = cross_validate_data(data5)
    print(f"验证结果: {passed}, 说明: {message}")
