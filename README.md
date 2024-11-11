# Discord TTS Bot

A Discord bot that reads messages from a text channel and outputs them as audio in a voice channel. Useful for friends who don't have access to a microphone but would like an easier/better way to communicate in voice channels.

This bot supports two modes:
1. **Discord's Built-in TTS**
2. **ElevenLabs API TTS** for a custom AI-generated voice

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Running the Bot](#running-the-bot)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
- [License](#license)

## Features

- Connects to a specified text channel to read messages and outputs audio in a voice channel.
- Two TTS options:
  - Discord's built-in TTS.
  - ElevenLabs API TTS for a custom AI-generated voice.

## Requirements

- Python 3.8 or higher
- Discord Bot Token
- ElevenLabs API Key (if using ElevenLabs TTS)

## Setup

1. **Clone this repository** to your local machine:

   ```bash
   git clone <repository-url>
   cd <repository-name>
