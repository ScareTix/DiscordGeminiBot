import discord
from discord.ext import commands
import requests
import os
from flask import Flask
from threading import Thread

# Discord-Bot-Einrichtung
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Halte den Bot auf Replit am Leben
app = Flask('')

@app.route('/')
def home():
    return "Bot läuft!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Verwende Umgebungsvariablen für sensible Daten
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Funktion, um ein Bild mit der Google Imagen 4 API zu generieren
def generate_image(prompt):
    # Ersetze durch den tatsächlichen Google Imagen 4 API-Endpunkt
    url = "https://imagen.googleapis.com/v1beta/generate"
    headers = {
        "Authorization": f"Bearer {GOOGLE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": {
            "text": prompt
        },
        "imageConfig": {
            "resolution": "1024x1024"
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("imageUrl")
    else:
        print(f"Fehler: {response.status_code}, {response.text}")
        return None

# Befehl, um ein Bild zu generieren
@bot.command()
async def generate(ctx, *, prompt):
    await ctx.send(f"Ein Bild wird generiert für: {prompt}")
    image_url = generate_image(prompt)
    if image_url:
        await ctx.send(f"Hier ist dein Bild: {image_url}")
    else:
        await ctx.send("Bild konnte nicht generiert werden. Bitte versuche es später erneut.")

# Halte den Bot am Leben
keep_alive()

# Starte den Bot
bot.run(DISCORD_TOKEN)
