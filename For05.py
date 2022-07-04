def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    x = list(range(A, B+1))
    return x[::-1]

print(main(1,5))