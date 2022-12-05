import os

def get_terminal_dimensions():
    return os.get_terminal_size()

def get_terminal_columns():
    return os.get_terminal_size().columns

def get_terminal_rows():
    return os.get_terminal_size().lines

def box_print(text, header = None):
    out = f"║ {text} ║"
    if header != None:
        left = f"╔══ {header} "
        count = len(out) - len(f"{left} ")
        straight = '═' * count 
        print(f"\n╔══ {header} {straight}╗")
    else:
        print(f"\n╔{'═' * (len(out) - 2)}╗")
    print(f"║{' ' * (len(out) - 2)}║")
    print(f"{out}")
    print(f"║{' ' * (len(out) - 2)}║")
    print(f"╚{'═' * (len(out) - 2)}╝")

def dictionary_print(dictionary):
    for key in dictionary.keys():
        print(f"{key}: {dictionary[key]}\n")


# use this to make a block of text (within a line, like a subline) that is formatted to have the text you want, but such that it fits within a certain amount of space 
# e.g. consider for a 2 column print f"{make_label(artist1)} | {make_label(artist2)}" -- if you pass in allowed_space as being perfect divisions of get_terminal_columns, then these will always align and look good
def make_label(text, allowed_space, list_number):
	if list_number != None:
		label = f"{list_number}. {text}"
	else:
		label = text
	
	if len(label) >= allowed_space:
		label = label[:allowed_space - 6]
		label += "..."
	
	if len(label) < allowed_space:
		white_space = " " * allowed_space - len(label)
		label += white_space
	
	return label


def two_column_print(t1, t2, divider = " ", indent = True):
    terminal_columns = get_terminal_columns()
    c1 = []
    c2 = []
    full_line = ""
    flags = {
            "c1 overflow": False,
            "c2 overflow": False
            }
    if terminal_columns % 2 == 0:
        """
        - if there is an even amount of columns then we have columns-1 space to display text.
            - why? Because the divider takes up 1 space.
            - we give (1/2) - 1 space to c1 on the right
                - minus one extra space to add whitespace padding from the divider
            - and we give (1/2)-2 space to c2 on the left
                - minus 2 extra space to add whitespace padding
            - this leaves us with 1 extra space for the divider, and 2 spaces for whitespace padding
                - (0.5x - 1) + (0.5x - 2) + 3 = 0.5x + 0.5x - 3 + 3 = x
                    - where x is the amount of terminal columns
        """
        c1_allocated_space = (terminal_columns // 2) - 1
        c2_allocated_space = (terminal_columns //2) - 2
        if c1_allocated_space >= len(t1):
            c1.append(t1)
            if c1_allocated_space > len(t1):
                white_space_count = c1_allocated_space - len(t1)
                white_spaces = " " * white_space_count
                c1.append(white_spaces)
        else:
            start = 0
            end = c1_allocated_space
            while end <= len(t1):
                c1.append(t1[start:end])
                start = end
                end = end * 2
                if end > len(t1) and start < len(t1):
                    remaining_characters = len(t1) - start
                    if c1_allocated_space >= remaining_characters:
                        c1.append(t1[start:start + remaining_characters])
                    else:
                        end = start + c1_allocated_space


        if c2_allocated_space >= len(t2):
            c2.append(t2)
            if c2_allocated_space > len(t2):
                white_space_count = c2_allocated_space - len(t2)
                white_spaces = " " * white_space_count
                c2.append(white_spaces)
        else:
            start = 0
            end = c2_allocated_space
            while end <= len(t2):
                c2.append(t2[start:end])
                start = end
                end = end * 2
                if end > len(t2) and start < len(t2):
                    remaining_characters = len(t2) - start
                    if c2_allocated_space >= remaining_characters:
                        c2.append(t2[start:start + remaining_characters])
                    else:
                        end = start + c2_allocated_space

    upper_bound = max(len(c1), len(c2))
    lower_bound = min(len(c1), len(c2))

    for x in range(upper_bound):
        line = ""
        if x < len(c1):
            line += f"{c1[x]} | "
            if x > len(c2):
                line += " " * c2_allocated_space

        if x < len(c2):
            if x < len(c1):
                line += f"{c2[x]}"
            else:
                line = f"{' ' * c1_allocated_space} | {c2[x]}"
        print(line)


def two_column_print_neo(t1, t2):

    terminal_columns = get_terminal_columns()
    c1_space = (terminal_columns // 2) - 1
    c2_space = (terminal_columns // 2) - 2
    divider = " | "
    div_len = len(divider)

    t1_list = t1.split(" ")
    t2_list = t2.split(" ")




def test(t1, t2):
    os.system("cls")
    two_column_print_neo(t1, t2)

t1 = "This is some text that I am hoping is longer than 59 characters. I need it to be longer than 59 characters so thatI can cause an overflow of the column to ensure that it works properly. Now I am adding even more text. It is certainly over the size. I want to see what happens if I just absolutely load this with text. I want to see what the computer algorithm I wrote does."

t2 = "This is some text that I am hoping is close to but less than 58 characters"

test(t1, t2)
