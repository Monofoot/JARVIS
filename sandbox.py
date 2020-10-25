import speech_recognition as sr # speech recognition
import pyttsx3 # text-to-speech



class Jarvis:
    """
    TO-DO:
    Activation function
    Implement error catching with an exception file,
    make Jarvis say the errors
    """

    def __init__(self):
        """
        """
        
        self.set_engine_properties()
    
    def set_engine_properties(self):
        """
        Properties for the voice engine.
        """

        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', 'voices[1].id')
    
    def say(self, text):
        """
        Initial testing rig for speech.
        """
        
        self.engine.say(text)
        self.engine.runAndWait()
    
    def process_command(self):
        """
        """

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

            try:
                statement=r.recognize_google(audio, language='en-in')
                print(f"user said: {statement}\n")
            
            except Exception as e:
                self.say("Didn't catch that")
                return "None"
        return statement

if __name__ == "__main__":
    JARVIS = Jarvis()
    command = JARVIS.process_command()
    JARVIS.say(command)
