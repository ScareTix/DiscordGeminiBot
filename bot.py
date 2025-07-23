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

# Funktion, um ein Bild mit Google's Imagen 4 KI-Modell zu generieren
def generate_image(prompt):
    # Ersetze durch den tatsächlichen Imagen 4 API-Endpunkt
    url = "https://api.google.com/imagen/v4/generate-image"
    headers = {
        "Authorization": f"Bearer {GOOGLE_API_KEY}",  # Falls ein anderer Schlüssel benötigt wird, anpassen
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "resolution": "1024x1024"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("image_url")
    else:
        print(f"Fehler: {response.status_code}, {response.text}")
        return None

# Funktion, um mit dem Gemini 2.5 Pro Chat-Modell zu interagieren
def chat_with_gemini(prompt):
    # Ersetze durch den tatsächlichen Gemini 2.5 Pro Chat API-Endpunkt
    url = "https://api.gemini.com/v2.5/pro/chat"
    headers = {
        "Authorization": f"Bearer {GOOGLE_API_KEY}",  # Falls ein anderer Schlüssel benötigt wird, anpassen
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("response")
    else:
        print(f"Fehler: {response.status_code}, {response.text}")
        return "Entschuldigung, ich konnte keine Antwort generieren."

# Befehl, um ein Bild zu generieren
@bot.command()
async def generate(ctx, *, prompt):
    await ctx.send(f"Ein Bild wird generiert für: {prompt}")
    image_url = generate_image(prompt)
    if image_url:
        await ctx.send(f"Hier ist dein Bild: {image_url}")
    else:
        await ctx.send("Bild konnte nicht generiert werden. Bitte versuche es später erneut.")

# Befehl, um mit dem Chat-Modell zu interagieren
@bot.command()
async def chat(ctx, *, prompt):
    await ctx.send(f"Frage: {prompt}")
    response = chat_with_gemini(prompt)
    await ctx.send(f"Antwort: {response}")

# Halte den Bot am Leben
keep_alive()

# Starte den Bot
bot.run(DISCORD_TOKEN)
