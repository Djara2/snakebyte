def try_str_to_int(string) -> bool:
    try:
        string = int(string)
        return True
    except:
        return False

def index_in_bounds(index: int, array: list) -> bool:
    if index >= 0:
        if index < len(array):
            return True
        else:
            return False
    else:
        return False

def item_in_list(item, array):
    if item in array:
        return True
    else:
        return False

def check_safe_str(item: str):
    if type(item) == type("str"):
        if len(item) >= 1:
            if not "\\" in item:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

