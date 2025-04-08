import constants


def read_file(file_path: str) -> str:
    """
    Функция для чтения содержимого файла.
    :param file_path: путь к файлу, который нужно прочитать.
    :return: содержимое файла в виде строки.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_to_file(file_path: str, content: str) -> None:
    """
    Функция для записи строки в файл.

    :param file_path: путь к файлу, куда нужно записать данные.
    :param content: строка, которую нужно записать в файл.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def сharacter_frequency_formation(text: str) -> list[tuple[str, float]]:
    """
    Функция для вычисления частоты  символов в строке.

    :param text: исходная строка, для которой будут рассчитаны проценты.
    :return: список кортежей, где первый элемент — символ, второй — доля этого символа в тексте.
    """
    text_length = len(text)
    unique_chars = set(list(text))  # набор уникальных символов
    char_percentages = {}  # словарь для хранения процента каждого символа

    for char in unique_chars:
        count = 0
        for char_in_text in text:
            if char_in_text == char:
                count += 1
        char_percentages[char] = (count / text_length)

    # Сортируем символы по убыванию их доли в тексте
    sorted_char_percentage = sorted(
        char_percentages.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return sorted_char_percentage


def main() -> None:
    """
    Главная функция программы.

    Читает зашифрованный текст из файла, вычисляет процентное соотношение символов,
    заменяет символы согласно заданному ключу и сохраняет результат в новый файл.
    """
    encrypted_text = read_file(constants.PATH_TO_ENCRYPTED_TEXT)
    print(сharacter_frequency_formation(encrypted_text))
if __name__ == "__main__":
    main()
