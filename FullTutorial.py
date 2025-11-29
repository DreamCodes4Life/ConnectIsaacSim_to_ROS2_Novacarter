
Text icon
Tutorial_Basic_07.sh

Page
1
/
1
100%
## Introduction to Omnigraph
https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph/tutorials/gentle_intro.html

## Omnigraph tutorial with JetBot
https://docs.isaacsim.omniverse.nvidia.com/latest/omnigraph/omnigraph_tutorial.html

## Python Interface APIs
https://docs.isaacsim.omniverse.nvidia.com/latest/development_tools/index.html

## ROS 2 Integration
https://docs.isaacsim.omniverse.nvidia.com/latest/ros2_tutorials/ros2_landing_page.html

## Other NVIDIA Isaac platforms
    # NVIDIA Isaac Manipulator build AI-enabled robot arms
    https://developer.nvidia.com/isaac/manipulator

    # NVIDIA Isaac Perceptor  for the development of autonomous mobile robots (AMRs)
    https://developer.nvidia.com/isaac/perceptor

## SIL is a critical phase in robotics development, 
# where we test and validate software in a simulated 
# environment before deploying it to physical hardware

## Why use SIL in Isaac?
    # Helps us catch bugs early
    # Reduce physical prototyping
    # Improve safety
    # Accelerate development cycles

## Set the environment in Isaac SIM
## Go to  Isaac Sim Assets [Beta]
## Search for simple_room, press with the right button and click on “Add at current selection”
## Search for Nova_carter, Right click on nova_carter.usd and select “Add at current selection”

## Right-click on nova_carter (as seen in the video) and navigate to Create > Visual Scripting > Action Graph
## Add the following nodes to your graph:
    On Playback Tick            # It activates every simulation tick during playback

    ROS2 Subscribe Twist        # Subscribes to a ROS 2 topic, 
                                # Listens for geometry_msgs/msg/Twist messages,
                                # Outputs the linear and angular velocities into Omnigraph

    ROS2 Context                # it acts as the gateway between ROS 2 and Isaac Sim

    Scale To/From Stage Units   # handle unit conversion — especially between real-world units (like meters, radians) 
                                # and Isaac Sim’s internal stage units, which are typically measured in meters
    
    Two Break 3-Vector nodes    # allow you to split a 3D vector into its individual components — typically x, y, and z
    
    Make Array
    
    Differential Controller
        # In the right pane, set the following properties:
        Max Linear Speed: 2.0
        Max Angular Speed: 3.0
        Wheel Distance: 0.413
        Wheel Radius: 0.14
    
    Articulation Controller
        # Add Target -->  click on nova_carter > chassis_link > Select to set the target to the Carter robot
    
    Two Constant Token nodes
        # Click on the first Constant Token node.
        # Set its Input value to joint_wheel_left.
        # Click on the second Constant Token node.
        # Set its Input value to joint_wheel_right.

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

## Install ROS 2 Humble on Ubuntu 22.04
sudo apt update && sudo apt install -y locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

## Add ROS 2 Repository Keys
sudo apt install -y curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
    -o /usr/share/keyrings/ros-archive-keyring.gpg

## Add ROS 2 Repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

## Install ROS 2 Humble
sudo apt update
sudo apt install -y ros-humble-desktop

## Source ROS 2
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc

## Test ROS 2
apt list --installed | grep ros-humble

## Try running a node:
ros2 run demo_nodes_cpp talker

## In a second terminal (open another WSL Ubuntu window):
ros2 run demo_nodes_cpp listener

## Ctrl C to break the process and close the second terminal
## check the folder have been created for ROS
ls /opt/ros/humble

##Install colcon and Build Tools
sudo apt update
sudo apt install -y python3-colcon-common-extensions python3-pip build-essential

## Create and Build a ROS 2 Workspace (optional)
# Create workspace folders
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws

# Build the workspace (empty for now)
colcon build

# Now source the generated setup file:
source install/setup.bash

# To load it every time automatically, you can add this to your ~/.bashrc:
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc

    ## For Windows Users:
        ## Enable Network Between Windows and WSL2
        export ROS_DOMAIN_ID=0  # Must match on both sides
        export RMW_IMPLEMENTATION=rmw_fastrtps_cpp

        ## Identify WSL2’s IP Address, In WSL2 (Ubuntu)
        ip addr show eth0 | grep inet

        ## From the Command Line (Before Launching Isaac Sim)
        ## in PowerShell set the environment variables first:
        $env:ROS_DOMAIN_ID="0"
        $env:RMW_IMPLEMENTATION="rmw_fastrtps_cpp"
        & "C:\path\to\isaac-sim.bat"

        ## WSL2 – Prepare ROS 2
        source /opt/ros/humble/setup.bash

