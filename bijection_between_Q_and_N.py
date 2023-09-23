"""
Fausto David Hernández Jasso.
Reference: https://math.stackexchange.com/questions/7643/produce-an-explicit-bijection-between-rationals-and-naturals
"""

from fractions import Fraction

""" 
Stern's diatomic series
a_{1} = 1
a_{2k} = a_{k}
a_{2k+1} = a_{k} + a_{k + 1}
"""
def sterns_diatomic_series(k):
    if (k == 1):
        return 1
    elif (k % 2 == 0):
        return sterns_diatomic_series(k // 2)
    else:
        n = k // 2
        return sterns_diatomic_series(n) + sterns_diatomic_series(n + 1)


"""
N rational number.
f: N -> Q^{+}
This function is a bijection between N and Q^{+}.
You can see the proof on this site:
http://faculty.plattsburgh.edu/sam.northshield/08-0412.pdf
"""
def n_rational_number(n):
    return Fraction(sterns_diatomic_series(n), sterns_diatomic_series(n+1))


"""
Inverse function of n_rational_number.
f^{-1}: Q^{+} -> N
"""
def n_natural_number(q):
    if (q == 1):
        return 1
    elif (q < 1):
        return 2 * n_natural_number(Fraction(q, 1 - q))
    else:
        return 2 * n_natural_number(q - 1) + 1


"""
As we know, exists a bijection between Z and Q,
this a bijective function between those two sets.
f: Z -> Q
"""
def integers_to_rationals(z):
    if (z > 0):
        return Fraction(sterns_diatomic_series(z), sterns_diatomic_series(z + 1))
    elif (z < 0):
        return (-1) * Fraction(sterns_diatomic_series(-z), sterns_diatomic_series(-z + 1))
    else:
        return 0

"""
Bijection between Q and Z.
"""
def rational_to_integers(q):
    if (q > 1):
        return n_natural_number(q)
    elif (q == 1):
        return n_natural_number(q)
    elif (0 < q and q < 1):
        return n_natural_number(q)
    elif (q == 0):
        return 0
    elif (-1 < q and q < 0 ):
        return (-1) * (n_natural_number(-q))
    elif (q == - 1):
        return -1
    elif (q < -1): 
        return (-1) * (n_natural_number(-q) + 1)

"""
Bijection between Z and N.
"""
def integers_to_naturals(z):
    if (z > 0):
        return 2 * z
    elif (z == 0):
        return 0
    else:
        return (-2) * z - 1

"""
Bijection between Q and N.
"""
def rational_to_naturals(q):
    return integers_to_naturals(rational_to_integers(q))

"""
This function take two parameters, numerator and denominator
and returns a natural number which is the image in the bijection.
"""
def main():
    n = input("Numerator: ")
    d = input("Denominator: ")
    numerator = int(n)
    denominator = int(d)
    fraction = Fraction(numerator, denominator)
    print("Natural number: " + str(rational_to_naturals(fraction)))
    
    
    
if __name__ == "__main__":
    main()