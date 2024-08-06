import reflex as rx

from cheer_mail.states.base import Base


def render_button(
    value: str,
    placeholder: str,
    func: callable,
    view: tuple[str, str],
):
    return rx.hstack(
        rx.chakra.input(
            value=value,
            placeholder=placeholder,
            height="40px",
            width="100%",
            variant="unstyled",
            padding_left="10px",
            on_change=func,
        ),
        rx.button(
            "Enter",
            bg="#9e2015",
            height="40px",
            radius="none",
            max_width="8em",
            width="100%",
            cursor="pointer",
            on_click=Base.toggle_transition(view),
        ),
        width="100%",
        max_width="25em",
        height="40px",
        border="1px solid #9e2015",
        border_radius="8px",
        overflow="hidden",
        spacing="0",
    )


def render_link():
    return rx.hstack(
        rx.chakra.input(
            value=Base.birthday_url,
            height="40px",
            width="100%",
            variant="unstyled",
            padding_left="10px",
            is_read_only=True,
        ),
        rx.button(
            rx.icon(tag="copy", size=16),
            bg="#9e2015",
            height="40px",
            radius="none",
            max_width="4em",
            width="100%",
            cursor="pointer",
            on_click=Base.copy_url,
        ),
        width="100%",
        max_width="25em",
        height="40px",
        border="1px solid #9e2015",
        border_radius="8px",
        overflow="hidden",
        spacing="2",
    )
