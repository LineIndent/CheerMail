import asyncio
from datetime import datetime
from typing import Dict, Tuple
import reflex as rx
import os
import httpx
import uuid


URL: str = os.getenv("URL")
KEY: str = os.getenv("KEY")


class Base(rx.State):
    # main vars ...
    birthday_uuid: str
    birthday_name: str
    birthday_age: str
    birthday_url: str

    # placeholders ...
    p_name: str = "Type the person's name..."
    p_age: str = "Type the person's age..."

    # UI maps ...
    view_map: Dict[str, Dict[str, str]] = {
        "name": {"opacity": "1", "display": "flex"},
        "age": {"opacity": "0", "display": "none"},
        "url": {"opacity": "0", "display": "none"},
    }

    # application methods ...
    async def toggle_transition(self, view_name: Tuple[str, str]):
        if await self.checkpoint_name():
            if view_name[1]:
                # Hide the current view ...
                self.view_map[view_name[0]]["opacity"] = "0"
                yield
                self.view_map[view_name[0]]["display"] = "none"
                await asyncio.sleep(1.1)

                # Show the new view ...
                self.view_map[view_name[1]]["display"] = "flex"
                self.view_map[view_name[1]]["opacity"] = "1"

            else:
                if await self.checkpoint_age():
                    await self.send_data_to_db()

                    self.view_map[view_name[0]]["opacity"] = "0"
                    yield
                    self.view_map[view_name[0]]["display"] = "none"
                    await asyncio.sleep(1.1)

                    self.birthday_url = f"https://cheermail.reflex.run/uuid={self.birthday_uuid}&name={self.birthday_name}&age={self.birthday_age}"

                    self.view_map["url"]["display"] = "flex"
                    self.view_map["url"]["opacity"] = "1"

                else:
                    yield rx.toast.error("Enter the person's age - numbers only!")

        else:
            yield rx.toast.error("Enter the person's name!")

    async def checkpoint_name(self):
        return True if self.birthday_name else False

    async def checkpoint_age(self):
        return True if self.birthday_age.isdigit() else False

    async def update_name(self, value: str):
        self.birthday_name = value

    async def update_age(self, value: str):
        self.birthday_age = value

    async def copy_url(self):
        yield [rx.toast.success("Copied URL"), rx.set_clipboard(self.birthday_url)]

    async def send_data_to_db(self):
        self.birthday_uuid: str = str(uuid.uuid4())

        data: dict[str, str] = {
            "id": self.birthday_uuid,
            "name": self.birthday_name,
            "age": self.birthday_age,
            "stamp": str(int(datetime.now().timestamp())),
        }

        async with httpx.AsyncClient() as client:
            res = await client.post(
                URL,
                headers={
                    "apikey": KEY,
                    "Authorization": f"Bearer {KEY}",
                    "Content-Type": "application/json",
                    "Prefer": "return-minimal",
                },
                json=data,
            )
