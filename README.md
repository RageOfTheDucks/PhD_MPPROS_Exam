# CubeInSpace: Python Binding for Raylib

### Overview

CubeInSpace is a Python implementation of a simple 3D cube rendering using bindings for the Raylib C library.
Utilizing the ctypes module the python implementation provides a simple interface for this 3D rendering.
The implementation prioritize simplicity and adherence to Pythonic principles.

## Design Choices

### Object Oriented 

Encapsulated functionality within the `CubeInSpace` class.
Methods like `set_cube_position`, `set_cube_color`, and `set_cube_dimension` expose, in an intuitive way, how to modify the cube properties.
Instance attributes such as `camera`, `screen_width` and `screen_height` are explicitly defined in the constructor enabling flexibility.

### Python's Dynamic Typing

Type hints (camera: Camera3D, color: Color, etc) provide helpful assist with IDE autocompletion, while still adhering to Python's dynamic typing.

### Modulariti & Minimized Boilerplate

The class encapsulates all logic related to cube rendering, camera interaction, and window management, adhering to the single responsibility principle.
The main operations such as window setup, rendering loop, and cleanup are all handled within the `display` method, simplifying the final utilization.


## Usage

**Initialization**: Create a Camera3D object and instantiate the CubeInSpace class:
```
camera = Camera3D()
cube = CubeInSpace(camera)
```

**Setting Cube Properties** (Optional): Adjust cube position, dimensions, and color using the provided methods:
```
cube.set_cube_position(1.0, 2.0, -5.0)
cube.set_cube_color(BLUE)
cube.set_cube_dimension(3.0, 3.0, 3.0)
```

**Displaying the Cube**: Call the `display` method to render the cube:
```
cube.display(camera_free=True)
```

*What a beautiful cube*
