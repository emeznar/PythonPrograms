def mySqrt(n):
    almost = 0.5 * n
    better = 0.5 * (almost + n/almost)
    
    return almost


print("Final approx:", mySqrt(4))


