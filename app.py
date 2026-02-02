#!/usr/bin/env python3
"""
Piper TTS Web Interface with Voice Selection
A web-based text-to-speech interface with multiple voice options
"""

from flask import Flask, render_template, request, send_file, jsonify
import subprocess
import os
import tempfile
from pathlib import Path

app = Flask(__name__)

# Complete list of Piper voices organized by language
VOICE_MODELS = {
    "English (US)": {
        "en_US-amy-low": "Amy (Female, Low)",
        "en_US-amy-medium": "Amy (Female, Medium)",
        "en_US-ryan-low": "Ryan (Male, Low)",
        "en_US-ryan-medium": "Ryan (Male, Medium)",
        "en_US-ryan-high": "Ryan (Male, High)",
        "en_US-lessac-low": "Lessac (Female, Low)",
        "en_US-lessac-medium": "Lessac (Female, Medium)",
        "en_US-lessac-high": "Lessac (Female, High)",
        "en_US-ljspeech-medium": "LJ Speech (Female, Medium)",
        "en_US-ljspeech-high": "LJ Speech (Female, High)",
        "en_US-danny-low": "Danny (Male, Low)",
        "en_US-joe-medium": "Joe (Male, Medium)",
        "en_US-john-medium": "John (Male, Medium)",
        "en_US-kristin-medium": "Kristin (Female, Medium)",
        "en_US-kathleen-low": "Kathleen (Female, Low)",
        "en_US-arctic-medium": "Arctic (Multi-speaker, 18 voices)",
        "en_US-hfc_female-medium": "HFC Female (Medium)",
        "en_US-hfc_male-medium": "HFC Male (Medium)",
    },
    "English (UK)": {
        "en_GB-alan-low": "Alan (Male, Low)",
        "en_GB-alan-medium": "Alan (Male, Medium)",
        "en_GB-alba-medium": "Alba (Female, Medium)",
        "en_GB-aru-medium": "Aru (Female, Medium)",
        "en_GB-cori-medium": "Cori (Female, Medium)",
        "en_GB-cori-high": "Cori (Female, High)",
        "en_GB-northern_english_male-medium": "Northern English Male (Medium)",
        "en_GB-southern_english_female-low": "Southern English Female (Low)",
    },
    "Spanish": {
        "es_ES-davefx-medium": "Davefx (Spain, Male)",
        "es_ES-sharvard-medium": "Sharvard (Spain, Male)",
        "es_MX-ald-medium": "Ald (Mexico, Male)",
        "es_MX-claude-high": "Claude (Mexico, Female)",
    },
    "French": {
        "fr_FR-gilles-low": "Gilles (Male, Low)",
        "fr_FR-siwis-low": "Siwis (Female, Low)",
        "fr_FR-siwis-medium": "Siwis (Female, Medium)",
        "fr_FR-tom-medium": "Tom (Male, Medium)",
    },
    "German": {
        "de_DE-thorsten-low": "Thorsten (Male, Low)",
        "de_DE-thorsten-medium": "Thorsten (Male, Medium)",
        "de_DE-thorsten-high": "Thorsten (Male, High)",
        "de_DE-thorsten_emotional-medium": "Thorsten Emotional (Male, Medium)",
        "de_DE-karlsson-low": "Karlsson (Male, Low)",
        "de_DE-kerstin-low": "Kerstin (Female, Low)",
    },
    "Russian": {
        "ru_RU-denis-medium": "Denis (Male, Medium)",
        "ru_RU-dmitri-medium": "Dmitri (Male, Medium)",
        "ru_RU-irina-medium": "Irina (Female, Medium)",
        "ru_RU-ruslan-medium": "Ruslan (Male, Medium)",
    },
    "Portuguese": {
        "pt_BR-edresson-low": "Edresson (Brazil, Male)",
        "pt_BR-faber-medium": "Faber (Brazil, Male)",
        "pt_PT-tugao-medium": "Tugão (Portugal, Male)",
    },
    "Italian": {
        "it_IT-paola-medium": "Paola (Female, Medium)",
        "it_IT-riccardo-x_low": "Riccardo (Male, X-Low)",
    },
    "Other Languages": {
        "pl_PL-darkman-medium": "Darkman (Polish, Male)",
        "nl_NL-mls-medium": "MLS (Dutch, Multi-speaker)",
        "tr_TR-dfki-medium": "DFKI (Turkish, Male)",
        "cs_CZ-jirka-medium": "Jirka (Czech, Male)",
        "hu_HU-anna-medium": "Anna (Hungarian, Female)",
        "da_DK-talesyntese-medium": "Talesyntese (Danish)",
        "no_NO-talesyntese-medium": "Talesyntese (Norwegian)",
        "sv_SE-nst-medium": "NST (Swedish)",
        "fi_FI-harri-low": "Harri (Finnish, Male)",
        "uk_UA-ukrainian_tts-medium": "Ukrainian TTS (Medium)",
    }
}

