import discord
from discord import app_commands
from discord.ext import commands

class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="generate", description="Generiere ein Bild basierend auf einem Prompt")
    async def generate(self, interaction: discord.Interaction, prompt: str):
        await interaction.response.send_message(f"Ein Bild wird generiert für: {prompt}")
        image_url = generate_image(prompt)  # Nutzt die Funktion aus bot.py
        if image_url:
            await interaction.followup.send(f"Hier ist dein Bild: {image_url}")
        else:
            await interaction.followup.send("Bild konnte nicht generiert werden. Bitte versuche es später erneut.")

    @app_commands.command(name="chat", description="Interagiere mit dem Chat-Modell")
    async def chat(self, interaction: discord.Interaction, prompt: str):
        await interaction.response.send_message(f"Frage: {prompt}")
        response = chat_with_gemini(prompt)  # Nutzt die Funktion aus bot.py
        await interaction.followup.send(f"Antwort: {response}")

async def setup(bot):
    await bot.add_cog(SlashCommands(bot))
