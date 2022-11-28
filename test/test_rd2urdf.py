import sys
from pathlib import Path

import rospy
from urdf2mjcf.core import tostring
from urdf2mjcf.urdf_from_robot_description import urdf_from_robot_description

_test_dir = Path(__file__).resolve().parent
sys.path.append(str(_test_dir))

from test_urdf2mjcf import _urdf


def test_rd2urdf():
    urdf_in = _urdf()
    rospy.set_param("robot_description", tostring(urdf_in, encoding="unicode"))
    urdf_out = urdf_from_robot_description()
    assert tostring(urdf_in, encoding="unicode") == tostring(
        urdf_out, encoding="unicode"
    )