## If you didnt have ROS2 configured previously, re-launch ISAACSIM
isaac-sim.selector.bat

## Try next command in your terminal:
ros2 topic list

## Click Play in your scene, and try again:
ros2 topic list
    # You will see a new topic connected

## To drive the robot forward, run the following command
ros2 topic pub /cmd_vel geometry_msgs/Twist "{'linear': {'x': 0.2, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}}"

## To stop the robot, run:
ros2 topic pub /cmd_vel geometry_msgs/Twist "{'linear': {'x': 0.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}}"

##  Install Teleop Package
sudo apt-get install ros-humble-teleop-twist-keyboard

## Start the teleop_twist_keyboard node
ros2 run teleop_twist_keyboard teleop_twist_keyboard
    
    #  keyboard layout
    i = move forward (linear.x > 0)
    , = move backward (linear.x < 0)
    j = turn left (angular.z > 0)
    l = turn right (angular.z < 0)
    k = stop (linear = 0, angular = 0)
    u, o, m, . = combine forward/backward with turning

    I = move forward (linear.x > 0)
    < (comma) = move backward (linear.x < 0)
    J = move left (linear.y > 0)
    L = move right (linear.y < 0)

    t = up (linear.z > 0)
    b = down (linear.z < 0)


## Script Editor is a built-in Python editor within Isaac Sim's
## In the Isaac Sim Menu Bar, 
click on Window > Script Editor.
Click Run or press Ctrl+Enter to execute an entire script
Go to the Tab Menu within the Script Editor
Click on Tab > Add Tab to open a new tab
    ## These are shared environments, what runs in one tab is available in the others

## Interactive Scripting
https://docs.omniverse.nvidia.com/isaacsim/latest/gui_tutorials/tutorial_gui_interactive_scripting.html

## Using USD APISs
Open Isaac Sim and create a new, empty stage

## In the Script Editor, paste the following code to set up

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
from pxr import UsdPhysics, PhysxSchema, Gf, PhysicsSchemaTools, UsdGeom

import omni 

stage = omni.usd.get_context().get_stage() 
 
# Setting up Physics Scene 
gravity = 9.8 
scene = UsdPhysics.Scene.Define(stage, "/World/physics") 
scene.CreateGravityDirectionAttr().Set(Gf.Vec3f(0.0, 0.0, -1.0)) 
scene.CreateGravityMagnitudeAttr().Set(gravity)  
PhysxSchema.PhysxSceneAPI.Apply(stage.GetPrimAtPath("/World/physics")) 
physxSceneAPI = PhysxSchema.PhysxSceneAPI.Get(stage, "/World/physics") 
physxSceneAPI.CreateEnableCCDAttr(True) 
physxSceneAPI.CreateEnableStabilizationAttr(True) 
physxSceneAPI.CreateEnableGPUDynamicsAttr(False) 
physxSceneAPI.CreateBroadphaseTypeAttr("MBP") 
physxSceneAPI.CreateSolverTypeAttr("TGS")

# Setting up Ground Plane 
PhysicsSchemaTools.addGroundPlane(stage, "/World/groundPlane", "Z", 15, Gf.Vec3f(0,0,0), Gf.Vec3f(0.7))

# Adding a Cube 
path = "/World/Cube" 
cubeGeom = UsdGeom.Cube.Define(stage, path) 
cubePrim = stage.GetPrimAtPath(path) 
size = 0.5 
offset = Gf.Vec3f(0.5,0.2,1.0) 
cubeGeom.CreateSizeAttr(size) 
cubeGeom.AddTranslateOp().Set(offset)

# Attach Rigid Body and Collision Preset 
rigid_api = UsdPhysics.RigidBodyAPI.Apply(cubePrim) 
rigid_api.CreateRigidBodyEnabledAttr(True) 
UsdPhysics.CollisionAPI.Apply(cubePrim)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

Click the Run button in the Script Editor

## Omniverse USD DOcumentation
https://docs.isaacsim.omniverse.nvidia.com/latest/omniverse_usd/index.html

## Using Isaac Sim Core APIs
Create a new stage from File > New From Stage Template > Empty.
In the Script Editor, paste the following script to set up a ground plane and add a dynamic cube

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
import numpy as np 
from omni.isaac.core.objects import DynamicCuboid 
from omni.isaac.core.objects.ground_plane import GroundPlane 
from omni.isaac.core.physics_context import PhysicsContext 

