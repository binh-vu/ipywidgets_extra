from typing import List, Dict, Tuple, Callable, Any, Optional, Type

from IPython.core.display import display, Javascript

from labext.module import Module


class Tippy(Module):
    """
    By default, this module allows reload tippy content directly embedded in the attributes of elements

    Example:
        >>> Tippy.register()

        >>> display(HTML('<button data-tippy-content="<b>Hello</b> what are you doing" data-tippy-allowHTML="true">Text</button>'))

        >>> Tippy.render()
    """

    @classmethod
    def id(cls) -> str:
        return "tippy"

    @classmethod
    def css(cls) -> List[str]:
        return ["https://unpkg.com/tippy.js@6.2.3/dist/tippy.css"]

    @classmethod
    def js(cls) -> Dict[str, str]:
        return {"@popperjs/core": 'https://unpkg.com/@popperjs/core@2/dist/umd/popper.min', cls.id(): "https://unpkg.com/tippy.js@6/dist/tippy-bundle.umd.min"}

    @classmethod
    def dependencies(cls) -> List[Type['Module']]:
        return []

    @classmethod
    def render(cls):
        jscode = """
require(["@popperjs/core", "tippy"], function (popper, tippy) {
    tippy('[data-tippy-content]');
});"""
        display(Javascript(jscode))