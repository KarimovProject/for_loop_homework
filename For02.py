def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    s = "0"
    for i in range(1, n):
        s += ","+str(i)
    return s


print(main(3))