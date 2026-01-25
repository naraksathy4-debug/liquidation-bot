import json, websocket, requests, os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(msg):
    if not TOKEN or not CHAT_ID:
        return
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def on_message(ws, message):
    data = json.loads(message)
    for e in data:
        o = e["o"]
        value = float(o["p"]) * float(o["q"])
        if value > 100000:
            send(f"🔥 {o['s']} liquidation ${value:,.0f}")

ws = websocket.WebSocketApp(
    "wss://fstream.binance.com/ws/!forceOrder@arr",
    on_message=on_message
)
ws.run_forever()
