def conv_mul(a,b):
	a=int(''.join(list(map(lambda x:('{:0'+str(M)+'b}').format(x), a))),2)
	b=int(''.join(list(map(lambda x:('{:0'+str(M)+'b}').format(x), b))),2)
	c=format(a*b,'b')[::-1]
	d=[]
	for i in range(0,len(c),M):
		d.append(int(c[i:min(i+M,len(c))][::-1],2))
	return d

M=30
n=int(input())
a=list(map(int,input().split()))[::-1]
b=list(map(int,input().split()))
a+=a
b+=[0]*len(b)
print(max(conv_mul(a,b)))
