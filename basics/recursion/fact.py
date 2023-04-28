def dfact(n):
    if n==1:
     
      return n
    
    return (n * fact(n-1))
if "__name__" == "__main__":
      
    print(dfact(10)) 
