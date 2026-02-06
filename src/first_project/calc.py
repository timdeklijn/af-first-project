import numpy as np


def do_calc(num: int, fac: int) -> int:
    a = np.full((10, 10), num)
    return np.concatenate(a * fac).sum()
