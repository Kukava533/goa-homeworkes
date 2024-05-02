def paperwork(n, m):
    if n<0 or m<0:
        return 0
    else:
        return n*m
    def count_by(x, n):
    multiples_x = []
    
    for i in range(x, x * n + 1):
        if i % x == 0:
            multiples_x.append(i)
    
    return multiples_x