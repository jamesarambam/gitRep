"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Author : James Arambam
Date   : 03 Feb 2017
Description :
Input : 
Output : 

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

# ================================ priImports ================================ #

import sys
import os
import platform
from pprint import pprint

# ================================ secImports ================================ #

o = platform.system()
if o == "Linux":
    d = platform.dist()
    if d[0] == "debian":
        sys.path.append("/media/james/Storage/PyCharmProjects/auxLib")
    if d[0] == "centos":
        sys.path.append("/home/ajsingh/PycharmProjects/auxLib")
if o == "Darwin":
    sys.path.append("/Users/james/PycharmProjects/auxLib")

import auxLib as ax

print "# ============================ START ============================ #"

# ============================================================================ #

# --------------------- Variables ------------------------------ #

ppath = os.getcwd() + "/"  # Project Path Location


# -------------------------------------------------------------- #

def main():


    print "Hello World"


# =============================================================================== #

if __name__ == '__main__':
    main()
    print "# ============================  END  ============================ #"

