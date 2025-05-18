from flask import Flask
import threading
import sniper_logic
import telegram_bot

# Keep-alive server for UptimeRobot pinging
def start_keep_alive():
    app = Flask('')
    @app.route('/')
    def home():
        return "Bot is alive!"
    app.run(host='0.0.0.0', port=8080)

# Run keep-alive server in a separate thread
threading.Thread(target=start_keep_alive).start()

# Start the sniper bot logic
sniper_logic.run_bot()