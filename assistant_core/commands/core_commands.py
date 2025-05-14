from .registry import register_command
import pyautogui
import pyttsx3

engine = pyttsx3.init()
is_muted = False


def speak(text: str):
    print(text)
    engine.say(text)
    engine.runAndWait()

@register_command("mute_discord")
def mute_discord():
    """
    Command to mute Discord.
    """
    global is_muted
    if is_muted:
        speak("Discord is already muted.")
        return
    speak("Muting Discord...")
    pyautogui.hotkey('f10')  # TODO: remind user to set the hotkey to F10
    is_muted = True

@register_command("unmute_discord")
def unmute_discord():
    """
    Command to unmute Discord.
    """
    global is_muted
    if not is_muted:
        speak("Discord is already unmuted.")
        return
    speak("Unmuting Discord...")
    pyautogui.hotkey('f10')
    is_muted = False