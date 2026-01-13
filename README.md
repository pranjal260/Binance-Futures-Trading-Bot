# Binance Futures Trading Bot

A simplified Python trading bot for Binance Futures (USDT-M), using the official Binance API (Testnet).  
Designed for clarity, structure, logging, and user interaction via a menu-driven CLI interface.

---

## 🛠️ Features

✔ Menu-driven command-line interface  
✔ Input validation for symbol, side, order type, and quantity  
✔ Market, Limit, and Stop-Limit order support  
✔ Logging of API requests, responses, and errors  
✔ Clear error handling  
✔ Clean, reusable Python structure

---

## 🚀 Setup

### 1. Clone the repository
```bash
git clone https://github.com/pranjal260/Binance-Futures-Trading-Bot.git
cd Binance-Futures-Trading-Bot
```

### 2. Create & activate virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add API credentials
Create a file named `.env` (see `.env.example`) and add:

```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret
```

> ⚠ Do NOT commit `.env` to the repo.

---

## 📌 Usage

Run the bot:

```bash
python bot.py
```

You will be prompted to:
- select order type
- enter symbol (e.g. `BTCUSDT`)
- enter side (`BUY` or `SELL`)
- enter quantity
- (if needed) enter stop/limit prices

---

## 🧠 Design Notes

This bot focuses on backend trading logic with a clean interface, robust validation, and logging.  
A GUI/web frontend was intentionally omitted in favor of clarity and reliability.

---

## ⚠ Binance Testnet Note

Binance testnet API access may redirect to mainnet UI and restrict key generation.  
If testnet keys cannot be generated, orders may fail with an authentication error (`APIError -2015`).  
The trading logic remains correct and structured for futures testnet use.

---

## 📄 License

MIT
