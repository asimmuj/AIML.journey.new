#exercise 1
import sympy as sp
x,y=sp.symbols('x y')
f=x**2+y**2
dx=sp.diff(f,x)
dy=sp.diff(f,y)
print(dx)
print(dy)

#exercise 2
import sympy as sp
x,y=sp.symbols('x y')
f=5*x+7*y
dx=sp.diff(f,x)
dy=sp.diff(f,y)
print(dx)
print(dy)

#exercise 3
import sympy as sp
x,y=sp.symbols('x y')
f=x**2+4*x*y+2*y**2
dx=sp.diff(f,x)
valuex=dx.subs(x,2)
dy=sp.diff(f,y)
valuey=dy.subs(y,1)
print(valuex)
print(valuey)

#exercise 4
import sympy as sp
x,y,z=sp.symbols('x y z')
f=x**2+y**2+z**2+3*x*y
dx=sp.diff(f,x)
dy=sp.diff(f,y)
dz=sp.diff(f,z)
print(dx)
print(dy)
print(dz)