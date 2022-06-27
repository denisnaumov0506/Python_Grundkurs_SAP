stocks = [
    ["SAP", 106, -3.0],
    ["AAPL", 165, 1.25],
    ["TSLA", 860, 54.2],
    ["ORCL", 76, -0.25],
    ["ZM", 114, 6.2]
    ]

sell_list = []

for stock in stocks:
    if abs(stock[1]/(stock[1]+stock[2])*100-100) > 5:
        sell_list.append(stock[0])

print(sell_list)
