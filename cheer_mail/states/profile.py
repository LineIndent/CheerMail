import asyncio
import os
import httpx
from .base import Base
from urllib.parse import urlparse, parse_qs
import reflex as rx

KEY: str = os.getenv("KEY")


string = """
// Function to fire confetti
function fireConfetti() {
    confetti({
        particleCount: 120,
        spread: 1000,
        origin: { x: 0.5, y: 0.5 }
    });
}

for (let i = 0; i < 8; i++) {
    setTimeout(fireConfetti, i * 1000); // Delay in milliseconds
}
"""


class Profile(Base):

    verified: bool = False
    is_loading: bool = False

    msg: str
    uuid: str
    name: str
    age: str

    title: str

    component_map: dict[str, str] = {"button": "flex", "birthday": "none"}

    async def process_url_query(self):
        parsed_url = urlparse(
            "https://cheermail.reflex.run" + self.router.page.raw_path
        )
        query_params = parse_qs(parsed_url.path)

        self.uuid = query_params.get("/uuid")[0]
        self.name = query_params.get("name")[0]
        self.age = query_params.get("age")[0].replace("/", "")

    def wish_birthday(self):
        self.component_map["button"], self.component_map["birthday"] = (
            "none",
            "flex",
        )
        yield rx.call_script(string)

    async def get_user_profile(self):
        self.is_loading = True
        yield
        await asyncio.sleep(1.5)

        await self.process_url_query()

        async with httpx.AsyncClient() as client:
            res = await client.get(
                url="",  # insert database table to check if self.uuid exists...
                headers={"apikey": KEY, "Authorization": f"Bearer {KEY}"},
            )

            if len(res.json()) >= 1:
                self.verified = True
                self.is_loading = False
                self.title = "Happy Birthday"

            else:
                self.is_loading = False
                self.verified = False
                self.title = "404 Error"
                yield rx.toast.error("Invalid URL address.", duration=3000)
