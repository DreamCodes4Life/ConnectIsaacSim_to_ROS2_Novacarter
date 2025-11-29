## Go to  Isaac Sim Assets [Beta]
## Search for simple_room, press with the right button and click on “Add at current selection”
## Search for Nova_carter, Right click on nova_carter.usd and select “Add at current selection”

## Right-click on nova_carter (as seen in the video) and navigate to Create > Visual Scripting > Action Graph
## Add the following nodes to your graph:
    On Playback Tick            # It activates every simulation tick during playback
    ROS2 Subscribe Twist        # Subscribes to a ROS 2 topic,  # Listens for geometry_msgs/msg/Twist messages, # Outputs the linear and angular velocities into Omnigraph
    ROS2 Context                # it acts as the gateway between ROS 2 and Isaac Sim
    Scale To/From Stage Units   # handle unit conversion — especially between real-world units (like meters, radians) and Isaac Sim’s internal stage units, which are typically measured in meters
    Break 3-Vector    # allow you to split a 3D vector into its individual components — typically x, y, and z
    Break 3-Vector    # allow you to split a 3D vector into its individual components — typically x, y, and z
    Make Array
    Differential Controller
        # In the right pane, set the following properties:
        Max Linear Speed: 2.0
        Max Angular Speed: 3.0
        Wheel Distance: 0.413
        Wheel Radius: 0.14
    Articulation Controller 
        Add Target -->  click on nova_carter > chassis_link > Select to set the target to the Carter robot
    Constant Token # joint_wheel_left.
    Constant Token # joint_wheel_right..

      ## Only for Windows Users
      ## Open a powershell terminal and install an Ubuntu distro, if you dont have it
      wsl --install -d Ubuntu-22.04
      ## Then Launch it
      wsl -d Ubuntu-22.04
  
          # Note: 
          # To see active Distros
          wsl --list --verbose
          # To stop a specific distro/instance
          # wsl --terminate "Name of Distro" ie:
          wsl --terminate Ubuntu
