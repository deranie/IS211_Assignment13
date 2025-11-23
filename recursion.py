


# Part I – Fibonacci Sequence

def fibonacci(n):
    """
    Returns the nth Fibonacci number using recursion.
    Fibonacci sequence:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2)
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)



# Part II – Euclid's GCD Algorithm

def gcd(a, b):
    """
    Returns the greatest common divisor of a and b using recursion.
    Euclid's Algorithm:
        gcd(a, b) = gcd(b, a % b)
    Base case:
        when b == 0, gcd is a
    """
    if b == 0:
        return a
    return gcd(b, a % b)


# Part III – Recursive String Comparison

def compareTo(s1, s2):
    """
    Recursively compares two strings.
    Returns:
        negative number if s1 < s2
        0 if s1 == s2
        positive number if s1 > s2
    """

    # Base case:
    if s1 == "" and s2 == "":
        return 0

    # If first characters differ or one string is empty
    if s1 == "" and s2 != "":
        return -1
    if s1 != "" and s2 == "":
        return 1
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])

    # Characters equal → recurse on the rest
    return compareTo(s1[1:], s2[1:])


# Optional Testing / Debug

if __name__ == "__main__":
    print("Fibonacci(10):", fibonacci(10))  # 55
    print("gcd(48, 18):", gcd(48, 18))      # 6
    print("compareTo('apple', 'apricot'):", compareTo("apple", "apricot"))
    print("compareTo('cat', 'cat'):", compareTo("cat", "cat"))
    print("compareTo('zoo', 'apple'):", compareTo("zoo", "apple"))
