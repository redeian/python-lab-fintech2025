
def print_mult_table(a, b):
    for i in range(a, b+1):
        for j in range(1, 13):
            if (i*j%2==0):
                print( f'{i} x {j} = {i*j}')