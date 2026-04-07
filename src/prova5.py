def primer(n):
    for i in range(2, n):
        if n % i == 0:
            break
    if (i + 1)  == n:
        print(str(n) + "primer")
    else: 
        print(str(n) + " NO primer")
