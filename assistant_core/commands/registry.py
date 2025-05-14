command_registry = {}  # Dictionary to hold command functions
def register_command(name: str):
    """
    A decorator to register a command function.
    - `name`: The name of the command (e.g., 'mute_discord')
    """
    def wrapper(func):
        command_registry[name] = func  # Register the function in the command registry
        return func
    return wrapper



def execute_command(command_name: str, *args):
    """
    Executes a registered command by name.
    - `command_name`: The name of the command to execute (e.g., 'mute_discord')
    - `*args`: Arguments passed to the command function (if any)

    If no command is found, return an error message.
    """
    command = command_registry.get(command_name)
    if command:
        command(*args)  # Call the command handler
    else:
        print(f"⚠️ Command '{command_name}' not found!")