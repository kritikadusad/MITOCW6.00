# 6.00 Problem Set 2
#
# Successive Approximation
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    value_of_poly = 0
    for i in range(0, len(poly)):
        var = x
        power = i
        coeff = poly[i]
        value_of_poly += (coeff * (var**power))
    return value_of_poly

def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    derivative_of_poly = []
    for i in range(1, len(poly)):
        power = i
        coeff = poly[i]
        y = float(coeff * power)
        first = derivative_of_poly.append(y)
    return derivative_of_poly

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    guess = 0
    while True:
        poly_value = evaluate_poly(poly, x_0)
        if -epsilon < poly_value < epsilon:
            guess += 1
            return x_0, guess
        else:
            poly_derivative = compute_deriv(poly)
            deriv_value = evaluate_poly(poly_derivative, x_0)
            x_0 = x_0 - poly_value / deriv_value
            guess += 1
            


    
        

# poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
# z = compute_deriv(poly)
# tuple_z = tuple(z)
# print 'The derivative of polynomial is:', tuple_z

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = 0.1
epsilon = .0001
r = compute_root(poly, x_0, epsilon)
print 'The root of the polynomial is:', r 


    # TO DO ... 

