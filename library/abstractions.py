import ctypes

# Re-define Color 
class Color(ctypes.Structure):
    _fields_ = [
        ("r", ctypes.c_ubyte),
        ("g", ctypes.c_ubyte),
        ("b", ctypes.c_ubyte),
        ("a", ctypes.c_ubyte)
    ]

# Re-define Vector3 
class Vector3(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float)
    ]

# Re-define Camera3D 
class Camera3D(ctypes.Structure):
    _fields_ = [
        ("position", Vector3),
        ("target", Vector3),
        ("up", Vector3),
        ("fovy", ctypes.c_float),
        ("projection", ctypes.c_int)
    ]

# Colors!
RAYWHITE = Color(245, 245, 245, 255)
RED = Color(230, 41, 55, 255)
MAROON = Color(190, 33, 55, 255)
BLUE = Color(0, 121, 241, 255)
SKYBLUE = Color(102, 191, 255, 255)
LIME = Color( 0, 158, 47, 255 )
DARKPURPLE = Color(112, 31, 126, 255)

CAMERA_FREE = 0