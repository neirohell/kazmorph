from common_forms import generate_plural
from common_forms import generate_all_possessives
from common_forms import generate_all_long_personals_without_3p
from common_forms import generate_all_cases


# def generate_noun_forms(word_and_tags: tuple) -> list:
def generate_noun_forms(word_and_tags: tuple) -> list:
    """функция, генерирующая все формы для существительного
    """
    result = []
    all_possessives = generate_all_possessives(word_and_tags)
    result += all_possessives
    plural = generate_plural(word_and_tags)
    result += plural
    # result += generate_all_possessives(plural[0])
    result += generate_all_cases(word_and_tags)
    result += generate_all_long_personals_without_3p(word_and_tags)
    # TODO сначала отдельные аффиксы - потом комбинировать
    # Падежные окончания (и личные) применяются в конце слова
    # (ставятся последними, если аффиксов несколько).
    #  ...
    # TODO в конце пробегать по всем формам
    # и заполнять отсутствующие теги значениями по умолчанию
    return result
