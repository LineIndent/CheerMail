import reflex as rx

from ..views.name import render_name_view
from ..views.age import render_email_view
from ..views.preview import render_preview_view


@rx.page("/", "CheerMail")
def index():
    return rx.center(
        render_name_view(),
        render_email_view(),
        render_preview_view(),
        width="100%",
        height="100vh",
    )
