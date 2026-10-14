@echo off
pyinstaller --noconsole --name AdvancedAudioSteganography --add-data "assets;assets" --icon assets\app.ico main.py
