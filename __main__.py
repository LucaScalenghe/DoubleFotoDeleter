import sys
import os
from pathlib import  Path

#importtant reference 
# https://www.decodingdevops.com/python-os-walk-recursive-examples/#Python_os_walk()_Example3_with_Recursive


# while len(sys.argv) > 1 and len(sys.argv)<3 and not os.path.exists(sys.argv[1]) :
#     print("Insert ONE valid path to start")

# path_as_string= sys.argv[1]
# path = Path (p)

path = Path( r'C:\Users\lucas\Desktop\Foto' )


for root, dirs, files in os.walk(str(path)):
        for i in files:
         print(i)
    













