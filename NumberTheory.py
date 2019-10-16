def fastpow(a, p, m):
	if a==0:
		return 1
	t=fastpow(a,p//2)
	return t*t*(a if a%2 else 1)

def xgcd(a,b):
	if b==0:
		return (1,0,abs(a))
	x,y,g=xgcd(b,a%b)
	return (y,x-(a//b)*y,g);

def adjust_xgcd_lb(x,y,g,a,b,lbx,lby):
	if x<lbx:
		t=0
		if b>=0:
			t=(lbx-x)*g//b + int((lbx-x)*g%b!=0)
		else:
			t=(lbx-x)*g//b
		x+=t*b//g;
		y-=t*a//g;
	if y<lby:
		t=0
		if a>=0:
			t=(lby-y)*g//a + int((lby-y)*g%a!=0)
		else:
			t=(lby-y)*g//a
		x-=t*b//g;
		y+=t*a//g;
	#if x<lbx or y<lby:
	#	raise Exception;
	return (x,y);


# XGCD XGCDtoub(XGCD a, i64 ubx, i64 uby){
# 	if(0)
# 		throw "no root";
# 	return {};
# 	//return maximum a which satisfies a<ub
# }

def is_prime(n):
	if n<2:
		return False
	for i in range(n):
		if i*i>n:
			break
		if n%i==0:
			return False
	return True

def miller_rabin(n):
	return True

def factorize(n):
	x=n
	ret=[]
	for i in range(n):
		if i*i>n:
			break
		while x%i==0:
			x//=i
			ret.append(i)
	if x>1:
		ret.append(x)
	return ret

# Arr<i64> divisors(i64 n){
# 	Arr<i64> ret, tmp;
# 	for(i64 i=1; i*i<=n; i++){
# 		if (n%i==0){
# 			ret.pushb(i);
# 			if (i!=n/i)
# 				tmp.pushb(n/i);
# 		}
# 	}
# 	reverse(all(tmp));
# 	ret.insert(ret.end(), all(tmp));
# 	return ret;
# }

# //nloglog(n)
# Arr<bool> sieve_prime(int ub){
# 	Arr<bool> ret(ub, true);
# 	ret[0]=ret[1]=false;
# 	for (i64 i=2; i*i<ub; i++) {
# 		if (!ret[i])
# 			continue;
# 		for (i64 j=i*i; j<ub; j+=i)
# 			ret[j]=false;
# 	}
# 	return ret;
# }

# //nlogn (harmony series)
# //can apply to calculate (low constant factor)sieve_numdiv, sieve_sumdiv, etc.
# Arr<Arr<int>> sieve_divs(int ub){
# 	Arr<Arr<int>> ret(ub);
# 	for (i64 i=1; i<ub; i++) {
# 		for (i64 j=i; j<ub; j+=i)
# 			ret[j].pushb(i);
# 	}
# 	return ret;
# }

# int eulerphi(int n){return 0;}

# //floor(log(n))
# int lgf(i64 n, int base=2){
# 	int ret=0;
# 	while (n)
# 		n/=base, ret++;
# 	return ret-1;
# }

# //ceil(log(n))
# int lgc(i64 n, int base=2) {
# 	int ret=0;
# 	int rem=0;
# 	while (n)
# 		rem+=n%base, n/=base, ret++;
# 	return ret-(rem<=1);
# }

# int sqrt_f(i64 n){
# 	i64 i=1;
# 	while(i*i<=n)
# 		i++;
# 	return i-1;
# }

# int sqrt_c(i64 n){
# 	i64 i=1;
# 	while(i*i<n)
# 		i++;
# 	return i;
# }

# template<typename T>
# Arr<T> factorials(T n){
# 	Arr<T> ret(int(n)+1);
# 	ret[0]=1;
# 	cfor(i, 1, n)
# 		ret[i]=ret[i-1]*i;
# 	return ret;
# }

# //recommanded T=ModNum. i64 can easily overflow.
# template<typename T>
# T binom(T n, T k){
# 	if(k>n/2)
# 		return binom(n, n-k);
# 	if(k==0)
# 		return 1;
# 	auto f=factorials(n);
# 	return f[int(n)]/(f[int(k)]*f[int(n-k)]);
# }

# template<typename T>
# Arr<Arr<T>> binom_dp(T n, T k){
# 	Arr<Arr<T>> ret(n, Arr<T>(k));

# 	return ret;
# }

# Arr<int> to_digits(i64 n){
# 	Arr<int> ret;
# 	while(n)
# 		ret.pushb(n%10), n/=10;
# 	return ret;
# }
