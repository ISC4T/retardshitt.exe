from sympy import symbols, Eq, solve

x, y = symbols('x y')
expr = 2*x + y
expr.subs(x, 2)
expr