from morph_rules import vowels
from morph_rules import consonants
from morph_rules import voiceless_consonant
from morph_rules import add_affix_choosing_hard_or_soft


def generate_adjective_forms(word_and_tags: tuple) -> list:
    """функция, генерирующая все формы для прилагательного
    """
    result = []
    result += generate_comparative_adjective(word_and_tags)
    result += generate_superlative_adjective(word_and_tags)

    return result


def generate_comparative_adjective(word_and_tags: tuple) -> list:
    """функция, генерирующая 2 варианта сравнительной степени прилагательного
    -рақ /-рек
    -ырақ /-iрек
    или
    -лау/-леу
    -дау/-деу
    """
    word, tags = word_and_tags
    result = []

    # -рақ /-рек
    # -ырақ /-iрек
    if (word[-1] in vowels):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="рақ",
                                                   soft_affix="рек")
    elif (word[-1] in consonants):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="ырақ",
                                                   soft_affix="iрек")
    new_tags = tags.copy()
    new_tags["degree_of_comparison"] = "<comp>"
    result.append((new_word, new_tags))

    # -лау/-леу
    # -дау/-деу
    # -тау/-теу
    if (word[-1] in vowels) \
            or (word[-1] in ('р', 'й', 'у')):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="лау",
                                                   soft_affix="леу")

    elif word[-1] in ('м', 'н', 'ң', 'л', 'з'):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="дау",
                                                   soft_affix="деу")

    elif (word[-1] in voiceless_consonant) \
            or (word[-1] in ('б', 'в', 'г', 'д')):
        new_word = add_affix_choosing_hard_or_soft(word,
                                                   hard_affix="тау",
                                                   soft_affix="теу")
    new_tags = tags.copy()
    new_tags["degree_of_comparison"] = "<comp>"
    result.append((new_word, new_tags))

    return result


def generate_superlative_adjective(word_and_tags: tuple) -> list:
    """функция, генерирующая превосходную степень прилагательного

    Удвоение начального слога:
    Жап – жақсы (весьма хорошо)

    Исключение :
    Аппақ – очень белый
    Көкпенбек – очень синий
    """
    word, tags = word_and_tags
    result = []

    if word == "ақ":
        new_word = "аппақ"
        new_tags = tags.copy()
        new_tags["degree_of_comparison"] = "<sup>"
        result.append((new_word, new_tags))
        return result
    if word == "көк":
        new_word = "көкпенбек"
        new_tags = tags.copy()
        new_tags["degree_of_comparison"] = "<sup>"
        result.append((new_word, new_tags))
        return result

    # Удвоение начального слога:
    # Жап – жақсы (весьма хорошо)
    first_vowel = 0
    while word[first_vowel] not in vowels:
        first_vowel += 1

    new_word = word[:first_vowel + 1] + "п-" + word
    new_tags = tags.copy()
    new_tags["degree_of_comparison"] = "<sup>"
    result.append((new_word, new_tags))
    return result
