# Voice-to-Hinglish Translator

This Python script is designed to take voice input from the user, translate it from English to Hinglish (a combination of Hindi and English), and save the translated text as an audio file. It uses various libraries and a pre-trained model to accomplish this task.

## Prerequisites

Before using this script, make sure you have the following libraries installed:
- [torch](https://pytorch.org/) (PyTorch)
- [transformers](https://huggingface.co/transformers/) (Hugging Face Transformers)
- [speech_recognition](https://pypi.org/project/SpeechRecognition/) (SpeechRecognition)
- [gtts](https://pypi.org/project/gTTS/) (gTTS)

You can install these libraries using pip:
```bash
pip install torch transformers SpeechRecognition gtts
```

## Usage

1. Run the script `voice_to_hinglish_translator.py`.

2. The script will initialize the microphone and ask you to say something.

3. After speaking, it will transcribe your speech to text using the Google Web Speech API.

4. If your speech is successfully transcribed, it will then translate the English text into Hinglish using a pre-trained model.

5. The translated Hinglish text will be converted into an audio file (MP3 format) and saved as "output.mp3" in the same directory as the script.

6. The script will display both the original English text and the translated Hinglish text.

## Troubleshooting

- If you encounter any issues with the speech recognition, ensure that your microphone is properly connected and that you have a working internet connection for the Google Web Speech API.

- If the translation results are not accurate, you can experiment with different pre-trained models and fine-tune them for your specific use case.

- Make sure your system's audio output is working so that you can hear the generated audio.

## Acknowledgments

This script utilizes the power of the Hugging Face Transformers library and the Google Web Speech API for speech recognition.

## Disclaimer

This script relies on external services and pre-trained models, and its performance may vary depending on the quality of your microphone, your internet connection, and the accuracy of the translation model. Use it responsibly and ensure compliance with any applicable terms of service for the services used.
