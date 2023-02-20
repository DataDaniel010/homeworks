def k_isalpha(s: str) -> bool:
    i = len(s) - 1
    result = True
    while i != -1:
        if 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122:
            pass
        else:
            result = False
            break
        i -= 1
    return result

def k_islower(s: str) -> bool:
    i = len(s) - 1
    result = True
    if s.isdigit() == False:
        while i != -1:
            if  65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122:
                if 65 <= ord(s[i]) <= 90:
                    result = False
                    break             
            i -= 1
    else:
        result = False
    return result

def k_istitle(s: str) -> bool:
    s = s.strip()
    i = len(s) - 1
    result = True
    if 65 <= ord(s[0]) <= 90:
        while i != 0:
            if 65 <= ord(s[i]) <= 90:
                result = False
                break
            i -= 1
    else:
        result = False
    return result

def k_upper(s: str) -> str:
    i = 0
    word = ''
    a = 0    
    while i < len(s):
        if 65 <= ord(s[i]) <= 90:
            word += s[i]                
        if 97 <= ord(s[i]) <= 122:
            a = ord(s[i]) - 32
            word += chr(a)
        if not 65 <= ord(s[i]) <= 90 and not 97 <= ord(s[i]) <= 122:
            word += s[i]
        i += 1
    return word

def k_endswith(s: str, substring: str) -> bool:
    if s[len(s) - len(substring)::] == substring:
        return True
    else:
        return False 
