M=30
n=int(input())
a=list(map(int,input().split()))[::-1]
b=list(map(int,input().split()))
a+=a
b+=[0]*len(b)
t=list(map(lambda x:('{:0'+str(M)+'b}').format(x), a))
u=list(map(lambda x:('{:0'+str(M)+'b}').format(x), b))

a=int(''.join(t),2)
b=int(''.join(u),2)
c=format(a*b,'b')[::-1]
d=0
for i in range(0,len(c),M):
  d=max(d,int(c[i:min(i+M,len(c))][::-1],2))
print(d)
