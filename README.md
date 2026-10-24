# Blender Python Course — Lesson 2: First 3D Objects

PyBlitz — Blender Python Course: "Python Se Blender Expert Bano"

## What this script does

`first_objects.py` runs **inside Blender** (Scripting workspace) and builds
a small scene from code:

- Clears the old scene
- Makes **3 objects from one list**: a red cube, a green sphere, and a
  blue cylinder — with one loop, not three copies of the code
- Sets each object's **size, location, and rotation** (the cube spins
  0.5, the cylinder 0.3, the sphere stays straight)
- Gives each object **its own color material**
- Adds a **camera that orbits** the objects and a sun light, then renders
  40 frames at 24 fps

## Requirements

- Blender **4.5.15 LTS** (tested; any recent Blender 4.x should work)
- No add-ons, no paid tools

## How to run it

1. Open Blender
2. Click the **Scripting** workspace at the top
3. Click **Open** in the Text Editor and open `first_objects.py`
4. Press **Run Script**
5. Watch the camera orbit the three objects in the 3D Viewport

## Exercises (from the Lesson 2 video)

1. **Add a cone to the row.** Add a fourth entry to the `OBJECTS` list
   with kind `CONE`, and use `primitive_cone_add` in the loop.
2. **Change one object's size or color.** Try sphere scale `2`, or the
   cube's color yellow, then run again.

## Files

- `first_objects.py` — the full lesson script
- `first_objects.blend` — the scene saved after running the script
- `render/` — the 40 Workbench preview frames

## Course

- Lesson 1: Cube Wave Animation — 9 colored cubes, loop + keyframes
- **Lesson 2 (this one): First 3D Objects — cube, sphere, cylinder**
- Lesson 3 (coming next): Colors & Materials

Full videos on YouTube: https://youtube.com/@pyblitz
