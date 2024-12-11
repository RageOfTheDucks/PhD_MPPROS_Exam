from library.abstractions import *
from library.functions import *

class CubeInSpace:
    def __init__(self, camera: Camera3D, screen_width: int=1020, screen_height:int =640):
        self.camera = camera
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cube_position = Vector3(0.0, 0.0, 0.0)
        self.cube_color = RED
        self.w = 2.0
        self.h = 2.0
        self.d = 2.0

        disable_cursor()

    def set_cube_position(self, x: float, y: float, z: float):
        self.cube_position = Vector3(x,y,z)

    def set_cube_color(self, color: Color):
        self.cube_color = color

    def set_cube_dimension(self, w: float, h: float, d: float):
        self.h = h
        self.w = w
        self.d = d
    
    def display(self, camera_free:bool =False):
        raylib.InitWindow(self.screen_width, self.screen_height, b"What a beautiful plane!")
        raylib.SetTargetFPS(60)

        while not raylib.WindowShouldClose():
            raylib.UpdateCamera(ctypes.byref(self.camera), camera_free)

            if raylib.IsKeyPressed(257):
                self.camera.target = (0.0, 0.0, 0.0)

            raylib.BeginDrawing()
            raylib.ClearBackground(RAYWHITE)

            raylib.BeginMode3D(self.camera)
            raylib.DrawCube(self.cube_position, self.w, self.h, self.d, self.cube_color)
            #raylib.DrawCubeWires(self.cube_position, 2.0, 2.0, 2.0, MAROON)
            raylib.DrawGrid(10, 1.0)
            raylib.EndMode3D()

            if camera_free:
                draw_text("Press Enter to reset view".encode(), 10, 40, 20, DARKPURPLE)
                draw_text("Use WASD to move around".encode(), 10, 70, 20, DARKPURPLE)

            raylib.EndDrawing()

        raylib.CloseWindow()