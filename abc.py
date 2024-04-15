from z3 import *

# Define variables
x = Int('x')
y = Int('y')
z = Int('z')

# Create solver
solver = Solver()

# Add constraints
solver.add(x*x + z == 16)
solver.add(y*y*y == 27)
solver.add(x*y == 6)

# Check satisfiability
print(solver.check())

result = solver.model()
print(result)
