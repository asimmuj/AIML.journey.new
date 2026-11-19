import sympy as s
x=s.symbols('x')
f=x**4
derivative=s.diff(f,x)
print("derivative: ",derivative)

#exercise 2
import sympy as s
x=s.symbols('x')
f=7*x**3
derivative=s.diff(f,x)
print("derivative: ",derivative)

#exercise 3
import sympy as s
x=s.symbols('x')
f=5*x**3+4*x**2+6*x+9
derivative=s.diff(f,x)
print("derivative: ",derivative)

#exercise 4
import sympy as s
x=s.symbols('x')
f=x**3+2*x**2
derivative=s.diff(f,x)
print("derivative: ",derivative)
value=derivative.subs(x,2)
print("derivative at x=2: ",value)

#exercise 5
import sympy as sp
x-sp.symbols('x')
f=4*x**2+3*x+1
derivative=sp.diff(f,x)
print("derivative: ",derivative)
value=derivative.subs(x,2)
print("derivative at x=2: ", value)