from .registry import register_command
import pyautogui

@register_command("mute_discord")
def mute_discord():
    """
    Command to mute Discord.
    """
    print("🔇 Muting Discord...")
    pyautogui.hotkey('f10')  # TODO: remind user to set the hotkey to F10

@register_command("unmute_discord")
def unmute_discord():
    """
    Command to unmute Discord.
    """
    print("🔊 Unmuting Discord...")
    pyautogui.hotkey('f10')