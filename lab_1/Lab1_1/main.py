from isb.lab_1.Lab1_1 import constants
import re


def read_file(file):
	with open(file, "r", encoding="utf-8") as f:
		return f.read()


def write_to_file(file, content):
	with open(file, 'w', encoding='utf-8') as f:
		f.write(content)


def text_editing(text: str):
	"""
	Преобразование текста:
	- Приводит текст к верхнему регистру.
	- Удаляет лишние пробелы.
	- Заменяет букву Ё на Е.
	- Оставляет только алфавитно-цифровые символы.
	- Вставляет символ 'Х' между повторяющимися символами.
	:param text: исходный текст
	:return: преобразованный текст
	"""
	new_text = text.upper().strip().replace('Ё', 'Е')
	new_text = ''.join(filter(str.isalnum, new_text))
	result = []
	i = 0
	while i < len(new_text):
		result.append(new_text[i])
		if i + 1 < len(new_text) and new_text[i] == new_text[i + 1]:
			result.append('Х')
		i += 1
	text_long = len(result)
	if text_long % 2 != 0:
		result.append("Х")
	print(result)
	return result


def matrix_editing(key: list):
	"""
	Создание матрицы на основе ключа.
	:param key: список уникальных символов ключа
	:return: матрица размером 4x8, заполненная сначала символами ключа,
			 затем остальными символами алфавита
	"""
	matrix = constants.MATRIX
	letters = constants.ALPHABET
	for letter in key:
		letters = letters.replace(letter, '')
	combined_list = key + list(letters)
	row, col = 0, 0
	for letter in combined_list:
		matrix[row][col] = letter
		col += 1
		if col == 8:
			col = 0
			row += 1
	return matrix


def key_editing(key: str) -> list:
	"""
	Преобразование ключа в список уникальных символов.
	:param key: строка с ключом
	:return: список уникальных символов ключа в верхнем регистре
	"""
	seen = set()
	unique_chars = []
	for char in key:
		if char not in seen:
			seen.add(char)
			unique_chars.append(char.upper())
	return unique_chars


def pair_formation(text: list):
	"""
	Формирование пар символов из списка.
	:param text: список символов
	:return: список пар символов
	"""
	pairs = []
	for i in range(0, len(text), 2):
		pair = (text[i], text[i + 1])
		pairs.append(pair)
	return pairs


def letter_position(letter, matrix: list):
	"""
	Поиск позиции символа в матрице.
	:param letter: искомый символ
	:param matrix: матрица символов
	:return: кортеж с индексами строки и столбца символа
	"""
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] == letter:
				# Возврат индексов строки и столбца
				return row, col
	return None, None


def shifr(text: list, matrix):
	"""
	Шифрование текста с использованием матрицы.
	:param text: список пар символов
	:param matrix: матрица символов
	:return: зашифрованный текст
	"""
	encrypted_text = []
	for par in text:
		# Нахождение позиций символов в матрице
		position_one = letter_position(par[0], matrix)
		position_two = letter_position(par[1], matrix)
		# Шифрование в зависимости от положения символов в матрице
		if position_one[0] == position_two[0]:
			# Символы находятся в одной строке
			if position_one[1] == 7:
				# Последний столбец первой буквы
				encrypted_text.append(matrix[(position_one[0])][0])
				encrypted_text.append(matrix[(position_two[0])][(position_two[1] + 1)])
			elif position_two[1] == 7:
				# Последний столбец второй буквы
				encrypted_text.append(matrix[(position_one[0])][(position_one[1] + 1)])
				encrypted_text.append(matrix[(position_two[0])][0])
			else:
				# Обычный сдвиг вправо
				encrypted_text.append(matrix[(position_one[0])][(position_one[1] + 1)])
				encrypted_text.append(matrix[(position_two[0])][(position_two[1] + 1)])
		elif position_one[1] == position_two[1]:
			# Символы находятся в одном столбце
			if position_one[0] == 3:
				# Последняя строка первой буквы
				encrypted_text.append(matrix[0][position_one[1]])
				encrypted_text.append(matrix[position_two[0] + 1][position_two[1]])
			elif position_two[0] == 3:
				# Последняя строка второй буквы
				encrypted_text.append(matrix[position_one[0] + 1][position_one[1]])
				encrypted_text.append(matrix[0][position_two[1]])
			else:
				# Обычный сдвиг вниз
				encrypted_text.append(matrix[(position_one[0] + 1)][(position_one[1])])
				encrypted_text.append(matrix[(position_two[0] + 1)][(position_two[1])])
		else:
			# Символы не в одной строке и не в одном столбце
			encrypted_text.append(matrix[position_two[0]][position_one[1]])
			encrypted_text.append(matrix[position_one[0]][position_two[1]])
	# Преобразование списка в строку и возврат результата
	return ''.join(encrypted_text)


def main():
	# Чтение текста и ключа из файлов
	text = read_file(constants.PATH_TO_TEXT_FILE)
	key = read_file(constants.PATH_TO_KEY_FILE)
	# Подготовка текста и создание матрицы
	pair_text = pair_formation(text_editing(text))
	matrix = matrix_editing(key_editing(key))
	# Шифрование текста и запись результата в файл
	write_to_file(constants.PATH_TO_WRITE_TEXT_FILE, shifr(pair_text, matrix))


if __name__ == "__main__":
	main()
