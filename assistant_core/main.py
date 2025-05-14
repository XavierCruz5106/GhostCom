from voice_recognition.recognizer import recognize_audio
from commands.registry import execute_command
from commands import core_commands


# Simulating voice recognition
def process_transcript(transcript: str):
    """
    Match the transcript with commands and execute them.
    """
    # TODO: Implement command matching logic
    # For now, just print the transcript
    print(f"👂 Heard: {transcript}")
    execute_command("mute_discord")

def main():

    # Start listening for audio and process it
    print("🎙️ Starting voice detection...")
    transcript = recognize_audio()  # Listen to microphone or audio file
    process_transcript(transcript)

if __name__ == "__main__":
    main()