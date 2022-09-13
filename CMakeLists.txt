cmake_minimum_required(VERSION 3.0.2)
project(urdf2mjcf)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()

catkin_install_python(
  PROGRAMS
  scripts/urdf2mjcf
  scripts/rd2urdf
  scripts/urdf2mjcf_ros
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)