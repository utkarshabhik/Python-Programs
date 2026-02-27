def factorial_digits(n):
    result = [1]  # stores digits in reverse order
    
    for x in range(2, n + 1):
        carry = 0
        
        for i in range(len(result)):
            product = result[i] * x + carry
            result[i] = product % 10
            carry = product // 10
        
        while carry:
            result.append(carry % 10)
            carry //= 10
    
    return result[::-1]  # reverse to get correct order


# Example usage
n = 5
print(factorial_digits(n))
