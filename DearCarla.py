### Modules ###

import os   # Finding terminal size and clearing terminal
import time # For waiting between print functions

### Data ###

SPACE_BETWEEN_LETTERS = 4 # How much horizontal space between letters
LINES_AT_END = 2 # How many blank lines to leave at end (for style and shell prompt)
english_love_letter = [
    "Dear Carla,",
    "",
    "You are the love of my life,",
    "the key to my heart,",
    "and the fuel to my fire.",
    "",
    "I love you with every cell in my body —",
    "from head to toe,",
    "left to right",
    "inside and out.",
    "",
    "My love for you transcends language,",
    "cannot be quantified mathematically,",
    "and will forever overcome any distance between us.",
    "",
    "And every time I say this,",
    "I mean it with all of my heart —",
    "my favourite words of all time:",
    "",
    "I love you Carla Rodde.",
]
german_love_letter = [
    "Liebe Carla,",
    "",
    "Du bist die Liebe meines Lebens,",
    "der Schlüssel zu meinem Herzen",
    "und der Treibstoff für mein Feuer.",
    "",
    "Ich liebe dich mit jeder Zelle meines Körpers —",
    "von Kopf bis Fuß,",
    "von links nach rechts,",
    "innen und außen.",
    "",
    "Meine Liebe zu dir übersteigt jede Sprache,",
    "lässt sich nicht mathematisch ausdrücken",
    "und wird jede Distanz zwischen uns für immer überwinden.",
    "",
    "Und jedes Mal, wenn ich das sage,",
    "meine ich es von ganzem Herzen —",
    "meine liebsten Worte überhaupt:",
    "",
    "Ich liebe dich, Carla Rodde.",
]

### Functions ###

def longest_string(array_of_strings):
    max = 0
    for string in array_of_strings:
        if len(string) > max:
            max = len(string)
    return max

### Main code ###

if len(english_love_letter) != len(german_love_letter):
    print("Please make love letters the same number of lines long :)")
    quit()
letter_linecount = len(english_love_letter)

os.system('clear')  # Clear terminal (macOS and linux only)

# Check and wait until the terminal is sufficiently sized
terminal_size = os.get_terminal_size()
minimum_terminal_width = (
    longest_string(english_love_letter)
    + longest_string(german_love_letter)
    + SPACE_BETWEEN_LETTERS
)
minimum_terminal_height = letter_linecount + LINES_AT_END
if terminal_size.columns < minimum_terminal_width or terminal_size.lines < minimum_terminal_height:
    print("Please make the terminal larger than", minimum_terminal_width, "x", minimum_terminal_height, ":)")
    while True:
        terminal_size = os.get_terminal_size()
        if terminal_size.columns >= minimum_terminal_width and terminal_size.lines >= minimum_terminal_height:
            os.system('clear')
            time.sleep(2)   # Give time to finish terminal resize
            terminal_size = os.get_terminal_size() # Grab final terminal size
            break

# Print letters, character by character, line by line
for line in range(letter_linecount):
    # Print english line
    for char in english_love_letter[line]:
        print(char, end='', flush=True)
        time.sleep(0.05)
    # This finds and prints the number of blank spaces needed at end of each english line
    print(" " * (longest_string(english_love_letter) - len(english_love_letter[line]) + SPACE_BETWEEN_LETTERS),  end='')
    time.sleep(0.1)
    # Print german line
    for char in german_love_letter[line]:
        print(char, end='', flush=True)
        time.sleep(0.05)
    time.sleep(0.1)
    # Prints newline if there is another line after
    if line < letter_linecount - 1:
        print()
input() # Waits for user to press enter
print() # Prints final newline :)
