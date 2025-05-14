from voice_recognition.recognizer import recognize_audio
from commands.registry import execute_command, command_registry
from commands import core_commands


# Simulating voice recognition
def process_transcript(transcript: str):
    """
    Match the transcript with commands and execute them.
    """
    print(f"👂 Heard: {transcript}")
    matched_command = None
    for command in command_registry.keys():
        if command.replace("_", " ") in transcript.lower():
            matched_command = command
            break
        # Extra: fuzzy match just in case
        elif command in transcript.lower().replace(" ", "_"):
            matched_command = command
            break

    if matched_command:
        print(f"✅ Recognized command: {matched_command}")
        execute_command(matched_command)
    else:
        print("❌ No known command matched.")

def main():

    # Start listening for audio and process it
    print("🎙️ Starting voice detection...")
    transcript = recognize_audio()  # Listen to microphone or audio file
    process_transcript(transcript)

if __name__ == "__main__":
    main()