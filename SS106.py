def coin_change_dp(coins, amount):
    """
    Find minimum coins needed for amount using dynamic programming.
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    if amount == 0:
        return [], 0, None, 0
    
    if not coins or amount < 0:
        return None, float('inf'), None, 0
    
    # dp[i] represents minimum coins needed for amount i
    dp = [float('inf')] * (amount + 1)
    # To reconstruct the solution
    prev = [-1] * (amount + 1)
    operations = 0
    
    dp[0] = 0
    
    print("\nSolving Coin Change Problem (Dynamic Programming):")
    print(f"Amount: {amount}")
    print(f"Available coins: {coins}")
    
    # Fill dp table
    for i in range(1, amount + 1):
        for coin in coins:
            operations += 1
            if coin <= i and dp[i - coin] != float('inf'):
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    prev[i] = i - coin
                    
                    print(f"\nUpdating solution for amount {i}:")
                    print(f"Using coin: {coin}")
                    print_dp_state(dp, i, coin)
    
    # Reconstruct solution
    if dp[amount] == float('inf'):
        return None, float('inf'), dp, operations
    
    # Get coins used
    coins_used = []
    current = amount
    while current > 0:
        coin = current - prev[current]
        coins_used.append(coin)
        current = prev[current]
    
    return coins_used, dp[amount], dp, operations

def print_dp_state(dp, current_amount, current_coin):
    """Print current state of dynamic programming table."""
    print("\nDP Table (minimum coins needed for each amount):")
    for i in range(len(dp)):
        if i == current_amount:
            print(f"[{i:2}]: ", end="")
        else:
            print(f" {i:2} : ", end="")
        
        if dp[i] == float('inf'):
            print("∞")
        else:
            print(dp[i])
    
    # Visual representation of current state
    print("\nProgress:")
    progress = (current_amount + 1) / len(dp) * 50  # 50 characters for progress bar
    print("[" + "=" * int(progress) + ">" + " " * (50 - int(progress)) + "]")
    print(f"{((current_amount + 1)/len(dp))*100:.1f}%")

def analyze_solution(coins_used, amount, dp):
    """Analyze the solution."""
    if not coins_used:
        return
    
    print("\nSolution Analysis:")
    # Count frequency of each coin
    from collections import Counter
    freq = Counter(coins_used)
    
    print("Coin breakdown:")
    for coin, count in sorted(freq.items(), reverse=True):
        print(f"${coin}: {count} coins = ${coin * count}")
    
    print(f"\nTotal coins used: {len(coins_used)}")
    print(f"Total amount: ${sum(coins_used)}")
    
    # Show subproblem solutions
    print("\nSubproblem solutions:")
    for i in range(amount + 1):
        if dp[i] != float('inf'):
            print(f"Amount ${i}: {dp[i]} coins")

def get_user_input():
    """Get coins and amount from user."""
    try:
        coins_input = input("Enter available coin denominations (space-separated): ")
        coins = sorted([int(x) for x in coins_input.split()])
        
        if not coins:
            print("No coins provided!")
            return None, 0
        
        if any(coin <= 0 for coin in coins):
            print("Coin values must be positive!")
            return None, 0
        
        amount = int(input("Enter target amount: "))
        if amount < 0:
            print("Amount must be non-negative!")
            return None, 0
        
        return coins, amount
    
    except ValueError:
        print("Please enter valid numbers!")
        return None, 0

def main():
    """Test coin change dynamic programming implementation."""
    # Get input
    coins, amount = get_user_input()
    if coins is None:
        return
    
    print(f"\nSolving for amount ${amount}")
    print(f"Available coins: {coins}")
    
    # Find solution and measure time
    import time
    start_time = time.time()
    result, min_coins, dp, operations = coin_change_dp(coins, amount)
    end_time = time.time()
    
    # Print results
    print("\nAnalysis completed!")
    print(f"Operations performed: {operations}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
    
    if result:
        print("\nOptimal solution found!")
        print(f"Minimum coins needed: {min_coins}")
        print(f"Coins used: {result}")
        analyze_solution(result, amount, dp)
    else:
        print("\nNo solution exists!")
        print("The amount cannot be made exactly with given coins")

if __name__ == "__main__":
    main()
