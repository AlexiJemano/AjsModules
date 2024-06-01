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

