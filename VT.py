import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

def voice_typing(language):
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening for your voice...")
            audio = recognizer.listen(source)

            try:
                # Recognize speech using Google Web Speech API with the specified language
                print("Processing audio...")
                text = recognizer.recognize_google(audio, language=language)
                print("You said: " + text)
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError:
                print("Could not request results; check your network connection.")
    except KeyboardInterrupt:
        print("\nExiting gracefully...")

if __name__ == "__main__":
    # Ask the user for the language they will speak
    print("Available languages: 'en' (English), 'es' (Spanish), 'fr' (French), 'de' (German), etc.")
    speak_language = input("Enter the language code you will speak in (default is 'en' for English): ").strip()
    if not speak_language:
        speak_language = 'en'  # Default to English if no input is provided

    # Ask the user for the language they want to use for speech recognition
    print("Available recognition languages: 'en' (English), 'es' (Spanish), 'fr' (French), 'de' (German), etc.")
    recognize_language = input("Enter the language code for speech recognition (default is 'en' for English): ").strip()
    if not recognize_language:
        recognize_language = 'en'  # Default to English if no input is provided
    
    print(f"Will recognize speech in {recognize_language} and you will speak in {speak_language}.")
    voice_typing(recognize_language)