PhysicsContext() 
GroundPlane(prim_path="/World/groundPlane", size=10, color=np.array([0.5, 0.5, 0.5])) 
DynamicCuboid(prim_path="/World/cube",
     position=np.array([-.5, -.2, 1.0]),
     scale=np.array([.5, .5, .5]),
     color=np.array([.2,.3,0.]))
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

## Core APIs tutorial
https://docs.omniverse.nvidia.com/isaacsim/latest/core_api_tutorials/index.html

## Developer Environment Setup
https://nvidia-isaac-ros.github.io/getting_started/dev_env_setup.html

## Isaac ROS Development Environment
https://nvidia-isaac-ros.github.io/concepts/docker_devenv/index.html#development-environment

## ****************************************************************************************************
    # NEXT SECTION:
    # Gain hands-on experience with Isaac ROS development tools.
    # Learn how to set up and run the image segmentation package using a docker-based development container.
    # Test the PeopleSemSegNet model on pre-recorded data to validate its functionality.
## ****************************************************************************************************

## PeopleSemSegNet Model Card
https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/peoplesemsegnet

## Clone repo for Isaac Ros Common in your root
git clone https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common.git

## Set the variables paths to ROS workspace and ISAAC ROS COMMON repo
export PATH_TO_ISAAC_ROS_COMMON=~/isaac_ros_common
export PATH_TO_ROS_WORKSPACE=~/ros2_ws

## make them permanents
echo 'export PATH_TO_ISAAC_ROS_COMMON=~/isaac_ros_common' >> ~/.bashrc
echo 'export PATH_TO_ROS_WORKSPACE=~/ros2_ws' >> ~/.bashrc
source ~/.bashrc
            ## In case error connecting to docker!!
            ## Add user to docker container
            sudo usermod -aG docker $USER

            ## then close terminal, in powershell run:
            wsl --shutdown
            wsl -d Ubuntu-22.04

    ## NOTE: next command to run and jump into docker container
    docker run --rm -it ubuntu:22.04 bash

## we might need Git LFS
sudo apt update
sudo apt install git-lfs
git lfs install

## Installing the NVIDIA Container Toolkit
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

## Update the packages list from the repository:
sudo apt-get update

## Install the NVIDIA Container Toolkit packages:
sudo apt-get install -y nvidia-container-toolkit

## Restart the Docker daemon:
## or If you are using WSL in Windows, just close docker and open it again
sudo systemctl restart docker

## verify the NVIDIA runtime works:
docker run --rm --runtime=nvidia --gpus all nvidia/cuda:12.2.0-base-ubuntu22.04 nvidia-smi

## You should see something like:
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 575.57.04              Driver Version: 576.52         CUDA Version: 12.9     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 3090        On  |   00000000:01:00.0  On |                  N/A |
| 30%   55C    P3             81W /  350W |    9380MiB /  24576MiB |     27%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A              31      G   /Xwayland                             N/A      |
+-----------------------------------------------------------------------------------------+

## Create a ROS 2 workspace for experimenting with Isaac ROS
mkdir -p  ~/workspaces/isaac_ros-dev/src
echo "export ISAAC_ROS_WS=${HOME}/workspaces/isaac_ros-dev/" >> ~/.bashrc
source ~/.bashrc

## We expect to use the ISAAC_ROS_WS environmental variable to refer to this ROS 2 workspace directory, in the future.

##  Log in to nvcr.io via Docker
docker login nvcr.io
## next is an example, not working anymore, you need to get your api key
## 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

## clone the isaac_ros_common
cd ${ISAAC_ROS_WS}/src && git clone -b release-3.1 https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common.git isaac_ros_common

## Sensors Setup if needed, no needed for this lab
## We strongly recommend installing all sensor dependencies before starting any 
## quickstarts. Some sensor dependencies require restarting the Isaac ROS Dev container 
## during installation, which will interrupt the quickstart process.
https://nvidia-isaac-ros.github.io/getting_started/hardware_setup/sensors/index.html

## Download Quickstart Assets
https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_image_segmentation/isaac_ros_unet/index.html#quickstart

## Download quickstart data from NGC:
sudo apt-get install -y curl jq tar

## lets create a file to run some commands
nano download_unet_assets.sh

