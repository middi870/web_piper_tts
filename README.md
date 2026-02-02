# Piper TTS Web Interface

A beautiful web-based interface for Piper Text-to-Speech with support for 200+ voices in 40+ languages!

## Features

- 🎙️ **200+ Voice Models** - Choose from a massive selection of voices
- 🌍 **40+ Languages** - English, Spanish, French, German, Russian, and many more
- 🎯 **Easy to Use** - Simple web interface accessible from any browser
- ⚡ **High Quality** - Multiple quality levels (low, medium, high)
- 🔊 **Real-time Preview** - Listen to generated speech immediately
- 💾 **Download Audio** - Save generated speech as WAV files
- 📱 **Mobile Friendly** - Works on phones, tablets, and computers

## Prerequisites

1. **Python 3.7+**
2. **Piper TTS** - Install from: https://github.com/rhasspy/piper

### Installing Piper

**On Linux:**
```bash
# Download Piper binary
wget https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_amd64.tar.gz
tar -xzf piper_amd64.tar.gz
sudo mv piper/piper /usr/local/bin/
```

**On macOS:**
```bash
# Using Homebrew
brew install piper-tts

# Or download from releases
```

**On Windows:**
Download from: https://github.com/rhasspy/piper/releases

## Installation

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the application:**
```bash
python3 app.py
```

3. **Open your browser:**
Navigate to `http://localhost:5000`

## Usage

1. **Select a Voice** - Choose from the dropdown menu
2. **Enter Text** - Type or paste the text you want to convert
3. **Generate Speech** - Click the "Generate Speech" button
4. **Listen** - The audio will auto-play when ready
5. **Download** - Right-click the audio player to save

## Available Voices by Language

### English (US) - 18 voices
- **Amy** (Female) - Low, Medium
- **Ryan** (Male) - Low, Medium, High ⭐ Recommended
- **Lessac** (Female) - Low, Medium, High
- **LJ Speech** (Female) - Medium, High
- And many more...

### English (UK) - 8 voices
- **Alan** (Male) - Low, Medium
- **Cori** (Female) - Medium, High ⭐ Recommended
- **Alba** (Female) - Medium
- And more...

### Other Major Languages
- **Spanish** (Spain & Mexico) - 6 voices
- **French** - 7 voices
- **German** - 10 voices (including emotional!)
- **Russian** - 4 voices
- **Portuguese** - 3 voices (Brazil & Portugal)
- **Italian** - 2 voices
- **Polish** - 4 voices
- **Turkish** - 3 voices
- And 30+ more languages!

See `PIPER_VOICES_LIST.md` for the complete list.

## Voice Quality Levels

- **x_low** - Fastest, smallest size, basic quality
- **low** - Fast, small size, good quality
- **medium** - Balanced (recommended for most uses)
- **high** - Best quality, larger file size, slower

## Recommended Voices

### Best Overall Quality
1. `en_US-lessac-high` - Crystal clear female voice
2. `en_US-ryan-high` - Natural male voice
3. `en_GB-cori-high` - British female voice

### Best for Speed
1. `en_US-amy-low` - Quick female voice
2. `en_US-danny-low` - Quick male voice

### Unique Features
1. `de_DE-thorsten_emotional-medium` - Expressive German voice
2. `en_US-arctic-medium` - 18 different speakers in one model!
3. `en_US-libritts-high` - 904 different speakers!

## Configuration

### Change Port
Edit `app.py`:
```python
port = 5000  # Change to your preferred port
```

### Voice Model Storage
Voice models are downloaded to:
- Linux/Mac: `~/.local/share/piper/voices/`
- Windows: `%LOCALAPPDATA%\piper\voices\`

Models are downloaded automatically on first use.

## How It Works

1. User selects voice and enters text
2. Flask backend receives the request
3. Voice model is downloaded if not present (first use only)
4. Piper TTS generates audio from text
5. Audio file is sent back to browser
6. User can listen and download

## API Endpoints

### GET `/`
Main interface

### POST `/synthesize`
Generate speech from text

**Request Body:**
```json
{
  "text": "Hello world",
  "voice": "en_US-ryan-medium"
}
```

**Response:**
Audio file (WAV format)

### GET `/voices`
Get list of all available voices

**Response:**
```json
{
  "English (US)": {
    "en_US-ryan-medium": "Ryan (Male, Medium)",
    ...
  }
}
```

## Troubleshooting

### "piper: command not found"
Install Piper TTS (see Prerequisites section)

### Voice model download fails
- Check your internet connection
- Try downloading manually from HuggingFace
- Place models in `~/.local/share/piper/voices/`

### Audio doesn't play
- Check browser compatibility
- Try a different browser (Chrome/Firefox recommended)
- Check browser console for errors

### Slow generation
- Try a lower quality voice (low instead of high)
- Use a smaller model
- Consider running on a more powerful machine

## Performance Tips

- Use `low` or `medium` quality for faster generation
- Cache frequently used voice models
- Run on a machine with good CPU (GPU not required)
- Consider using a smaller voice model for production

## Advanced Usage

### Using from Command Line

```bash
# Generate speech directly
echo "Hello world" | piper \
  --model ~/.local/share/piper/voices/en_US-ryan-medium.onnx \
  --output_file output.wav
```

### Batch Processing

```python
voices = ["en_US-ryan-medium", "en_GB-alan-medium"]
texts = ["Hello", "Goodbye"]

for voice in voices:
    for text in texts:
        text_to_speech(text, voice, f"{voice}_{text}.wav")
```

## Technical Details

- **Backend:** Python Flask
- **TTS Engine:** Piper (ONNX Runtime)
- **Model Format:** ONNX
- **Audio Format:** WAV (16kHz, mono)
- **Model Source:** HuggingFace (rhasspy/piper-voices)

## Contributing

Feel free to:
- Add more voice models
- Improve the UI
- Add new features (speed control, pitch adjustment, etc.)
- Fix bugs

## Resources

- **Piper GitHub:** https://github.com/rhasspy/piper
- **Voice Models:** https://huggingface.co/rhasspy/piper-voices
- **Voice Samples:** https://rhasspy.github.io/piper-samples/

## License

MIT License - Free to use and modify

## Credits

- **Piper TTS** by Rhasspy
- **Voice Models** by various contributors
- **Web Interface** design and implementation

---

**Enjoy creating speech with Piper! 🎙️**
