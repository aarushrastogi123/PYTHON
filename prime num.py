def prime():
    a=int(input())
    b=int(input())
    for j in range (a,b):
        prime_num=True
        if j==1:
            continue
            #print(f'{n} is not a prime number.')
        for i in range(2,j):
            if (j%i==0):
                prime_num=False
                break
        if prime_num:
            print(j)
        j+=1    
prime()
