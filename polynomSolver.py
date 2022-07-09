from math import log

eps = 1e-10

def deriv_coeffs(degree, coeffs):
    return [ elem*(degree-index) for index, elem in enumerate(coeffs[:-1]) ]

def eval_polynom(degree, coeffs, x):
    return sum([ coef * x**(degree-index) for index, coef in enumerate(coeffs) ])

def get_upper_bound(degree,coeffs):
    k = -1
    for i in range(degree+1):
        if coeffs[i]/coeffs[0] < 0:
            k = i
            break
    if k == -1: return 1
    return 1 + (max([abs(i) for i in coeffs if i < 0])/coeffs[0])**(1/k)
    
def solve_polynom(degree: int, coeffs: list):
    rootsBounds = [] # [a, b, c] -> x1 in [a; b], x2 in [b; c]

    if degree == 1:
        if coeffs[0] == 0:
            return []
        return [-coeffs[1]/coeffs[0]]
    
    negativeCoeffs = coeffs.copy()
    for i in range(1 - degree%2, degree, 2):
        negativeCoeffs[i] *= -1
    if negativeCoeffs[0] < 0:
        negativeCoeffs = [negativeCoeffs[i]*(-1) for i in range(degree+1)]
    
    bottomBound = -get_upper_bound(degree, negativeCoeffs)
    rootsBounds.append(bottomBound)
    
    rootsBounds += solve_polynom(degree-1, deriv_coeffs(degree, coeffs))
    
    upperBound = get_upper_bound(degree, coeffs)
    rootsBounds.append(upperBound)

    f = lambda x: eval_polynom(degree, coeffs, x)
    roots = []
    
    for i in range(len(rootsBounds)-1):
        l, r = rootsBounds[i:i+2]

        if f(l)*f(r) > 0:
            continue
        
        # Signs of f(l) and f(r) are different
        #y ↑ f(l) _  
        #  |    |  \
        #  |----l---\----r-→ x
        #  |         \   |
        #  |          -- f(r)
        
        while r - l > eps:
            mid = (r+l)/2
            if f(mid) == 0:
                l = mid
                break
            elif f(mid) < 0:
                if f(l) < f(r): l = mid
                else: r = mid
            else: # f(mid) > 0
                if f(l) < f(r): r = mid
                else: l = mid
        roots.append(l)

    return roots

if __name__ == '__main__':
    deg = int(input("Enter degree: "))
    coeffs = [float(i) for i in input("Enter coefficients: ").split()]

    accuracy = round(-log(eps, 10)) - 2
    solutions = [round(i, accuracy) for i in solve_polynom(deg, coeffs)]
    answer = sorted(set(solutions))

    print("Solutions: ")
    for ind, item in enumerate(answer):
        print(f'{ind+1}) {item}')
    
