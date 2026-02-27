def minimum_swaps(s1: str, s2: str) -> int:
    # If lengths are different, it is impossible to make them equal
    if len(s1) != len(s2):
        return -1

    # xy → count of positions where s1 has '0' and s2 has '1'
    # yx → count of positions where s1 has '1' and s2 has '0'
    xy = 0
    yx = 0

    # Traverse both strings
    for i in range(len(s1)):
        # Check if characters at same index are different
        if s1[i] != s2[i]:

            # Case 1: s1 = '0' and s2 = '1'
            if s1[i] == '0' and s2[i] == '1':
                xy += 1

            # Case 2: s1 = '1' and s2 = '0'
            elif s1[i] == '1' and s2[i] == '0':
                yx += 1

    # If total mismatches are odd, we cannot fix them using swaps
    if (xy + yx) % 2 != 0:
        return -1

    # Minimum swaps calculation:
    # Every two xy mismatches need 1 swap
    # Every two yx mismatches need 1 swap
    # If one xy and one yx remain, they need 2 swaps
    swaps = (xy // 2) + (yx // 2) + 2 * (xy % 2)

    # Return total swaps required
    return swaps


# -------------------------
# Driver Code
# -------------------------

if __name__ == "__main__":
    # Taking input from user
    s1 = input("Enter first binary string: ")
    s2 = input("Enter second binary string: ")

    # Calling function
    result = minimum_swaps(s1, s2)

    # Printing result
    print("Minimum swaps required:", result)
