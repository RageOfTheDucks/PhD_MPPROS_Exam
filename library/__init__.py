import ctypes
from ctypes.util import *


try: 
    raylib = ctypes.CDLL(r".\raylib-5.5_win64_msvc16\raylib-5.5_win64_msvc16\lib\raylib.dll")
    print("Correctly loaded")
except OSError as e:
    print(e)
    print("Error loading raylib")
    sys.exit(1)