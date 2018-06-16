
# твёрдые гласные
hard_vowels = {'а', 'о', 'ы', 'ұ', 'у'}
# мягкие гласные
soft_vowels = {'ә', 'ө', 'і', 'ү', 'и', 'е', 'э'}
# все гласные
vowels = hard_vowels.union(soft_vowels)

# звонкие согласные
voiced_consonants = {'б', 'в', 'г', 'ғ', 'д', 'ж', 'з'}
# глухие согласные
voiceless_consonant = {'к', 'қ', 'п', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'}
# сонорные согласные
sonorous_consonants = {'р', 'л', 'й', 'у', 'м', 'н', 'ң'}
# твёрдые согласные
hard_consonants = {'қ', 'ғ'}
# мягкие согласные
soft_consonants = {'к', 'г'}
# все согласные
consonants = (voiced_consonants.union(
              voiceless_consonant).union(
              sonorous_consonants))


def add_affix_with_harmony(word: str, affix: str) -> str:
    """Функция, реализующая присоединение аффикса с учётом сингармонизма
    """
    result = word

    # если слово оканчивается на қ, к, п,
    # а аффикс начинается с гласного звука, то:
    # к чередуется с г
    # қ чередуется с ғ
    # TODO п чередуется с б или у
    # Көк + i = көгi
    # Қонақ + ы = қонағы
    # Жап + ып = жауып
    if (word[-1] == 'к') \
            and (affix[0] in vowels):
        # TODO TypeError: 'str' object does not support item assignment
        # result[-1] = 'г'
        result = result[:-1] + 'г'
        result += affix

    elif (word[-1] == 'қ') \
            and (affix[0] in vowels):
        result = result[:-1] + 'ғ'
        result += affix

    elif (word[-1] == 'п') \
            and (affix[0] in vowels):
        result = result[:-1] + 'б'
        # TODO result[-1] = 'у'
        result += affix

    # В заимствованных словах, оканчивающихся на двойной согласный,
    # при добавлении аффикса один согласный выпадает.
    elif (word[-1] == word[-2]):
        result = word[:-1] + affix

    # В заимствованных словах, оканчивающихся на «Ь»,
    # при аффиксе, начинающемся с гласного, «Ь» выпадает;
    # при аффиксе, начинающемся с согласного – остается.
    elif (word[-1] == 'ь') \
            and (affix[0] in vowels):
        result = word[:-1] + affix

    # В словах русского происхождения, оканчивающихся на:
    # НК, НТ, СК, НД, КТ, РВ, МБ, МСК, ДЖ, ПТ, РЗЬ, НКТ
    # при добавлении аффиксов, начинающихся на согласные,
    # добавляется «Ы» или «i»
    elif (word.endswith("НК") or
          word.endswith("НТ") or
          word.endswith("СК") or
          word.endswith("НД") or
          word.endswith("КТ") or
          word.endswith("РВ") or
          word.endswith("МБ") or
          word.endswith("МСК") or
          word.endswith("ДЖ") or
          word.endswith("ПТ") or
          word.endswith("РЗЬ") or
          word.endswith("НКТ")) \
            and (affix[0] in consonants):
        result = word + 'ы' + affix
        # TODO result = word + 'i' + affix

    else:
        result += affix

    return result

    # TODO
    # В глаголах, оканчивающихся на « И » при добавлении
    # аффикса « –А » пишется « Я »:
    # Той + а + сың = Тоясың
    # Қой + а + ды = Қояды

    # TODO
    # Если глагол оканчивается на И, Й, то в неопределенной
    # форме добавляется не
    # « -У», а «–Ю»:
    # Кию Жаю Той + у = Тою Жай + у = Жаю

    # TODO
    # В словах на СТ, ОТ, ВТ, СТЬ, ЗД, оканчивающихся при
    # аффиксе, последняя Т, ТЬ, Д не пишется:
    # Текст + те = Тексте Съезд + ге = съезге


def add_affix_choosing_hard_or_soft(word: str,
                                    hard_affix: str,
                                    soft_affix: str) -> str:
    """Функция, добавляющая твёрдый или мягкий аффикс в зависимости от гласной,
    находящейся среди последних 2-3 букв слова.
    """
    result = ""

    if len(word) > 2:
        if len(set(word[-3:]).intersection(hard_vowels)) != 0:
            result += add_affix_with_harmony(word, hard_affix)
        if len(set(word[-3:]).intersection(soft_vowels)) != 0:
            result += add_affix_with_harmony(word, soft_affix)
    else:
        if len(set(word[-2:]).intersection(hard_vowels)) != 0:
            result += add_affix_with_harmony(word, hard_affix)
        if len(set(word[-2:]).intersection(soft_vowels)) != 0:
            result += add_affix_with_harmony(word, soft_affix)

    return result
