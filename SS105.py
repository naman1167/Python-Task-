def coin_change_greedy(coins, amount):
    """
    Find minimum coins needed for amount using greedy approach.
    Note: This may not always give optimal solution!
    Time Complexity: O(n log n) for sorting + O(n) for selection
    Space Complexity: O(n) for result
    """
    if amount == 0:
        return [], 0, 0
    
    if not coins or amount < 0:
        return None, 0, 0
    
    # Sort coins in descending order
    coins = sorted(coins, reverse=True)
    result = []
    total = 0
    operations = 0
    
    print("\nSolving Coin Change Problem (Greedy Approach):")
    print(f"Amount: {amount}")
    print(f"Available coins: {coins}")
    
    for coin in coins:
        while total + coin <= amount:
            operations += 1
            result.append(coin)
            total += coin
            
            print(f"\nSelected coin: {coin}")
            print_current_state(result, total, amount)
            
            if total == amount:
                return result, len(result), operations
    
    if total != amount:
        return None, 0, operations
    
    return result, len(result), operations

def print_current_state(coins_used, current_sum, target):
    """Print current state of coin selection."""
    print("\nCurrent state:")
    print(f"Coins used: {coins_used}")
    print(f"Current sum: {current_sum}")
    print(f"Remaining: {target - current_sum}")
    
    # Visual representation
    print("\nProgress:")
    progress = current_sum / target * 50  # 50 characters for progress bar
    print("[" + "=" * int(progress) + ">" + " " * (50 - int(progress)) + "]")
    print(f"{(current_sum/target)*100:.1f}%")

def analyze_solution(coins_used, amount):
    """Analyze the solution for optimality."""
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
    
    # Calculate efficiency
    min_possible = amount // max(coins_used)
    efficiency = min_possible / len(coins_used) * 100
    print(f"Solution efficiency: {efficiency:.1f}%")
    
    if efficiency < 100:
        print("Note: This greedy solution might not be optimal!")

def get_user_input():
    """Get coins and amount from user."""
    try:
        coins_input = input("Enter available coin denominations (space-separated): ")
        coins = sorted([int(x) for x in coins_input.split()], reverse=True)
        
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
    """Test coin change greedy implementation."""
    # Get input
    coins, amount = get_user_input()
    if coins is None:
        return
    
    print(f"\nSolving for amount ${amount}")
    print(f"Available coins: {coins}")
    
    # Find solution and measure time
    import time
    start_time = time.time()
    result, num_coins, operations = coin_change_greedy(coins, amount)
    end_time = time.time()
    
    # Print results
    print("\nAnalysis completed!")
    print(f"Operations performed: {operations}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
    
    if result:
        print("\nSolution found!")
        print(f"Coins used: {result}")
        analyze_solution(result, amount)
    else:
        print("\nNo solution found!")
        print("This can happen if:")
        print("1. The amount cannot be made exactly with given coins")
        print("2. The greedy approach failed to find a solution")
        print("\nTry using dynamic programming for an optimal solution!")

if __name__ == "__main__":
    main()
