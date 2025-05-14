import speech_recognition as sr
from commands.registry import execute_command, command_registry

WAKE_WORD = "ghost"

def recognize_audio_loop():
    """
    Continuously listens to the microphone and processes detected speech in a loop.
    Stops only with a KeyboardInterrupt (Ctrl+C).
    """
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print(f"🎤 Voice assistant is running. To speak say {WAKE_WORD} ... (Press Ctrl+C to stop)")

        while True:
            try:
                audio = recognizer.listen(source)

                transcript = recognizer.recognize_google(audio)
                if WAKE_WORD in transcript.lower():
                    process_transcript(transcript)

            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                print(f"⚠️ API error: {e}")


def process_transcript(transcript: str):
    """
    Match the transcript with commands and execute them.
    """
    if not transcript:
        print("❌ No transcript available.")
        return

    print(f"👂 Heard: {transcript}")
    matched_command = None

    # Sort commands by length (descending) to prioritize more specific matches
    for command in sorted(command_registry.keys(), key=lambda x: -len(x)):
        command_phrase = command.replace("_", " ")
        if command_phrase in transcript.lower():
            matched_command = command
            break
        elif command in transcript.lower().replace(" ", "_"):
            matched_command = command
            break

    if matched_command:
        print(f"✅ Recognized command: {matched_command}")
        execute_command(matched_command)
    else:
        print("❌ No known command matched.")

if __name__ == "__main__":
    recognize_audio()
