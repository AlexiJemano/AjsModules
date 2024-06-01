# AjsModules - A Collection of usefull small thinks to make your code better

To install please use:
```angular2html
pip install -i https://test.pypi.org/simple/ AjsModules
```

A complete list of small things in this modules:

- ```from AjsModules import typewriter```: \
   makes a cool type writing effect \
   ```sh
    message = "This is another message with a typewriter effect."
    typewriter(message, type_delay=0.2, newline_delay=2)  # Adjust delays as needed
   ```
-  ```from AjsModules import colored_message```: \
   ability to manipulate text color: 
   ```sh
   my_message = "This is a message from a variable (green)!"
   colored_message(my_message, color=fg.GREEN)
   ```
   or other example of the usage: \
   ```sh
   colored_message("This is a bold message (green)!", color=fg.GREEN, style="1")  # Bold
   colored_message("This is a dimmed message (red).", color=fg.RED, style="2")  # Less bright
   colored_message("This is underlined (blue) and bold.", color=fg.BLUE, style="4;1")  # Underline and bold
   colored_message("This is inverted (white on black).", color=fg.WHITE, style="7")  # Swap foreground and background
   ```