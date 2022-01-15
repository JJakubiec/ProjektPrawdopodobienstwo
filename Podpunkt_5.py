from numpy import *
from scipy.stats import norm


def solve_CLT_task(constraints):
    x = (constraints[0]-k*mean(range(1, 7)))/(std(range(1, 7))*sqrt(k))
    if x < 0:
        x = 1 - norm.cdf(-x)
    if constraints[1] == ">" or constraints == ">=":
        return 1 - x

    return x


k = 7
print(solve_CLT_task([12, "<"]))
