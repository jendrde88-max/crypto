#!/usr/bin/env python3
import json
import websocket

# Threshold for a "huge" buy (ETH)
HUGE_BUY_THRESHOLD = 100

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@trade"

def on_message(ws, message):
    data = json.loads(message)
    price = float(data['p'])
    qty = float(data['q'])
    side = "BUY" if data['m'] == False else "SELL"

    if side == "BUY" and qty >= HUGE_BUY_THRESHOLD:
        print(f"\n🚨 HUGE BUY DETECTED! 🚨\nQuantity: {qty} ETH\nPrice: {price} USDT\nTrade ID: {data['t']}\n")

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("### Connection closed ###")

def on_open(ws):
    print("Connected to Binance ETH/USDT trade stream...")

if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        SOCKET,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()