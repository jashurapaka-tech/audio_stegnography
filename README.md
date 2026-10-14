# Advanced Audio Steganography

Educational desktop application for password-protected LSB audio steganography.

## Run

```powershell
python -m pip install -r requirements.txt
python main.py
```

Use WAV or FLAC only. Re-encoding the resulting file as MP3 can destroy the embedded data.

## Security notes

Messages are encrypted with AES-256-GCM and a PBKDF2-HMAC-SHA256-derived key. The application does not store passwords, messages, or encryption keys in activity logs. Use only with authorization and in compliance with applicable laws.

## Packaging

On each target operating system, install dependencies and run:

```powershell
pyinstaller --noconsole --name AdvancedAudioSteganography --add-data "assets;assets" main.py
```

Build executables separately on Windows, Linux, and macOS.
