import constants


def read_file(file: str) -> str:
    """
    Читает содержимое файла и возвращает его строку.

    :param file: Путь к файлу, который нужно прочитать.
    :raises FileNotFoundError: Если файл не найден.
    :raises UnicodeDecodeError: Если происходит ошибка декодирования файла.
    :return: Содержимое файла в виде строки.
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file} не найден.")
    except UnicodeDecodeError:
        raise UnicodeDecodeError(f"Произошла ошибка при чтении файла {file}.")


def write_to_file(file: str, content: str) -> None:
    """
    Записывает переданное содержимое в указанный файл.

    :param file: Путь к файлу, куда нужно записать данные.
    :param content: Строка, которую нужно записать в файл.
    :raises FileExistsError: Если файл уже существует и не перезаписывается.
    :raises PermissionError: Если нет прав на запись в файл.
    """
    try:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
    except FileExistsError:
        raise FileExistsError(f"Файл {file} уже существует.")
    except PermissionError:
        raise PermissionError(f"У вас нет прав на запись в файл {file}.")


def substitution_key(key: dict, text: str) -> str:
    """
    Преобразует текст согласно переданному ключу замены символов.

    :param key: Словарь, где ключи — символы, подлежащие замене, а значения — новые символы.
    :param text: Исходная строка, которую нужно преобразовать.
    :return: Преобразованная строка.
    """
    new_text = text
    for original_char, replacement_char in key.items():
        new_text = new_text.replace(original_char, replacement_char)
    return new_text


def main() -> None:
    """
    Основная функция программы.

    Читает зашифрованный текст из файла, применяет ключ дешифрации и записывает результат в другой файл.
    """
    try:
        text = read_file(constants.PATH_TO_ENCRYPTED_TEXT)
        new_text = substitution_key(constants.KEY_DECRYPT, text)
        write_to_file(constants.PATH_TO_WRITE_DECRYPTED_TEXT_FILE, new_text)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    main()
