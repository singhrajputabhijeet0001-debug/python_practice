n=int(input("n: "))

for i in range(2,n):
    if(n%i)==0:
     print('number is not prime:', i)
     break
    else:
        print('number is prime')
