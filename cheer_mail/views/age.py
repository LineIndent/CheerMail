import reflex as rx

from ..components.typography import render_title
from ..components.buttons import render_button

from ..states.base import Base


def render_email_view():
    return rx.vstack(
        rx.vstack(
            render_title(f"How old is {Base.birthday_name}?"),
            render_button(
                Base.birthday_age,
                Base.p_age,
                Base.update_age,
                ("age", ""),
            ),
            spacing="8",
            width="100%",
            align="center",
        ),
        rx.box(
            rx.button(
                rx.text("BACK", weight="bold"),
                variant="ghost",
                size="1",
                color_scheme="gray",
                cursor="pointer",
                on_click=Base.toggle_transition(("age", "name")),
            ),
            width="100%",
            max_width="25em",
            justify="center",
        ),
        spacing="3",
        width="100%",
        align="center",
        opacity=Base.view_map["age"]["opacity"],
        display=Base.view_map["age"]["display"],
        transition="all 500ms ease",
    )
