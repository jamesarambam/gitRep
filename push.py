#!/usr/bin/python
"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Author : James Arambam
Date   : 08 Feb 2017
Description :
Input :
Output :


How to use :

$python push.py "message"

or

$python push.py


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

# ================================ priImports ================================ #

import sys
import os
import time


print "# ============================ STARTING GIT PUSH ============================ #"

# ============================================================================ #

# --------------------- Variables ------------------------------ #

ppath = os.getcwd() + "/"  # Project Path Location


# -------------------------------------------------------------- #

def main():

    s = str(time.strftime("%d/%m/%Y"))
    tmp = s.split("/")
    tmp[2] = tmp[2][2:4]
    version = reduce(lambda v1, v2 : v1+""+v2, tmp)
    version = "v"+version
    try:
        msg = sys.argv[1]

    except:
        msg = ""
        os.system("cd "+ppath)
    os.system("cd "+ppath +" && "+"git add .")
    os.system("cd "+ppath +" && "+'git commit -m "'+version+' - '+msg+'"')
    os.system("cd "+ppath +" && "+'git push')


# =============================================================================== #

if __name__ == '__main__':
    main()
    print "# ============================  GIT PUSH FINISHED  ============================ #"

