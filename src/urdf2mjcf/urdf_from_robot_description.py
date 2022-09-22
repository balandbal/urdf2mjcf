from io import StringIO
from typing import Iterable

from rospy import get_param

from .core import Element, _parse_element


def urdf_from_robot_description(filter_xpaths: Iterable[str] = None) -> Element:
    filter_xpaths = filter_xpaths if filter_xpaths is not None else []

    with StringIO(get_param("robot_description")) as urdf_string:
        urdf = _parse_element(urdf_string)

    for filter in filter_xpaths:
        for node in urdf.findall(filter):
            urdf.remove(node)

    return urdf
