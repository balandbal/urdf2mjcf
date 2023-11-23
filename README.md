# urdf2mjcf

A utility tool to convert models of the URDF to that of MJCF.

## Python dependencies

Install the Python dependencies that rosdep can not resolve from the `requirements.txt`

```shell
pip install -r $(rospack find urdf2mjcf)/requirements.txt
```

## Running things

The package comes with command-line applications; use their help arguments for usage information.

```shell
urdf2mjcf --help
```
```
usage: urdf2mjcf [-h] [-s SENSOR_CONFIG] [-m MUJOCO_NODE] [--ground] [--lighting] [--version] [-l] [urdf] [mjcf]

Copyright (c) 2022 Fraunhofer IPA; use option '-l' to print license.

Parse a URDF model into MJCF format

positional arguments:
  urdf              the URDF file to convert (default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>)
  mjcf              the converted MJCF file (default: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)

optional arguments:
  -h, --help        show this help message and exit
  -s SENSOR_CONFIG  the XML file of the sensor configuration (default: None)
  -m MUJOCO_NODE    the XML file defining the global MuJoCo configuration (default: None)
  --ground          whether to add the default ground plane to the MuJoCo model (default: False)
  --lighting        whether to add the default lighting to the MuJoCo model (default: False)
  --version         show program's version number and exit
  -l                print license information (default: False)
```