## paste the next
## -----------------------------------------------------------------------------------------------------------
## -----------------------------------------------------------------------------------------------------------
NGC_ORG="nvidia"
NGC_TEAM="isaac"
PACKAGE_NAME="isaac_ros_unet"
NGC_RESOURCE="isaac_ros_unet_assets"
NGC_FILENAME="quickstart.tar.gz"
MAJOR_VERSION=3
MINOR_VERSION=2
VERSION_REQ_URL="https://catalog.ngc.nvidia.com/api/resources/versions?orgName=$NGC_ORG&teamName=$NGC_TEAM&name=$NGC_RESOURCE&isPublic=true&pageNumber=0&pageSize=100&sortOrder=CREATED_DATE_DESC"
AVAILABLE_VERSIONS=$(curl -s \
    -H "Accept: application/json" "$VERSION_REQ_URL")
LATEST_VERSION_ID=$(echo $AVAILABLE_VERSIONS | jq -r "
    .recipeVersions[]
    | .versionId as \$v
    | \$v | select(test(\"^\\\\d+\\\\.\\\\d+\\\\.\\\\d+$\"))
    | split(\".\") | {major: .[0]|tonumber, minor: .[1]|tonumber, patch: .[2]|tonumber}
    | select(.major == $MAJOR_VERSION and .minor <= $MINOR_VERSION)
    | \$v
    " | sort -V | tail -n 1
)
if [ -z "$LATEST_VERSION_ID" ]; then
    echo "No corresponding version found for Isaac ROS $MAJOR_VERSION.$MINOR_VERSION"
    echo "Found versions:"
    echo $AVAILABLE_VERSIONS | jq -r '.recipeVersions[].versionId'
else
    mkdir -p ${ISAAC_ROS_WS}/isaac_ros_assets && \
    FILE_REQ_URL="https://api.ngc.nvidia.com/v2/resources/$NGC_ORG/$NGC_TEAM/$NGC_RESOURCE/\
versions/$LATEST_VERSION_ID/files/$NGC_FILENAME" && \
    curl -LO --request GET "${FILE_REQ_URL}" && \
    tar -xf ${NGC_FILENAME} -C ${ISAAC_ROS_WS}/isaac_ros_assets && \
    rm ${NGC_FILENAME}
fi
## -----------------------------------------------------------------------------------------------------------
## -----------------------------------------------------------------------------------------------------------


## Then press:
Ctrl + O → to write (save) the file
Enter → to confirm the filename
Ctrl + X → to exit the editor

## Make the script executable
chmod +x download_unet_assets.sh

## Run the script
./download_unet_assets.sh

## Build isaac_ros_unet
## Clone this repository under ${ISAAC_ROS_WS}/src
cd ${ISAAC_ROS_WS}/src
git clone -b release-3.2 https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_image_segmentation.git isaac_ros_image_segmentation
git clone -b release-3.2 https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common.git isaac_ros_common

    ## Do this if you get an error creating the docker container
    ## Edit Dockerfile.x86_64 to avoid version error
    nano ~/workspaces/isaac_ros-dev/src/isaac_ros_common/docker/Dockerfile.x86_64
    # Upgrade system packages for security patches
    ls
    ##  modify this block:
    RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && apt-get install -y \
            nghttp2=1.43.0-1ubuntu0.2 \
            openssh-client=1:8.9p1-3ubuntu0.10 \
            libcurl3-gnutls=7.81.0-1ubuntu1.20 \
            libc-bin=2.35-0ubuntu3.8

    # To this:
    RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && apt-get install -y \
            nghttp2 \
            openssh-client \
            libcurl3-gnutls \
            libc-bin
    ## After editing, press:
    Ctrl + O (to save)
    Enter to confirm the filename
    Ctrl + X to exit        

## Launch the Docker container using the run_dev.sh script
$PATH_TO_ISAAC_ROS_COMMON/scripts/run_dev.sh -d $ISAAC_ROS_WS

## you should land in Isaac ROS development container: admin@docker-desktop:/workspaces/isaac_ros-dev$
✅ Docker used the official NVIDIA pre-built image
✅ The workspace at ~/workspaces/isaac_ros-dev is mounted at /workspaces/isaac_ros-dev in the container
✅ You're running as a non-root user (admin)
From here, you're ready to start working with Isaac ROS packages

## Use rosdep to install the package’s dependencies
sudo apt-get update
rosdep update && rosdep install --from-paths ${ISAAC_ROS_WS}/src/isaac_ros_image_segmentation/isaac_ros_unet --ignore-src -y

## Build the package from source
cd ${ISAAC_ROS_WS}
colcon build --symlink-install --packages-up-to isaac_ros_unet --base-paths ${ISAAC_ROS_WS}/src/isaac_ros_image_segmentation/isaac_ros_unet

## Source the ROS workspace:
source install/setup.bash

## Prepare PeopleSemSegnet Model
sudo apt-get install -y ros-humble-isaac-ros-peoplesemseg-models-install &&
ros2 run isaac_ros_peoplesemseg_models_install install_peoplesemsegnet_vanilla.sh --eula &&
ros2 run isaac_ros_peoplesemseg_models_install install_peoplesemsegnet_shuffleseg.sh --eula

## Build isaac_ros_unet
https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_image_segmentation/isaac_ros_unet/index.html#build-package-name

        ## Clone this repository under ${ISAAC_ROS_WS}/src -- fromsource
        cd ${ISAAC_ROS_WS}/src
        git clone -b release-3.2 https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_image_segmentation.git isaac_ros_image_segmentation

## Install the prebuilt Debian package:
sudo apt-get update
sudo apt-get install -y ros-humble-isaac-ros-unet

## Prepare PeopleSemSegnet Model
## Download and install model assets inside the Docker container:
## This process will install model assets and convert the downloaded PeopleSemSegNet model into a TensorRT plan file optimized for GPU inference.
sudo apt-get install -y ros-humble-isaac-ros-peoplesemseg-models-install &&
ros2 run isaac_ros_peoplesemseg_models_install install_peoplesemsegnet_vanilla.sh --eula &&
ros2 run isaac_ros_peoplesemseg_models_install install_peoplesemsegnet_shuffleseg.sh --eula

    ## Check directories have been created
    ls /workspaces/isaac_ros-dev/isaac_ros_assets/models/peoplesemsegnet/
    ## you should see:
    deployable_quantized_vanilla_unet_onnx_v2.0
    optimized_deployable_shuffleseg_unet_amr_v1.0


    ## Learn more about rosbags
    https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data.html
    ## Learn more about launch files
    https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Launch-Main.html

    ## A rosbag is a file format in ROS used to record and playback data streams, such as images or sensor readings.

## start the image segmentation package.
## install the following dependencies:
sudo apt-get update
sudo apt-get install -y ros-humble-isaac-ros-examples

## Run the following launch file to spin up a demo of this package using the quickstart rosbag:
ros2 launch isaac_ros_examples isaac_ros_examples.launch.py launch_fragments:=unet interface_specs_file:=${ISAAC_ROS_WS}/isaac_ros_assets/isaac_ros_unet/quickstart_interface_specs.json engine_file_path:=${ISAAC_ROS_WS}/isaac_ros_assets/models/peoplesemsegnet/deployable_quantized_vanilla_unet_onnx_v2.0/1/model.plan input_binding_names:=['input_1:0']
    ## Check for the message Node was started in the terminal to confirm that the package is running without error
    
## Open a second terminal (if windows, another powershell)
    ## if using WSL
    wsl -d Ubuntu-22.04

## you might need to set the path again
export PATH_TO_ISAAC_ROS_COMMON=~/workspaces/isaac_ros-dev/src/isaac_ros_common

## then Open a second terminal inside the Docker container
$PATH_TO_ISAAC_ROS_COMMON/scripts/run_dev.sh -d $ISAAC_ROS_WS

## Run the rosbag file to simulate an image stream
ros2 bag play -l ${ISAAC_ROS_WS}/isaac_ros_assets/isaac_ros_unet/quickstart.bag

## Open a third terminal as before
## Run rqt_image_view
ros2 run rqt_image_view rqt_image_view /unet/colored_segmentation_mask

## ****************************************************************************************************
    # NEXT/LAST SECTION:
    # Integrate the Isaac ROS image segmentation package with a simulated environment in Isaac Sim
    # we will demonstrate how Software-in-the-Loop (SIL) enables testing and validating software in a controlled virtual settin
## ****************************************************************************************************
## In Isaac Sim navigate to Windows --> Examples --> robotics example
## Then in Robotics Examples tab, on the left menu select ROS2 --> ISAAC ROS
## Then select Sample Scene and in the right windows click on load sample scene

## Now click play in your scene
ros2 topic list
    # you should see all related topics

## In the same terminal, use the following command to launch the image segmentation package
ros2 launch isaac_ros_unet isaac_ros_unet_tensor_rt_isaac_sim.launch.py \
  engine_file_path:=${ISAAC_ROS_WS}/isaac_ros_assets/models/peoplesemsegnet/deployable_quantized_vanilla_unet_onnx_v2.0/1/model.plan \
  input_binding_names:="['input_1:0']" \
  force_engine_update:=false

## In a second terminal.inside the docker
ros2 run rqt_image_view rqt_image_view
Displaying Tutorial_Basic_07.sh.
