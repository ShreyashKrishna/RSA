import math
import random
def Extended(a,b):
    a0=a
    b0=b
    t0=0
    t1=1
    s0=1
    s=0
    q=math.floor(a0/b0)
    r=a0-q*b0
    while(r>0):
        temp=t0-(q*t1)
        t0=t1
        t1=temp
        temp=s0-(q*s)
        s0=s
        s=temp
        a0=b0
        b0=r
        q=math.floor(a0/b0)
        r=a0-(q*b0)
    r=b0;
    retval=[r,s,t1]
    
    return (s%b);
def primegenerator(n):
    count = 0;
    for i in range(0,20):
        x = rabinMiller(n);
        if (x == True):
            count = count + 1;
    if (count == 20):
        return n;
    else:
        return -1;
def isCoPrime(a,b):
    while b:
        a, b = b, a%b
    return a
def rabinMiller(num):
    # Returns True if num is a prime number.

    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True
def isPrime(num):
    # Return True if num is a prime number. This function does a quicker
    # prime number check before calling rabinMiller().

    if (num < 2):
        return False # 0, 1, and negative numbers are not prime

    # About 1/3 of the time we can quickly determine if num is not prime
    # by dividing by the first few dozen prime numbers. This is quicker
    # than rabinMiller(), but unlike rabinMiller() is not guaranteed to
    # prove that a number is prime.
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True

    # See if any of the low prime numbers can divide num
    for prime in lowPrimes:
        if (num % prime == 0):
            return False

    # If all else fails, call rabinMiller() to determine if num is a prime.
    return rabinMiller(num)


def generateLargePrime(keysize):
    # Return a random prime number of keysize bits in size.
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num

l=(int)(input("Enter a number:"))#ask for integer input
k=l/2
x=l/2
flag=True
while(flag):
    new=random.randint(2**(x-1),2**x);
    if (new%2==0):
        flag=True;
    else:
        prime=primegenerator(new);
        if(prime!=-1):
            p=new;
            flag=False;
flag1=True
while(flag1):
    new=random.randint(2**(x-1),2**x)
    if (new%2==0):
        flag1=True;
    else:
        prime=primegenerator(new);
        if(prime!=-1):
            q=new;
            flag1=False;
#p=generateLargePrime(k);
#q=generateLargePrime(k);
print(p)
n=p*q
phi=(p-1)*(q-1)
k=0
e=0
while k==0:
    e=random.randint(1,phi);
    i=isCoPrime(e,phi);
    if(i==1):
        k=k+1
inve=Extended(e,phi);
d=inve%phi
k=e*d
k=k%phi
print (k)
fo = open("PublicKey.txt", "a")
fo.write(str(e))
fo.write("\n")
fo.write(str(n))
fo.close()
f1=open("PrivateKey.txt","a")
f1.write(str((d)))
f1.write("\n")
f1.write(str((n)))
f1.close()
