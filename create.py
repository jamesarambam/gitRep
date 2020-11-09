#!/usr/bin/python
"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Author : James Arambam
Date   : 03 Feb 2017
Description :


Input :
There are two input arguments
    i. First Argument will be the path to the local project directory :
            e.g  '/Users/james/workspace/test3'  here test3 is my project folder
    ii. Second Argument will be the url to git repository :
            Note : First create the repository in the remote site
            e.g 'https://jamesarambam@bitbucket.org/jamesarambam/test3.git'
            

Output :

    You can go to the online repository as check !


git Shell Commands :
git init
git add .
git commit -m "First commit"
git remote add origin remote repository URL
git remote -v
git push origin master


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

# ================================ priImports ================================ #

import sys
import os
import platform
from pprint import pprint

# ================================ secImports ================================ #

o = platform.system()

print "# ============================ START ============================ #"

# ============================================================================ #

# --------------------- Variables ------------------------------ #

ppath = os.getcwd() + "/"  # Project Path Location



# -------------------------------------------------------------- #

def main():

    local = sys.argv[1]
    remote = sys.argv[2]

    os.system("cd "+local +" && "+"git init")
    os.system("cd "+local +" && "+"git add .")
    os.system("cd "+local +" && "+'git commit -m "First commit"')
    os.system("cd "+local +" && "+"git remote add origin "+remote)
    os.system("cd "+local +" && "+"git remote -v")
    os.system("cd "+local +" && "+"git push origin master")



# =============================================================================== #

if __name__ == '__main__':
    main()
    print "# ============================  END  ============================ #"

