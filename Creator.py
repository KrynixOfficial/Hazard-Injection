try:
    import ntpath
    import os
    import re
    from sys import argv
    import httpx
except:
    import os

    input("Found Missing Modules Required For Building, Press Enter To Install Them!")
    os.system("pip install httpx")
    os.system("cls")
    input("Re-Launch The Program To Proceed!")
    os._exit(0)
