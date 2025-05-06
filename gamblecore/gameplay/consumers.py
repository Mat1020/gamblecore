import asyncio
import sys
from channels.generic.websocket import AsyncWebsocketConsumer
import threading
from io import StringIO
from gameplay.logic.SlotMachines import classic_slot_machine

class GameplayConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.input_queue = asyncio.Queue()
        self.loop = asyncio.get_event_loop()

        # Run the game logic in a background thread
        def run_game():
            # Redirect stdout
            sys.stdout = mystdout = StringIO()
            sys.stdin = self  # override input() calls
            try:
                classic_slot_machine.main()
            except Exception as e:
                print(f"Error: {e}")
            finally:
                sys.stdout = sys.__stdout__

            # Send all remaining output
            output = mystdout.getvalue()
            asyncio.run_coroutine_threadsafe(self.send(text_data=output), self.loop)

        threading.Thread(target=run_game).start()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        await self.input_queue.put(text_data + "\n")  # mimic user pressing Enter

    def readline(self):
        # This is called by input()
        return asyncio.run(self.input_queue.get())