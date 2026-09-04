def fibonacci(n):
    if n<=1:
        return n 
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=5
print(f"the {n}th fibonacci number is:{fibonacci(n)}")
