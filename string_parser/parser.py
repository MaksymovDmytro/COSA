def func(s: str, k: int) -> str:
    """
    Given a string s, this function finds k most frequent characters in this string.
    The function returns the characters joined into another string, sorted by their
    frequency (descending order) and for the characters with equal frequency - in alphabetical order.
    Uppercase and lowercase letters are treated as the same letters. White-spaces are ignored.
    """
    # Making sure s is not an empty string
    if not s or not k:
        return ''
    elif k < 1:
        return ''
    try:
        # Removing anything but alphabetic in s
        s = [char.lower() for char in s.strip() if char.isalpha()]
    except (TypeError, AttributeError):
        return ''
    # 2) Sorting string by letter quantity, descending
    sorted_s = sorted(
        # 1) Sorting string alphabetically
        sorted(s),
        key=lambda x: s.count(x), reverse=True)
    dist_chars = set()
    try:
        # Return list of distinct letters.
        return ''.join([char for char in sorted_s
                        # if letter is not yet added to dist_chars then add it (set.add() always returns None)
                        if char not in dist_chars and not dist_chars.add(char)]
                       # return only first k letters.
                       [:int(k)])
    except (TypeError, AttributeError):
        return ''
