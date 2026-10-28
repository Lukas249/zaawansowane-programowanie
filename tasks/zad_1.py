def is_palindrome(s: str) -> bool:
    if len(s) == 0:
        return False

    s = s.replace(" ", "")

    i = 0
    j = len(s) - 1

    while i < j and s[i].lower() == s[j].lower():
        i += 1
        j -= 1

    return i >= j
