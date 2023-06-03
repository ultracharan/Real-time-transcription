import streamlit as st
import speech_recognition as sr

def transcribe_audio():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        st.write("Speak now...")
        while True:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                st.write(text)
            except sr.UnknownValueError:
                st.write("Sorry, I could not understand audio.")
            except sr.RequestError as e:
                st.write("Sorry, the service is currently unavailable.")

def main():
    st.title("Real-time Transcription")
    start_button = st.button("Start")
    stop_button = st.button("Stop")

    if start_button:
        transcribe_audio()
    if stop_button:
        st.write("Transcription stopped.")

if __name__ == "__main__":
    main()
