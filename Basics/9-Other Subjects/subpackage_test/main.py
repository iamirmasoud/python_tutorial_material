import sys

print(dir())

import pkg.sub1.mod1

print(dir())

from pkg.sub2 import mod3

print(dir())

# pkg.sub1.mod1.foo1()

mod3.foo3()
# import pkg
# pkg.mod3.foo3()
#
# exit()
# import pkg.mod1
# pkg.mod1.foo1()
#
# from pkg.mod2 import foo2
# foo2()
#
# print(dir())
#
# print(sys.path)
#
# print(pkg.PKG_CONST)

# print(dir())
# from pkg import *
# print(dir())
# mod2.foo2()
