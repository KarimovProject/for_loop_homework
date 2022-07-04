def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    s = price
    x = []
    for i in range(10):
        x.append(price)
        price += s
    return x

print(main(3.5))