def knapsack_01(values, weights, capacity):
    """
    Solve 0/1 Knapsack problem using dynamic programming.
    Time Complexity: O(n * capacity)
    Space Complexity: O(n * capacity)
    """
    n = len(values)
    if n == 0 or capacity <= 0:
        return 0, [], None, 0
    
    # dp[i][w] represents max value for first i items with capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    # To track selected items
    selected = [[False for _ in range(capacity + 1)] for _ in range(n + 1)]
    operations = 0
    
    print("\nSolving 0/1 Knapsack Problem:")
    print(f"Capacity: {capacity}")
    print("Items (value, weight):")
    for i in range(n):
        print(f"Item {i+1}: ({values[i]}, {weights[i]})")
    
    # Fill dp table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            operations += 1
            
            # Don't include item i
            dp[i][w] = dp[i-1][w]
            
            # Try including item i if possible
            if weights[i-1] <= w:
                val = dp[i-1][w-weights[i-1]] + values[i-1]
                if val > dp[i][w]:
                    dp[i][w] = val
                    selected[i][w] = True
            
            print(f"\nConsidering item {i} with capacity {w}:")
            print_dp_state(dp, selected, i, w, values, weights)
    
    # Reconstruct solution
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if selected[i][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    
    return dp[n][capacity], selected_items, dp, operations

def print_dp_state(dp, selected, current_item, current_weight, values, weights):
    """Print current state of dynamic programming table."""
    print("\nDP Table (maximum value for items 1..i and capacity w):")
    # Print header
    print("     w→", end="")
    for w in range(len(dp[0])):
        print(f"{w:4}", end="")
    print("\ni↓")
    
    # Print rows
    for i in range(len(dp)):
        if i == 0:
            print(f"0   ", end="")
        else:
            print(f"{i}({values[i-1]},{weights[i-1]}) ", end="")
        
        for w in range(len(dp[0])):
            if i == current_item and w == current_weight:
                print(f"[{dp[i][w]:2}]", end="")
            else:
                print(f" {dp[i][w]:2} ", end="")
        print()

def analyze_solution(selected_items, values, weights, capacity):
    """Analyze the knapsack solution."""
    if not selected_items:
        return
    
    print("\nSolution Analysis:")
    total_value = sum(values[i] for i in selected_items)
    total_weight = sum(weights[i] for i in selected_items)
    
    print("Selected items:")
    for i in selected_items:
        print(f"Item {i+1}: value = {values[i]}, weight = {weights[i]}")
    
    print(f"\nTotal value: {total_value}")
    print(f"Total weight: {total_weight}/{capacity}")
    
    # Calculate efficiency
    efficiency = total_value / total_weight if total_weight > 0 else 0
    print(f"Value per unit weight: {efficiency:.2f}")

def get_user_input():
    """Get items and capacity from user."""
    try:
        n = int(input("Enter number of items: "))
        if n <= 0:
            print("Number of items must be positive!")
            return None, None, 0
        
        values = []
        weights = []
        print("\nEnter item details:")
        for i in range(n):
            value = int(input(f"Enter value for item {i+1}: "))
            weight = int(input(f"Enter weight for item {i+1}: "))
            
            if value < 0 or weight <= 0:
                print("Values must be non-negative and weights must be positive!")
                return None, None, 0
            
            values.append(value)
            weights.append(weight)
        
        capacity = int(input("\nEnter knapsack capacity: "))
        if capacity <= 0:
            print("Capacity must be positive!")
            return None, None, 0
        
        return values, weights, capacity
    
    except ValueError:
        print("Please enter valid numbers!")
        return None, None, 0

def main():
    """Test 0/1 knapsack implementation."""
    # Get input
    values, weights, capacity = get_user_input()
    if values is None:
        return
    
    # Solve knapsack and measure time
    import time
    start_time = time.time()
    max_value, selected_items, dp, operations = knapsack_01(values, weights, capacity)
    end_time = time.time()
    
    # Print results
    print("\nAnalysis completed!")
    print(f"Operations performed: {operations}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
    
    print(f"\nMaximum value possible: {max_value}")
    analyze_solution(selected_items, values, weights, capacity)

if __name__ == "__main__":
    main()
