urdf2mjcf
===

A utility tool to convert models of the URDF to that of MJCF.

Requirements
---

1. The tool utilizes the [MuJoCo engine](https://github.com/deepmind/mujoco/releases) during conversion, so make sure it is installed on your machine.

1. Tho tool interfaces the MuJoCo engine through its official [python bindings](https://pypi.org/project/mujoco/).
   
   - You can install the bindings via
     
     ```shell
     pip install mujoco
     ```
   - Alternatively, the repository comes with a `rosdep.yaml`, to which you can point rosdep to automatically resolve the installation.
     
     On Ubuntu, this could mean

     ```shell
     echo "yaml file:///PATH/TO/urdf2mjcf/rosdep.yaml" >> /etc/ros/rosdep/sources.list.d/urdf2mjcf.list
     rosdep update
     ```

     If everything is in order, running

     ```shell
     rosdep resolve python3-mujoco
     ```

     should give back

     ```shell
     #pip
     mujoco
     ```
