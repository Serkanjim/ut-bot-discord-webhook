from flask import Flask, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discordapp.com/api/webhooks/your-webhook-url"  # <-- Your webhook URL   

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get('message', 'UT Bot singal has been received!')

    discord_payload = {
        "content": f"📈 UT Bot Alarmı: {message}"
    }

    requests.post(DISCORD_WEBHOOK_URL, json=discord_payload)
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
