from pypresence import Presence
from dotenv import load_dotenv
import os
import time

load_dotenv()
client_id = os.getenv("DISCORD_CLIENT_ID")

RPC = Presence(client_id)
RPC.connect()
print("Connected to Discord!")

RPC.update(
    details="Custom Details Here",
    state="Custom State Here",
    large_image="large_image_key",
    large_text="Large Image Text",
    small_image="small_image_key",
    small_text="Small Image Text",
    start = int(time.time()) - 3600,
    buttons=[
        {"label": "Button 1", "url": "https://example.com"},
        {"label": "Button 2", "url": "https://example.com"}
    ]
)

try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    RPC.clear()
    print("Presence cleared.")
