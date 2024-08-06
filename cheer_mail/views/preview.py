import reflex as rx

from ..components.typography import render_title
from ..components.buttons import render_link

from ..states.base import Base


def render_preview_view():
    return rx.vstack(
        rx.vstack(
            rx.vstack(
                render_title(f"Share the link below to say happy birthday!"),
                width="100%",
                max_width="23em",
            ),
            render_link(),
            spacing="8",
            width="100%",
            align="center",
        ),
        spacing="3",
        width="100%",
        align="center",
        opacity=Base.view_map["url"]["opacity"],
        display=Base.view_map["url"]["display"],
        transition="all 500ms ease",
    )
