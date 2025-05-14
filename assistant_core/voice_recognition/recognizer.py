import pyaudio
import speech_recognition as sr

# Parameters for recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS =

p = pyaudio.PyAudio()

# Open the microphone stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

def recognize_audio():
    """
    Recognize speech from live microphone input using the SpeechRecognition library.
    """
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    audio_data = b''.join(frames)

    # Convert the byte data to an AudioData object (speech_recognition needs this)
    audio_buffer = sr.AudioData(audio_data, RATE, 2)  # 2 represents 16-bit (2 bytes per sample)

    try:
        print("Recognizing...")
        transcript = recognizer.recognize_google(audio_buffer)
        return transcript
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

if __name__ == "__main__":
    recognize_audio()
