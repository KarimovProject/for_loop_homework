def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    s = 0
    x = list(range(A,B))
    for i in x:
        s += i
    return s

print(main(-5,10))