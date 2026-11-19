import sympy as sp
x=sp.symbols('x')
f=input("enter an expression to differentiate: ")
function = sp.sympify(f)
derivative=sp.diff(function,x)
value=int(input("enter a value: "))
differentiation=derivative.subs(x,value)
print("derivative at value: ",differentiation)