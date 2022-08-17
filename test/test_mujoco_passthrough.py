from utils import _pass_through, _test_dir
from urdf2mjcf.core import pass_through_mujoco


def test_basic_mjcf2mjcf():

    input_model = _test_dir() / "inputs" / "ip_model_1.xml"
    output_model = _test_dir() / "outputs" / "op_model_1.xml"

    result = _pass_through(input_model, pass_through_mujoco)

    with open(output_model, "r") as file:
        control = file.read()

    assert result == control


def test_basic_urdf2mjcf():

    input_model = _test_dir() / "inputs" / "ip_model_2.urdf"
    output_model = _test_dir() / "outputs" / "op_model_2.xml"

    result = _pass_through(input_model, pass_through_mujoco)

    with open(output_model, "r") as file:
        control = file.read()

    assert result == control
