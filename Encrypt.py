def squareAndmultiply(k,c,n):
    bin_e=bin(c)[2:]
    c1=[]
    for bit in bin_e:
        c1.append(int(bit));
    c1.reverse()
    l=len(bin(c)[2:])
    z=1    
    for i in range(l-1,-1,-1):
        z=(z*z)%n
        if c1[i]==1:
            z=(z*k)%n    
    return z
f1=open("C:\\Python34\\PublicKey.txt","r")
st1=f1.readline()
st2=f1.readline()
f1.close()
k=(int)(input("Enter the text to be encrypted of size n:"))
e=int(float(st1))
n=int(float(st2))
ret_z=squareAndmultiply(k,e,n)
f2=open("C:\\Python34\\SecretKey.txt","a")
f2.write(str(ret_z))
f2.close()
