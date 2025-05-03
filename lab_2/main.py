import nist_test
import const


def read_file(filename: str):
    """
    Читает содержимое файла и возвращает его как строку.

    Параметры:
    filename (str): имя файла для чтения.

    Возвращает:
    str: содержимое файла.
    """
    with open(filename, "r") as file:
        sequence = file.read()
    return sequence


def write_results(freq_cpp, freq_java,
                  runs_cpp, runs_java,
                  long_cpp, long_java,
                  results: str):
    """
    Записывает результаты тестов в файл.

    Параметры:
    freq_cpp (float): результат частотного теста для C++.
    freq_java (float): результат частотного теста для Java.
    runs_cpp (float): результат теста на одинаковые подряд идущие биты для C++.
    runs_java (float): результат теста на одинаковые подряд идущие биты для Java.
    long_cpp (float): результат теста на самую длинную последовательность единиц в блоке для C++.
    long_java (float): результат теста на самую длинную последовательность единиц в блоке для Java.
    results (str): имя файла для записи результатов.
    """
    with open(results, 'w') as file:
        file.write("Frequency bitwise test:\n")
        file.write(f"c++: {freq_cpp}\n")
        file.write(f"java: {freq_java}\n\n")

        file.write("A test for identical consecutive bits:\n")
        file.write(f"c++: {runs_cpp}\n")
        file.write(f"java: {runs_java}\n\n")

        file.write("Test for the longest sequence of units in a block:\n")
        file.write(f"c++: {long_cpp}\n")
        file.write(f"java: {long_java}\n")


def main():
    """
    Основная функция программы.

    Выполняет тесты NIST для последовательностей из C++ и Java,
    записывает результаты в файл.
    """
    freq_cpp = nist_test.frequency_test(read_file(const.bin_seq_cpp))
    freq_java = nist_test.frequency_test(read_file(const.bin_seq_java))
    runs_cpp = nist_test.runs_test(read_file(const.bin_seq_cpp))
    runs_java = nist_test.runs_test(read_file(const.bin_seq_java))
    long_cpp = nist_test.longest_run_test(read_file(const.bin_seq_cpp))
    long_java = nist_test.longest_run_test(read_file(const.bin_seq_java))
    write_results(freq_cpp, freq_java, runs_cpp, runs_java, long_cpp, long_java, const.res)


if __name__ == "__main__":
    main()