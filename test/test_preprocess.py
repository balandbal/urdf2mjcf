from utils import _test_dir
from urdf2mjcf.core import abspath_from_ros_uri, add_mujoco_node, _parse_element


def test_resolving_ros_uris():

    with open(_test_dir() / "inputs" / "ros_uris.txt", "r") as input_file:
        input_uris = [uri.rstrip() for uri in input_file]

    with open(_test_dir() / "outputs" / "resolved_ros_uris.txt", "r") as output_file:
        control_uris = [uri.rstrip() for uri in output_file]

    for input_uri, control_uri in zip(input_uris, control_uris):
        assert abspath_from_ros_uri(input_uri) == control_uri


def test_update_mujoco_node():
    input_model = _test_dir() / "inputs" / "ip_model_3.urdf"
    urdf = _parse_element(input_model)

    add_mujoco_node(urdf, None)

    assert len(urdf.findall(".//mujoco")) == 0


if __name__ == "__main__":

    with open(_test_dir() / "inputs" / "ros_uris.txt", "r") as input_file:
        input_uris = [uri.rstrip() for uri in input_file]

    for input_uri in input_uris:
        print(abspath_from_ros_uri(input_uri))
