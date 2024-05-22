# Create a ROS 2 World in ROS 2 Galactic from import Sketchfab models

# Step 1: Launch Gazebo Empty World and Spawn Robot


```bash
ros2 launch my_custom_world start_empty_world.launch.py
```

# Step 2: Spawn models into world

**1.** Download models in [Sketchfab](https://sketchfab.com/feed)

**2.** Import them in Blender and do your edits (Add multiple models, join them, scale them, position them ...)

**3.** Export Blender file as a **Collada** file (.dae). For example name it **my_env.dae**.

**4.** Add the new model data into the **models** folder.

# Step 3: Save world from Gazebo

**1.** In Gazebo select: **File** then **Save World As**.

**2.** Save it inside the **worlds** folder and name it **my_world.world**.

**3.** Update **start_my_world.launch.py** so that it reads the new **my_world.world** file.

**4.** All this is done so that we can directly launch the final world from the **start_my_world.launch.py**