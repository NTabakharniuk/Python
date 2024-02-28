import math

def main (a, b, x):
    Z = math.sqrt(x**4+a*x+b)/math.sqrt(x**4+a*x+b)
    print(Z)

main(2,4,3)