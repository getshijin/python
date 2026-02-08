class solution:
    def buy_sell(self, prices):
        max_profit = 0
        buy_pice = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < buy_pice:
                buy_pice = prices[i]
            else:
                print("buy_price:", buy_pice, "sell_price:", prices[i])
                profit = prices[i] - buy_pice
                max_profit = max(max_profit, profit)
        return max_profit

if __name__ == "__main__":
    prices = [7, 3, 5, 1, 2, 4]
    obj = solution()
    result = obj.buy_sell(prices)
    print(result)  # Output: 5
