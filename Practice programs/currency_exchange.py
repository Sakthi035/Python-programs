def mincoin(coins , amount):
    coins.sort(reverse = True)
    mincoin = 0
    coinr =[]

    for coin in coins:
        while coin <= amount:
            amount -= coin
            mincoin += 1
            coinr.append(coin)
    #coinr.append(coins[len(coins)-1])
    return mincoin, coinr

coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]
amount = 1246
print(mincoin(coins, amount))