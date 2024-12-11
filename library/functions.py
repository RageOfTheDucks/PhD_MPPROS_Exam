import ctypes
from library.abstractions import Color, Camera3D, Vector3
from library import raylib

init_window = raylib.InitWindow
init_window.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
init_window.restype = None

set_target_fps = raylib.SetTargetFPS
set_target_fps.argtypes = [ctypes.c_int]
set_target_fps.restype = None

window_should_close = raylib.WindowShouldClose
window_should_close.argtypes = None
window_should_close.restype = ctypes.c_bool

update_camera = raylib.UpdateCamera
update_camera.argtypes = [ctypes.POINTER(Camera3D), ctypes.c_int]
update_camera.restype = None

begin_drawing = raylib.BeginDrawing
begin_drawing.argtypes = None
begin_drawing.restype = None

clear_background = raylib.ClearBackground
clear_background.argtypes = [Color]
clear_background.restype = None

begin_mode_3d = raylib.BeginMode3D
begin_mode_3d.argtypes = [Camera3D]
begin_mode_3d.restype = None

draw_cube = raylib.DrawCube
draw_cube.argtypes = [Vector3, ctypes.c_float, ctypes.c_float, ctypes.c_float, Color]
draw_cube.restype = None

draw_cube_wires = raylib.DrawCubeWires
draw_cube_wires.argtypes = [Vector3, ctypes.c_float, ctypes.c_float, ctypes.c_float, Color]
draw_cube_wires.restype = None

draw_grid = raylib.DrawGrid
draw_grid.argtypes = [ctypes.c_int, ctypes.c_float]
draw_grid.restype = None

end_mode_3d = raylib.EndMode3D
end_mode_3d.argtypes = None
end_mode_3d.restype = None

end_drawing = raylib.EndDrawing
end_drawing.argtypes = None
end_drawing.restype = None

close_window = raylib.CloseWindow
close_window.argtypes = None
close_window.restype = None

disable_cursor = raylib.DisableCursor
disable_cursor.argtypes = None
disable_cursor.restype = None

key_pressed = raylib.IsKeyPressed
key_pressed.argtypes = [ctypes.c_int]
key_pressed.restype = ctypes.c_bool

draw_text = raylib.DrawText
draw_text.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, Color]
draw_text.restype = None