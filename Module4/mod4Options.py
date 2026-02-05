#f = open('file.dat', rb)
#f.close()

### Option 1 ###
from Module4 import module4
module4.print_hello()

### option 2 #####
from Module4 import module4 as m4

m4.print_hello()

### Option 3 #####
from Module4.module4 import print_hello

print_hello

def o4():
    ### Option 4 ####
    from Module4.module4 import print_hello as phello
    from Module4.mod4_class import MyClass as mclass
    