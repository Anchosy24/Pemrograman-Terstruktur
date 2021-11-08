def faktorial(x):
    if(x <= 1):
       return 1
    else:
       f = x * faktorial(x-1)
       return f
