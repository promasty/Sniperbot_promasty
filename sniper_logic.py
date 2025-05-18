import time
import config
import utils
import metadata_check
import telegram_bot

def run_bot():
    while True:
        try:
            token = utils.scan_new_token()
            if not token:
                time.sleep(5)
                continue

            if not utils.check_conditions(token):
                continue

            if not metadata_check.verify_metadata(token):
                telegram_bot.send_message("Token selhal při ověření metadat.")
                continue

            buy_result = utils.buy_token(token)
            if buy_result:
                telegram_bot.send_message(f"Koupen token {token['symbol']} za {config.BUY_AMOUNT_SOL} SOL.")
                utils.monitor_profit(token)

        except Exception as e:
            telegram_bot.send_message(f"Chyba: {e}")
        time.sleep(5)