import requests
import time
import json
from datetime import datetime

ADDRESS = "0x0000000000000000000000000000000000000000"  # 🔁 Замени на свой адрес
API_KEY = "YourEtherscanAPIKey"  # ⚠️ Нужен API ключ от Etherscan

def get_balance(addr):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={addr}&tag=latest&apikey={API_KEY}"
    response = requests.get(url).json()
    if response["status"] == "1":
        return int(response["result"]) / 10**18
    return None

def log_event(message):
    with open("track_log.txt", "a") as f:
        f.write(f"{datetime.utcnow().isoformat()} — {message}\n")

def main():
    prev_balance = get_balance(ADDRESS)
    log_event(f"Start tracking. Balance: {prev_balance} ETH")
    while True:
        time.sleep(60)  # Проверка раз в минуту
        current_balance = get_balance(ADDRESS)
        if current_balance is not None and abs(current_balance - prev_balance) > 0.1:
            log_event(f"🔍 Balance change: {prev_balance} → {current_balance} ETH")
            prev_balance = current_balance

if __name__ == "__main__":
    main()
