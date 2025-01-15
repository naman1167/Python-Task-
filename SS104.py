def longest_common_subsequence(str1, str2):
    """
    Find the longest common subsequence between two strings.
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    Returns: (LCS string, length, dp table)
    """
    if not str1 or not str2:
        return "", 0, None
    
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    comparisons = 0
    
    print("\nFinding Longest Common Subsequence:")
    print(f"String 1: {str1}")
    print(f"String 2: {str2}")
    
    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            comparisons += 1
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                print(f"\nMatch found at positions {i-1} and {j-1}:")
                print(f"Character: {str1[i-1]}")
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                print(f"\nNo match at positions {i-1} and {j-1}:")
                print(f"Characters: {str1[i-1]} ≠ {str2[j-1]}")
            
            print_dp_state(dp, str1, str2, i, j)
    
    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    
    print("\nReconstructing the LCS:")
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
            print(f"Including character: {str1[i]}")
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
            print(f"Moving up (i = {i})")
        else:
            j -= 1
            print(f"Moving left (j = {j})")
        print_reconstruction_state(str1, str2, i, j, lcs)
    
    return ''.join(reversed(lcs)), dp[m][n], dp, comparisons

def print_dp_state(dp, str1, str2, current_i, current_j):
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

def print_reconstruction_state(str1, str2, pos1, pos2, current_lcs):
    """Print current state of LCS reconstruction."""
    def print_string_with_highlight(s, pos):
        for i in range(len(s)):
            if i == pos-1:
                print(f"[{s[i]}]", end="")
            else:
                print(s[i], end="")
        print()
    
    print("\nCurrent state:")
    print("String 1: ", end="")
    print_string_with_highlight(str1, pos1)
    print("String 2: ", end="")
    print_string_with_highlight(str2, pos2)
    print(f"Current LCS: {''.join(reversed(current_lcs))}")

def main():
    """Test longest common subsequence implementation."""
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
        lcs, length, dp, comparisons = longest_common_subsequence(str1, str2)
        end_time = time.time()
        
        # Print results
        print("\nAnalysis completed!")
        print(f"Comparisons made: {comparisons}")
        print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
        
        if length > 0:
            print(f"\nLongest Common Subsequence: '{lcs}'")
            print(f"Length: {length}")
            
            # Show how LCS appears in both strings
            print("\nLCS visualization:")
            def highlight_subsequence(s, subseq):
                result = []
                j = 0
                for i in range(len(s)):
                    if j < len(subseq) and s[i] == subseq[j]:
                        result.append(f"[{s[i]}]")
                        j += 1
                    else:
                        result.append(s[i])
                return ''.join(result)
            
            print(f"String 1: {highlight_subsequence(str1, lcs)}")
            print(f"String 2: {highlight_subsequence(str2, lcs)}")
        else:
            print("\nNo common subsequence found!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
