import time
import sys

def typewriter(message, type_delay=0.1, newline_delay=1):
  """
  Simulates a typewriter effect by printing characters one by one with delays.

  Args:
      message (str): The message to be typed.
      type_delay (float, optional): The delay between characters in seconds. Defaults to 0.1.
      newline_delay (float, optional): The delay after newlines in seconds. Defaults to 1.
  """

  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()

    if char != "\n":
      time.sleep(type_delay)
    else:
      time.sleep(newline_delay)

  # colored_message.py

# colored_message.py

def colored_message(message, color=None, style=None):
    """
    Prints a message with optional foreground color and style.

    Args:
        message (str): The message to print. Can be a variable containing the text.
        color (str, optional): The foreground color code from the `fg` class (e.g., `fg.GREEN`). Defaults to None (no color).
        style (str, optional): The style code from the `style` class (e.g., `style.BRIGHT`). Defaults to None (no style).

    Returns:
        None
    """

    # Import ANSI escape codes if not already imported
    try:
        from colorama import Fore, Style
    except ImportError:
        # Fallback to using ANSI escape codes directly
        import os
        if os.name == 'nt':
            # Windows compatibility (avoid colorama dependency)
            import ctypes
            windll = ctypes.WinDLL('kernel32')
            SetConsoleTextAttribute = windll.SetConsoleTextAttribute
            HANDLE = ctypes.windll.kernel32.GetStdHandle(-11)
            FOREGROUND_BLACK = 0x0000
            FOREGROUND_RED = 0x0C00
            FOREGROUND_GREEN = 0x0A00
            FOREGROUND_BLUE = 0x0900
            FOREGROUND_INTENSITY = 0x0800  # Adjust for bright colors
            colors = {
                'BLACK': FOREGROUND_BLACK,
                'RED': FOREGROUND_RED | FOREGROUND_INTENSITY,
                'GREEN': FOREGROUND_GREEN | FOREGROUND_INTENSITY,
                'YELLOW': (FOREGROUND_RED | FOREGROUND_GREEN) | FOREGROUND_INTENSITY,
                'BLUE': FOREGROUND_BLUE | FOREGROUND_INTENSITY,
                'MAGENTA': (FOREGROUND_RED | FOREGROUND_BLUE) | FOREGROUND_INTENSITY,
                'CYAN': (FOREGROUND_GREEN | FOREGROUND_BLUE) | FOREGROUND_INTENSITY,
                'WHITE': FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE,
            }
            def set_color(code):
                SetConsoleTextAttribute(HANDLE, colors[code])
        else:
            # Use ANSI escape codes for other platforms
            def set_color(code):
                print(f"\033[{colors[code]}m{message}\033[0m")  # ANSI escape sequences directly
    else:
        # Use colorama for convenient color and style options
        def set_color(code):
            print(f"{Fore.__dict__[color]}{Style.__dict__[style]}{message}{Style.RESET_ALL}")

    # Set the color and print the message
    if color:
        set_color(color)
        print(message)
    else:
        print(message)


