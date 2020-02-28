import sys
sys.setrecursionlimit(1000000)
from math import gcd
from NumberTheory import *
import gc; gc.disable()
n,x=map(int,input().split());
xgcd

n,p,w,d=map(int,input().split())
x,y,g=xgcd(w,d)

if p%g:
  print(-1)
  exit(0)
x*=p//g
y*=p//g

x,y=adjust_xgcd_lb(x,y,g,w,d,0,0)
if n-(x+y)<0:
  t=(n-(x+y))*g//(d-w) + int((n-(x+y))*g%(d-w)!=0)
  x+=t*d//g
  y-=t*w//g
if x<0 or y<0 or n-x-y<0:
	print(-1)
else:
	print( x,y,n-x-y)
