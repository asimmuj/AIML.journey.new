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