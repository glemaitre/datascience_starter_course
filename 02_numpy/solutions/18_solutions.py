def trapz_fast(y, x):
    area = (y[1:] - y[:-1]) * (x[1:] + x[:-1])
    return area.sum() / 2
