import reflex as rx

from ..components.typography import render_title
from ..components.buttons import render_button

from ..states.base import Base


def render_name_view():
    return rx.vstack(
        render_title("Who's birthday is it?"),
        render_button(
            Base.birthday_name,
            Base.p_name,
            Base.update_name,
            ("name", "age"),
        ),
        spacing="8",
        width="100%",
        align="center",
        opacity=Base.view_map["name"]["opacity"],
        display=Base.view_map["name"]["display"],
        transition="all 500ms ease",
    )
