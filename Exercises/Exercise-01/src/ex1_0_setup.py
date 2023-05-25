import sys
import pip

print(f"Python version: {sys.version}")
print(f"Pip: {pip.main(['list'])}")