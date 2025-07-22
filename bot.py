import discord
from discord.ext import commands
import requests
import os
from flask import Flask
from threading import Thread

# Discord bot setup
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Keep the bot alive on Replit
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Use environment variables for sensitive data
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Function to generate an image using Google's Imagen 4 API
def generate_image(prompt):
    # Replace with the actual Google Imagen 4 API endpoint
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
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Command to generate an image
@bot.command()
async def generate(ctx, *, prompt):
    await ctx.send(f"Generating an image for: {prompt}")
    image_url = generate_image(prompt)
    if image_url:
        await ctx.send(f"Here is your image: {image_url}")
    else:
        await ctx.send("Failed to generate image. Please try again later.")

# Keep the bot alive
keep_alive()

# Run the bot
bot.run(DISCORD_TOKEN)
