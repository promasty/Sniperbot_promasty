# Sniper Bot pro Pump.fun (Solana)

Tento bot:
- Sleduje nové tokeny na Pump.fun
- Kontroluje likviditu, marketcap, metadata
- Automaticky kupuje tokeny za 0.05 SOL
- Sleduje zisk a provádí automatické prodeje
- Posílá notifikace do Telegramu

## Nasazení:
1. Nahraj tento projekt na [https://replit.com/](https://replit.com/)
2. Uprav `config.py` – vlož privátní klíč, adresu peněženky, Telegram token a chat_id
3. Spusť `main.py`
4. Získané Replit URL přidej do [https://uptimerobot.com](https://uptimerobot.com) (HTTP monitor)

## Keep-alive server:
- Flask běží na portu 8080
- Pingování každých 5 minut udrží Replit běžící 24/7