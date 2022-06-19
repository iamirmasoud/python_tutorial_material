import sys

print(dir())
from mod1 import foo1
print(dir())

foo1()

import mod2
print(dir())

mod2.foo2()

print(sys.path)