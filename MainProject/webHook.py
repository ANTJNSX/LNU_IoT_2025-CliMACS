import requests


def send_discord_message(temp, hum):

    url = "https://discord.com/api/webhooks/your_webhook_url_here"  # Replace with your Discord webhook URL

    data = {"content": "OPEN A WINDOW", "username": "Window Wiper"}

    data["embeds"] = [
        {
            "description": f"THERES A HEAT OR HUMIDITY ISSUE;\nTemp: {temp}C, Humidity: {hum}%",
            "title": "WINDOW ALERT",
            "color": 16711680,
            "footer": {"text": "Raspberry Pi Pico W"},
        }
    ]

    result = requests.post(url, json=data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(f"Payload delivered successfully, code {result.status_code}.")
