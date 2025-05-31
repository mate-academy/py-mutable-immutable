from cmath import phase


def count_occurrences(phrase: str, letter: str) -> int:

    lower_phrase = phrase.lower() # zamienia duze litery w slownei na male
    lower_letter = letter.lower() # zamienia duze na male litery

    return(lower_phrase.count(lower_letter))


letter = 'd'
phrase = 'ABC'
print(count_occurrences(phrase, letter))