import reflex as rx
from .pages import *

from .states.profile import Profile

app = rx.App(theme=rx.theme(appearance="light"))
app.add_custom_404_page(
    rx.cond(
        Profile.is_hydrated & Profile.verified,
        rx.center(
            rx.button(
                "Click Me!",
                size="3",
                variant="surface",
                color_scheme="gray",
                display=Profile.component_map["button"],
                on_click=Profile.wish_birthday,
                cursor="pointer",
            ),
            rx.vstack(
                rx.heading(f"Happy Birthday,", font_size="48px", text_align="center"),
                rx.heading(f"{Profile.name}!", font_size="48px", text_align="center"),
                display=Profile.component_map["birthday"],
                width="100%",
                font_family="Times New Roman",
                align="center",
                justify="center",
            ),
            rx.script(
                src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"
            ),
            width="100%",
            height="100vh",
        ),
        rx.center(
            rx.spinner(loading=Profile.is_loading, transform="scale(2)", color="red"),
            width="100%",
            height="100vh",
        ),
    ),
    on_load=Profile.get_user_profile,
    title=f"{Profile.title}",
)
