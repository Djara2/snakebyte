from rich.console import Console
from rich.prompt import Prompt
import display_tools as dt
import math

console = Console()

"""Color schemes for prettier UI when using console.print() method"""
MENU_HEADER_SCHEME = "white on bright_black"
MENU_ITEM_SCHEME = "black on grey78"
PROMPT_SCHEME = "white on dark_orange3"
POSITIVE_SCHEME = "white on yellow4"
WARNING_SCHEME = "black on yellow"
CRITICAL_SCHEME = "white on red"

def print_warning(text: str):
    """
    Prints black text against a yellow background, indicating a warning.

    Keyword arguments:
    text -- the warning text to be displayed
    """
    console.print(f"[{WARNING_SCHEME}]{text}[/]")

def print_critical(text: str):
    """
    Prints white text against a red background, indicating a critical warning.

    Keyword arguments:
    text -- the critical warning text to be displayed
    """
    console.print(f"[{CRITICAL_SCHEME}]{text}[/]")

def prompt(text: str) -> str:
    """
    Prompts the user for input, with white text against an orange background for prompt text.

    Keyword arguments:
    text -- the prompt text to be displayed
    """
    user_input = Prompt.ask(f"[{PROMPT_SCHEME}]{text}[/]")
    return user_input
    
def get_longest_string(array) -> int:
    """
    Determines and returns the  length of the longest string in an array.

    Keyword arguments:
    array -- the list of strings to be operated on.
    """
    length = -1
    for item in array:
        if len(item) > length:
            length = len(item)
    return length

def center_print(text):
    terminal_rows = dt.get_terminal_rows()
    terminal_columns = dt.get_terminal_columns()
    longest_len = get_longest_string(text)
    div = "━" * longest_len
    total_blank_space = terminal_columns - longest_len
    if total_blank_space % 2 == 0:
        left_blank_space = total_blank_space // 2
        right_blank_space = total_blank_space // 2
    else:
        left_blank_space = math.floor(total_blank_space / 2)
        right_blank_space = total_blank_space + 1
    
    print("\n\n\n")
    x = 0
    for line in text:
        if x == 0:
            console.print(f"{' ' * left_blank_space}[dark_orange]{line}[/]")
            console.print(f"{' ' * left_blank_space}{div}")
        else:
            console.print(f"{' ' * left_blank_space}{line}")
        x += 1
    return left_blank_space
    