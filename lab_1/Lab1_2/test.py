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


def calculate_char_percentages(text: str) -> list[tuple[str, float]]:
    """
    Функция для вычисления процентного соотношения символов в строке.

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
    print(calculate_char_percentages(encrypted_text))

    # Замена символов по заранее определенному правилу
    decrypted_text = encrypted_text.replace(" ", 'р')
    decrypted_text = decrypted_text.replace("Д", 'а')
    decrypted_text = decrypted_text.replace("Е", 'б')
    decrypted_text = decrypted_text.replace("r", 'в')
    decrypted_text = decrypted_text.replace("А", 'г')
    decrypted_text = decrypted_text.replace("Б", 'д')
    decrypted_text = decrypted_text.replace("К", 'е')
    decrypted_text = decrypted_text.replace("Л", 'ж')
    decrypted_text = decrypted_text.replace("М", 'з')
    decrypted_text = decrypted_text.replace("t", 'и')
    decrypted_text = decrypted_text.replace("2", ' ')
    decrypted_text = decrypted_text.replace("Ь", 'о')
    decrypted_text = decrypted_text.replace("Ы", 'н')
    decrypted_text = decrypted_text.replace(">", 'с')
    decrypted_text = decrypted_text.replace("О", 'т')
    decrypted_text = decrypted_text.replace("<", 'м')
    decrypted_text = decrypted_text.replace("Й", 'к')
    decrypted_text = decrypted_text.replace("Я", 'п')
    decrypted_text = decrypted_text.replace("1", 'я')
    decrypted_text = decrypted_text.replace("Ч", 'л')
    decrypted_text = decrypted_text.replace("0", 'у')
    decrypted_text = decrypted_text.replace("a", 'ч')
    decrypted_text = decrypted_text.replace("Х", 'ю')
    decrypted_text = decrypted_text.replace("c", 'щ')
    decrypted_text = decrypted_text.replace("8", 'ы')
    decrypted_text = decrypted_text.replace(",", 'ь')
    decrypted_text = decrypted_text.replace("3", 'х')
    decrypted_text = decrypted_text.replace(".", 'ф')
    decrypted_text = decrypted_text.replace("b", 'ш')
    decrypted_text = decrypted_text.replace("9", 'ц')
    decrypted_text = decrypted_text.replace("?", ' ')
    decrypted_text = decrypted_text.replace("Ф", 'э')

    # Сохранение расшифрованного текста в файл
    write_to_file(constants.PATH_TO_WRITE_DECRYPTED_TEXT_FILE, decrypted_text)


if __name__ == "__main__":
    main()
