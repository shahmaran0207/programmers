# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution(money):
	coin = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
	counter = 0
	idx = len(coin) - 1
	while money:
		counter += 1
		money %= coin[idx]
		idx -= 1
	return counter-1

solution(2200)