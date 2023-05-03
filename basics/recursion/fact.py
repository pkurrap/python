def dfact(n):
    if n==0:
       return 1
    else:
       return (n * dfact(n-1))
if "__name__" == "__main__":
print(dfact(10)) 
