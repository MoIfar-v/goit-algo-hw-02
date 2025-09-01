from collections import deque




def palindrome_check(word):
    word_normal = deque()
    word_reverse = deque()
    
    message = f'Слово "{word}" є паліндромом'
    
    word_normal.extend(word.lower())
    word_reverse.extendleft(word.lower())
    
    if word_normal != word_reverse:
        message = f'Слово "{word}" не є паліндромом'
    return message

assert palindrome_check("level") == f'Слово "level" є паліндромом'
assert palindrome_check("Madam") == f'Слово "Madam" є паліндромом' 
assert palindrome_check("12321") == f'Слово "12321" є паліндромом'

assert palindrome_check("python") == f'Слово "python" не є паліндромом'
assert palindrome_check("palindrome") == f'Слово "palindrome" не є паліндромом'


word = input("Будь ласка введіть слово: ")


print(palindrome_check(word))