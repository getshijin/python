class solution:
    def sell_buy(self,prices):
        max_profit = 0
        print("prices list len:", len(prices))
        for i in range(1, len(prices)):
            print("i:", i)
            if prices[i] > prices[i-1]:
                print("buy_price:", prices[i-1], "sell_price:", prices[i])
                max_profit =max_profit + prices[i] -prices[i-1]
        return max_profit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    obj = solution()
    result = obj.sell_buy(prices)
    print(result)  # Output: 7

    for i in range(10):
        print("i:", i)