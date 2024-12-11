from library import wrap
from library.abstractions import *

camera = Camera3D(
    position=Vector3(10.0, 10.0, 10.0),
    target=Vector3(0.0, 0.0, 0.0),
    up=Vector3(0.0, 1.0, 0.0),
    fovy=45.0,
    projection=0 
)

cube = wrap.CubeInSpace(camera)

cube.set_cube_color(color = LIME)
cube.set_cube_position(1.0, 2.0, 2.0)
cube.set_cube_dimension(1.0, 1.0, 3.0)

cube.display(camera_free=True)