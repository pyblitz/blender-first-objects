# First 3D Objects - Blender Python Course, Lesson 2
# Our plan, written first as comments:
# Step 1: clear the old scene, so we start empty
# Step 2: make 3 objects from one list - cube, sphere, cylinder
# Step 3: set each object's size, location and rotation
# Step 4: give each object its own color material
# Step 5: add a camera and a light, and orbit the camera

import bpy
import math
from mathutils import Vector

# Step 1: clear the old scene, so we start empty
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

# Step 2: make 3 objects from one list - cube, sphere, cylinder
# Each entry: kind, name, position, color, spin
OBJECTS = [
    ("CUBE", "MyCube", (-4.5, 0, 1.0), (1.0, 0.2, 0.2, 1.0), 0.5),
    ("SPHERE", "MySphere", (0.0, 0, 1.2), (0.2, 0.8, 0.2, 1.0), 0.0),
    ("CYLINDER", "MyCylinder", (4.5, 0, 1.0), (0.2, 0.4, 1.0, 1.0), 0.3),
]

made = []
for kind, name, pos, color, spin in OBJECTS:
    if kind == "CUBE":
        bpy.ops.mesh.primitive_cube_add(size=2, location=pos)
    elif kind == "SPHERE":
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=pos)
    else:
        bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2,
                                            location=pos)
    obj = bpy.context.active_object
    obj.name = name
    made.append((obj, color, spin))

# Step 3: set each object's size, location and rotation
# The cube keeps size 2. The sphere grows to 1.2 times its size.
# The cylinder keeps radius 1 and height 2. Each one also gets
# its own little spin, so we can see rotation clearly.
made[1][0].scale = (1.2, 1.2, 1.2)
for obj, color, spin in made:
    obj.rotation_euler = (0, 0, spin)

# Step 4: give each object its own color material
for obj, color, spin in made:
    material = bpy.data.materials.new(name=obj.name + "Color")
    material.use_nodes = True
    material.node_tree.nodes["Principled BSDF"].inputs[
        "Base Color"].default_value = color
    # Workbench renders use the viewport display color, so set it too
    material.diffuse_color = color
    obj.data.materials.append(material)

# a dark floor, so the objects have something to stand on
bpy.ops.mesh.primitive_plane_add(size=40, location=(0, 0, 0))
floor = bpy.context.active_object
floor.name = "Floor"
floor_material = bpy.data.materials.new(name="FloorColor")
floor_material.use_nodes = True
floor_material.node_tree.nodes["Principled BSDF"].inputs[
    "Base Color"].default_value = (0.08, 0.08, 0.1, 1.0)
floor_material.diffuse_color = (0.08, 0.08, 0.1, 1.0)
floor.data.materials.append(floor_material)

# Step 5: add a camera and a light, and orbit the camera
bpy.ops.object.camera_add(location=(0, -11, 6))
camera = bpy.context.active_object
camera.name = "ObjectCamera"
camera.data.lens = 35
bpy.context.scene.camera = camera

bpy.ops.object.light_add(type="SUN", location=(5, -5, 10))
sun = bpy.context.active_object
sun.name = "ObjectSun"
sun.data.energy = 3

# The camera slowly orbits the objects, always looking at the middle
TARGET = Vector((0, 0, 1))
for frame in [1, 20, 40]:
    angle = 2 * math.pi * (frame - 1) / 40
    camera.location = (11 * math.sin(angle),
                       -11 * math.cos(angle), 6)
    direction = TARGET - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    camera.keyframe_insert(data_path="location", frame=frame)
    camera.keyframe_insert(data_path="rotation_euler", frame=frame)

scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 40
scene.render.fps = 24
scene.render.engine = "BLENDER_WORKBENCH"
scene.render.resolution_x = 640
scene.render.resolution_y = 360

print("First Objects ready: " + str(len(made)) + " objects, "
      + "40 frames at 24 fps")
