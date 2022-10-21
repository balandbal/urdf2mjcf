from urdf2mjcf.core import _parse_element, tostring
from urdf2mjcf.app import full_pipeline as urdf_to_mjcf
from utils import _test_dir


def _urdf():
    return _parse_element(_test_dir() / "inputs" / "panda.urdf")


def _sensor_config():
    return _parse_element(_test_dir() / "inputs" / "sensors.xml")


def _mujoco_node():
    return _parse_element(_test_dir() / "inputs" / "mujoco.xml")


def test_urdf2mjcf_mjnode():

    result_object = urdf_to_mjcf(_urdf(), mujoco_node=_mujoco_node())
    result_string = tostring(result_object, encoding="unicode")

    control_object = _parse_element(_test_dir() / "outputs" / "panda_mjnoded.xml")
    control_string = tostring(control_object, encoding="unicode")

    assert result_string == control_string


def test_urdf2mjcf_sensored():

    result_object = urdf_to_mjcf(_urdf(), sensor_config=_sensor_config())
    result_string = tostring(result_object, encoding="unicode")

    control_object = _parse_element(_test_dir() / "outputs" / "panda_sensored.xml")
    control_string = tostring(control_object, encoding="unicode")

    assert result_string == control_string
