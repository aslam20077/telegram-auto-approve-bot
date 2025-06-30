
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest

api_id = 11324359
api_hash = "36029fe38f89df504b44093670b7a6c1"
bot_token = "8109910176:AAFgccVsSvNs0Ro8Y0THdZ3xa-PzgOE2Dhg"

app = Client("auto_approve_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_chat_join_request()
async def auto_approve(client, join_request: ChatJoinRequest):
    try:
        await client.approve_chat_join_request(join_request.chat.id, join_request.from_user.id)
        print(f"Approved: {join_request.from_user.first_name} in {join_request.chat.title}")
    except Exception as e:
        print(f"Error approving: {e}")

print("Bot is running...")
app.run()
