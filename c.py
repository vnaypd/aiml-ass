import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import speech_recognition as sr
from gtts import gTTS

def take_voice_input():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen to the microphone

    try:
        # Recognize the speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
        return ""

def translate_to_hinglish(english_text):
    # Load the pre-trained model and tokenizer
    model_name = "Helsinki-NLP/opus-mt-en-hi"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # Tokenize and translate the input text
    inputs = tokenizer(english_text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model.generate(**inputs)

    # Decode the translated output
    hinglish_translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return hinglish_translation

if __name__ == "__main__":
     voice_input = take_voice_input()
     if voice_input:
        hinglish_translation=translate_to_hinglish(voice_input)
     print(f"English: {voice_input}")
     
     tts = gTTS(text=hinglish_translation, lang='hi')
     tts.save("output.mp3")
     print("Audio file 'output.mp3' has been created.")
     print(f"Hinglish: {hinglish_translation}")
