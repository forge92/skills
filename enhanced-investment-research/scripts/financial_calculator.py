
import decimal

def calculate_market_cap(price, shares_outstanding, currency='USD'):
    """
    计算市值。
    :param price: 股票价格
    :param shares_outstanding: 总股本
    :param currency: 货币单位 (e.g., 'USD', 'HKD', 'CNY')
    :return: 市值和货币单位
    """
    D = decimal.Decimal
    market_cap = D(str(price)) * D(str(shares_outstanding))
    return market_cap, currency

def calculate_pe_ratio(market_cap, net_income):
    """
    计算市盈率 (PE Ratio)。
    :param market_cap: 市值
    :param net_income: 净利润
    :return: 市盈率
    """
    D = decimal.Decimal
    if D(str(net_income)) == 0:
        return D('0')
    pe_ratio = D(str(market_cap)) / D(str(net_income))
    return pe_ratio

def calculate_pb_ratio(market_cap, book_value):
    """
    计算市净率 (PB Ratio)。
    :param market_cap: 市值
    :param book_value: 账面价值
    :return: 市净率
    """
    D = decimal.Decimal
    if D(str(book_value)) == 0:
        return D('0')
    pb_ratio = D(str(market_cap)) / D(str(book_value))
    return pb_ratio

def calculate_roe(net_income, equity):
    """
    计算净资产收益率 (ROE)。
    :param net_income: 净利润
    :param equity: 股东权益
    :return: ROE
    """
    D = decimal.Decimal
    if D(str(equity)) == 0:
        return D('0')
    roe = (D(str(net_income)) / D(str(equity))) * D('100')
    return roe

# 示例用法
if __name__ == "__main__":
    price = 510
    shares = 9.11e9
    reported_market_cap = 4.65e12
    currency = 'HKD'

    market_cap, mc_currency = calculate_market_cap(price, shares, currency)
    print(f"计算市值: {market_cap:.2f} {mc_currency}")

    # 验证市值
    deviation = abs(market_cap - decimal.Decimal(str(reported_market_cap))) / decimal.Decimal(str(reported_market_cap)) * decimal.Decimal('100')
    print(f"与报告市值偏差: {deviation:.2f}%")

    net_income = 100000000000  # 假设净利润
    book_value = 2000000000000 # 假设账面价值
    equity = 2000000000000 # 假设股东权益

    pe = calculate_pe_ratio(market_cap, net_income)
    print(f"市盈率 (PE): {pe:.2f}")

    pb = calculate_pb_ratio(market_cap, book_value)
    print(f"市净率 (PB): {pb:.2f}")

    roe = calculate_roe(net_income, equity)
    print(f"净资产收益率 (ROE): {roe:.2f}%")
