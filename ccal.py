def get_min_coins(coins, target):
    # Base cases
    if target == 0:
        return 0
    if target < 0:
        return float('inf')
    
    min_coins = float('inf')
    
    # Recursively try every coin
    for coin in coins:
        result = get_min_coins(coins, target - coin)
        if result != float('inf'):
            min_coins = min(min_coins, result + 1)
            
    return min_coins

# Example Usage
coin_denominations = [1, 2, 5, 10, 20, 50, 100, 200]
target_amount = 63 

# Calculate the result
result = get_min_coins(coin_denominations, target_amount)
print(f"Minimum coins needed for {target_amount}: {result}")
