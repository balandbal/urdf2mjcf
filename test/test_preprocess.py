from functools import lru_cache
from io import StringIO
import sys
from pathlib import Path

from urdf2mjcf.core import (
    abspath_from_ros_uri,
    add_mujoco_node,
    _parse_element,
    tostring,
    Element,
)

_test_dir = Path(__file__).resolve().parent
sys.path.append(str(_test_dir))


def test_resolving_ros_uris():
    _package_dir = _test_dir.parent
    _package_name = _package_dir.stem
    for path in (_test_dir / "inputs" / "meshes").glob("**/*.*"):
        input = f"package://{_package_name}/{path.relative_to(_package_dir)}"
        output = abspath_from_ros_uri(input)
        control = str(path.resolve())
        assert output == control, f"\n output:\n  '{output}'\n control:\n  '{control}'"


@lru_cache
def _get_mjnode1():
    with StringIO('<mujoco><compiler strippath="true" /></mujoco>') as node_1:
        mjnode1 = _parse_element(node_1)
    return mjnode1


@lru_cache
def _get_mjnode2():
    with open(_test_dir / "inputs" / "mujoco.xml", "r") as node_2:
        mjnode2 = _parse_element(node_2)
    return mjnode2


def test_add_mujoco_node_1():
    urdf = Element("robot")
    add_mujoco_node(urdf, None)
    assert (
        tostring(urdf, encoding="unicode")
        == '<robot><mujoco><compiler strippath="false" fusestatic="false" discardvisual="true"><lengthrange /></compiler><option><flag /></option><size /></mujoco></robot>'
    )


def test_add_mujoco_node_2():
    urdf = Element("robot")
    add_mujoco_node(urdf, _get_mjnode1())
    assert (
        tostring(urdf, encoding="unicode")
        == '<robot><mujoco><compiler strippath="true" fusestatic="false" discardvisual="true"><lengthrange /></compiler><option><flag /></option><size /></mujoco></robot>'
    )


def test_add_mujoco_node_3():
    urdf = Element("robot")
    add_mujoco_node(urdf, _get_mjnode2())
    assert (
        tostring(urdf, encoding="unicode")
        == '<robot><mujoco><compiler strippath="false" fusestatic="false" discardvisual="true"><lengthrange /></compiler><option timestep="0.001" cone="elliptic"><flag /></option><size /></mujoco></robot>'
    )


def test_update_mujoco_node_1():
    urdf = Element("robot")
    add_mujoco_node(urdf, _get_mjnode1())
    add_mujoco_node(urdf, _get_mjnode2())
    assert (
        tostring(urdf, encoding="unicode")
        == '<robot><mujoco><compiler strippath="false" fusestatic="false" discardvisual="true"><lengthrange /></compiler><option timestep="0.001" cone="elliptic"><flag /></option><size /></mujoco></robot>'
    )


def test_update_mujoco_node_2():
    urdf = Element("robot")
    add_mujoco_node(urdf, _get_mjnode2())
    add_mujoco_node(urdf, _get_mjnode1())
    assert (
        tostring(urdf, encoding="unicode")
        == '<robot><mujoco><compiler strippath="true" fusestatic="false" discardvisual="true"><lengthrange /></compiler><option timestep="0.001" cone="elliptic"><flag /></option><size /></mujoco></robot>'
    )


if __name__ == "__main__":

    with open(_test_dir / "inputs" / "ros_uris.txt", "r") as input_file:
        input_uris = [uri.rstrip() for uri in input_file]

    for input_uri in input_uris:
        print(abspath_from_ros_uri(input_uri))
