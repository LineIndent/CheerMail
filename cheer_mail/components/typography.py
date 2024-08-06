import reflex as rx


def render_title(title: str):
    return rx.heading(
        title,
        font_size="34px",
        font_family="Times New Roman",
        text_align="center",
        line_spacing="2em",
    )
