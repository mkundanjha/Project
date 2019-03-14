
n=int(input("Enter nummber\n"))
def isPrime(num):
    for i in range(2,num//2):
        if(num%i==0):
            return False
    return True

def isSemiPrime(num):
    for i in range(num):
        for j in range(num):
            if i!=j and (isPrime(i) and isPrime(j)) and i*j==num:
                return True
    return False

def isSum(num):
    for i in range(num):
        for j in range(num):
            if (isSemiPrime(i) and isSemiPrime(j)) and i+j==num:
                return True
    return False

print(isSum(n))

     
    
        
       
    

