from pathlib import Path
from typing import Callable
from xml.etree.ElementTree import Element, tostring

from defusedxml.ElementTree import fromstring


def _pass_through(input_model: Path, converter: Callable[[Element], Element]) -> str:

    with open(input_model, "r") as file:
        model_xml: Element = fromstring(file.read())

    converted_model_xml = converter(model_xml)

    return tostring(converted_model_xml, encoding="unicode")


def _test_dir() -> Path:
    return Path(__file__).parent.resolve()
