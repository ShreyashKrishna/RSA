def squareAndmultiply(k,d,n):
    bin_e=bin(d)[2:]
    c1=[]
    for bit in bin_e:
        c1.append(int(bit));
    c1.reverse()
    l=len(bin(d)[2:])
    z=1    
    for i in range(l-1,-1,-1):
        z=(z*z)%n
        if c1[i]==1:
            z=(z*k)%n    
    return z
f1=open("C:\\Python34\\PrivateKey.txt","r")
st1=f1.readline()
st2=f1.readline()
f1.close()
f2=open("C:\\Python34\\Secretkey.txt","r")
st3=f2.readline()
f2.close()
d=int(float(st1))
n=int(float(st2))
k=int(float(st3))
ret_z=squareAndmultiply(k,d,n)
print (ret_z)
