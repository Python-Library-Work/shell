#coding: utf-8

try:
    from time import *
    from random import *
    import os
    import glob
    import platform
except ImportError:
    print("Missing Modules in Python...")
    main = input("Press a [ENTER] for Continue...")
    exit()

try:
    import patch
    import support
    patch.init() # In future, the support realy support you...
    support.init() 
except ImportError:
    print("=> This a raw version, patch and support not included...")

__version__ = "1.1.000-raw_version-00001"
__author__ = "Python Works"

# Repos of Shell
#__git__ = "https://github.com/Python-Library-Work/shell.git"
#############################################################

def __init_shell__():
    print("[*] Shell Version: "+ __version__)
    sleep(1)
    print("[*] Support Version: null")
"""
try:
    cursor = open('cursor.conf', 'r')
    cursor1 = cursor.read()
    cursor.close()
    print("Cursor Defined is: "+ cursor1)
except:
"""
cursor1 = "shell-1.1.000~$: "
main2 = 1
while(main2<100):
    main = input(cursor1)
    if(main=="shutdown"):
        print("Shutdown...")
        sleep(1)
        break
        print("{*} Retriggering the SystemStart...")
    elif(main=="edit-cursor"):
        os.system("nano ./cursor.conf")
    elif(main=="support"):
        try:
            support.backend()
        except:
            print("[*] Not Support of Mix System...")
    elif(main=="patch"):
        try:
            patch.backend()
        except:
            print("[*] Not patch of Mix System...")
    elif(main=="dectect-sys"):
        x = platform.system()
        #y = platform.realese()
        z = platform.python_version()
        print("System: "+ x)
        #print("Realese: "+ y)
        print("Py Version: "+ z)
    else:
        print("Command not Exist...")

print("Closing a Sys !!! bye bye")
