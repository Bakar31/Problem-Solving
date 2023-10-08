"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
"""

def maxProfit(prices):
    lowest_price = prices[0]
    profit = []

    for price in prices:
        if price < lowest_price:
            lowest_price = price

        profit.append(price - lowest_price)
    return max(profit)

prices = [7,1,5,3,6,4]
maxP = maxProfit(prices)
print(maxP)