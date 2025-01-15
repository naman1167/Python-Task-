def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two strings.
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    Returns: (longest substring, length, start positions in both strings)
    """
    if not str1 or not str2:
        return "", 0, (-1, -1)
    
    m, n = len(str1), len(str2)
    # dp[i][j] represents length of LCS ending at i-1 and j-1
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to keep track of maximum length substring
    max_length = 0
    end_pos = 0  # End position in str1
    comparisons = 0
    
    print("\nFinding Longest Common Substring:")
    print(f"String 1: {str1}")
    print(f"String 2: {str2}")
    
    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            comparisons += 1
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_pos = i
                
                print(f"\nMatch found at positions {i-1} and {j-1}:")
                print(f"Character: {str1[i-1]}")
                print_comparison_state(str1, str2, i-1, j-1, 
                                    end_pos-max_length, end_pos)
            
            print_dp_table(dp, str1, str2, i, j)
    
    # Extract the longest common substring
    start_pos = end_pos - max_length
    lcs = str1[start_pos:end_pos]
    
    # Find start position in str2
    str2_start = -1
    for i in range(n - max_length + 1):
        if str2[i:i+max_length] == lcs:
            str2_start = i
            break
    
    return lcs, max_length, (start_pos, str2_start), comparisons

def print_comparison_state(str1, str2, pos1, pos2, start, end):
    """Print current state of comparison with highlighting."""
    def print_string_with_highlight(s, current_pos, start=None, end=None):
        for i in range(len(s)):
            if start is not None and start <= i < end:
                print(f"[{s[i]}]", end="")
            elif i == current_pos:
                print(f"({s[i]})", end="")
            else:
                print(s[i], end="")
        print()
    
    print("\nCurrent state:")
    print("String 1: ", end="")
    print_string_with_highlight(str1, pos1, start, end)
    print("String 2: ", end="")
    print_string_with_highlight(str2, pos2)

def print_dp_table(dp, str1, str2, current_i, current_j):
    """Print current state of dynamic programming table."""
    print("\nDP Table:")
    # Print header
    print("    ", end="")
    print("  ε", end="")
    for c in str2:
        print(f"  {c}", end="")
    print()
    
    # Print rows
    for i in range(len(dp)):
        if i == 0:
            print("ε ", end="")
        else:
            print(f"{str1[i-1]} ", end="")
        
        for j in range(len(dp[0])):
            if i == current_i and j == current_j:
                print(f"[{dp[i][j]}]", end="")
            else:
                print(f" {dp[i][j]} ", end="")
        print()

def main():
    """Test longest common substring implementation."""
    try:
        # Get input strings
        str1 = input("Enter first string: ")
        str2 = input("Enter second string: ")
        
        if not str1 or not str2:
            print("Strings cannot be empty!")
            return
        
        # Find LCS and measure time
        import time
        start_time = time.time()
        lcs, length, (pos1, pos2), comparisons = longest_common_substring(str1, str2)
        end_time = time.time()
        
        # Print results
        print("\nAnalysis completed!")
        print(f"Comparisons made: {comparisons}")
        print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
        
        if length > 0:
            print(f"\nLongest Common Substring: '{lcs}'")
            print(f"Length: {length}")
            print(f"Position in first string: {pos1}")
            print(f"Position in second string: {pos2}")
            
            # Visualize result
            print("\nVisualization:")
            print(f"String 1: {str1}")
            print("          " + " " * pos1 + "^" * length)
            print(f"String 2: {str2}")
            print("          " + " " * pos2 + "^" * length)
        else:
            print("\nNo common substring found!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
