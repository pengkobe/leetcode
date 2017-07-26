def is_match(string, pattern):
    if not string and not pattern:
        return True
    
    # `*` match blank string 
    if not string and not pattern.replace('*', ''):
        return True

    if not pattern or not string:
        return False

    if pattern[0] == '*':
        return is_match(string[1:], pattern) or is_match(string, pattern[1:])
    else:
        if pattern[0] != string[0]:
            if pattern[0] != '.':
                return False
        return is_match(string[1:], pattern[1:])
    

if __name__ == '__main__':
    assert is_match('aa', 'a') == False
    assert is_match('aa', 'aa') == True
    assert is_match('aaa', 'aaa') == True
    assert is_match('aaa', '.a') == False
    assert is_match('aa', '.*') == True
    assert is_match('aab', '*') == True
    assert is_match('b', '.*.') == False