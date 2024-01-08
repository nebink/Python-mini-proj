def maxProfit(prices, n):
	buy = prices[0]
	max_profit = 0
	for i in range(1, n):


		if (buy > prices[i]):
			buy = prices[i]


		elif (prices[i] - buy > max_profit):
			max_profit = prices[i] - buy
	return max_profit



if __name__ == '__main__':

	prices = [7, 1, 5, 6, 4]
	n = len(prices)
	max_profit = maxProfit(prices, n)
	print(max_profit)
