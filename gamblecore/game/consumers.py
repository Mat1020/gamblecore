import asyncio, os, sys
from channels.generic.websocket import AsyncWebsocketConsumer

class TerminalConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        self.process = await asyncio.create_subprocess_exec(
            sys.executable,
            os.path.join("game", "script.py"),  # This is your script
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
        )

        asyncio.create_task(self.send_output())

    async def disconnect(self, close_code):
        if self.process:
            self.process.terminate()
            await self.process.wait()

    async def receive(self, text_data):
        self.process.stdin.write((text_data + "\n").encode())
        await self.process.stdin.drain()

    async def send_output(self):
        while True:
            line = await self.process.stdout.readline()
            if line:
                await self.send(line.decode())
            else:
                break