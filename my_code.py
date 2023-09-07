def power(x, y):
    """Exponent function

    Args:
        x (int): Any positive integer
        y (int): Any positive integer
    """
    rv = x # rv = return value
    for i in range(y):
        rv = rv * x
    return(rv)