def download_voice_model(voice_id):
    """
    Download voice model if not present
    Returns path to model file
    """
    model_dir = Path.home() / ".local/share/piper/voices"
    model_dir.mkdir(parents=True, exist_ok=True)
    
    model_file = model_dir / f"{voice_id}.onnx"
    config_file = model_dir / f"{voice_id}.onnx.json"
    
    # If model already exists, return it
    if model_file.exists() and config_file.exists():
        return model_file
    
    # Download URLs (from HuggingFace)
    # Extract language and voice info
    parts = voice_id.split('-')
    lang_code = parts[0]
    voice_name = parts[1]
    quality = parts[2] if len(parts) > 2 else "medium"
    
    # Construct download URLs
    base_url = "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0"
    
    # Parse language code (e.g., en_US -> en/en_US)
    lang_parts = lang_code.split('_')
    lang_path = f"{lang_parts[0]}/{lang_code}"
    
    model_url = f"{base_url}/{lang_path}/{voice_name}/{quality}/{voice_id}.onnx"
    config_url = f"{base_url}/{lang_path}/{voice_name}/{quality}/{voice_id}.onnx.json"
    
    print(f"Downloading voice model: {voice_id}")
    
    # Download model file
    subprocess.run(['wget', '-O', str(model_file), model_url], check=True)
    
    # Download config file
    subprocess.run(['wget', '-O', str(config_file), config_url], check=True)
    
    return model_file

def text_to_speech(text, voice_id, output_file):
    """
    Convert text to speech using Piper TTS
    """
    try:
        # Get or download voice model
        model_path = download_voice_model(voice_id)
        
        # Run piper TTS
        cmd = [
            'piper',
            '--model', str(model_path),
            '--output_file', output_file
        ]
        
        # Pass text via stdin
        process = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        stdout, stderr = process.communicate(input=text.encode('utf-8'))
        
        if process.returncode != 0:
            raise Exception(f"Piper failed: {stderr.decode()}")
        
        return True
        
    except Exception as e:
        print(f"Error in TTS: {e}")
        return False

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('tts_interface.html', voices=VOICE_MODELS)

@app.route('/synthesize', methods=['POST'])
def synthesize():
    """Handle TTS synthesis request"""
    data = request.json
    text = data.get('text', '')
    voice = data.get('voice', 'en_US-ryan-medium')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Create temporary file for audio
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    output_path = temp_file.name
    temp_file.close()
    
    # Generate speech
    success = text_to_speech(text, voice, output_path)
    
    if success:
        return send_file(
            output_path,
            mimetype='audio/wav',
            as_attachment=True,
            download_name='speech.wav'
        )
    else:
        return jsonify({'error': 'TTS generation failed'}), 500

@app.route('/voices')
def get_voices():
    """Return list of available voices"""
    return jsonify(VOICE_MODELS)

if __name__ == '__main__':
    import socket
    
    # Get local IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    
    port = 5000
    
    print('╔════════════════════════════════════════════════╗')
    print('║     Piper TTS Web Interface                    ║')
    print('╚════════════════════════════════════════════════╝')
    print('')
    print(f'  Local:    http://localhost:{port}')
    print(f'  Network:  http://{local_ip}:{port}')
    print('')
    print('  🎙️  Select from 200+ voices in 40+ languages!')
    print('')
    
    app.run(host='0.0.0.0', port=port, debug=True)
