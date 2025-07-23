# Discord Gemini Bot

Ein Discord-Bot, der die Gemini 2.5 Pro KI-Modelle verwendet, um Bilder zu generieren und mit einem Chat-Modell zu interagieren. Der Bot ist so konfiguriert, dass er auf Replit gehostet werden kann.

## Funktionen

- **Bildgenerierung**: Generiert Bilder basierend auf einem Text-Prompt mit Google's Imagen 4 API.
- **Chat-Interaktion**: Interagiert mit dem Gemini 2.5 Pro Chat-Modell basierend auf einem Text-Prompt.
- **Slash-Commands**: Unterstützt benutzerfreundliche Slash-Commands für einfache Interaktion.

## Voraussetzungen

- Python 3.8 oder höher
- Abhängigkeiten aus der Datei `requirements.txt`
- Ein Discord-Bot-Token
- Ein Google API-Schlüssel für die Imagen 4 API

## Installation

1. Klone dieses Repository:
   ```bash
   git clone https://github.com/ScareTix/DiscordGeminiBot.git
   ```

2. Navigiere in das Projektverzeichnis:
   ```bash
   cd DiscordGeminiBot
   ```

3. Installiere die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

4. Erstelle eine `.env`-Datei und füge die Umgebungsvariablen hinzu:
   ```env
   DISCORD_BOT_TOKEN=dein_discord_bot_token
   GOOGLE_API_KEY=dein_google_api_schluessel
   ```

## Nutzung

1. Starte den Bot lokal:
   ```bash
   python bot.py
   ```

2. Lade den Bot auf Replit hoch, um ihn online zu hosten.

## Befehle

### Präfix-Befehle
- `!generate <prompt>`: Generiert ein Bild basierend auf dem Prompt.
- `!chat <prompt>`: Interagiert mit dem Chat-Modell basierend auf dem Prompt.

### Slash-Commands
- `/generate <prompt>`: Generiert ein Bild basierend auf dem Prompt.
- `/chat <prompt>`: Interagiert mit dem Chat-Modell basierend auf dem Prompt.

## Hosting auf Replit

1. Lade die Dateien in ein neues Replit-Projekt hoch.
2. Füge die Umgebungsvariablen in den "Secrets"-Bereich von Replit hinzu.
3. Klicke auf "Run", um den Bot zu starten.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die [LICENSE](LICENSE)-Datei für weitere Details.
