import os

import constants


def read_file(file):
	with open(file, "r", encoding="utf-8") as f:
		return f.read()


def calculate_char_percentages(text):
	text_len = len(text)
	uniq = set(list(text))
	char_percentages = {}
	for char in uniq:
		count = 0
		for char1 in text:
			if char1 == char:
				count += 1
		char_percentages[char] = (count/text_len)
	sorted1 = sorted(char_percentages.items(),key=lambda item: item[1],reverse=True)
	return sorted1

def main():
	text = read_file(constants.PATH_TO_ENCRYPTED_TEXT)
	result_char = {}
	print(calculate_char_percentages(text))
	text = text.replace(" ", 'р')
	text = text.replace("Д", 'а')
	text = text.replace("Е", 'б')
	text = text.replace("r", 'в')
	text = text.replace("А", 'г')
	text = text.replace("Б", 'д')
	text = text.replace("К", 'е')
	text = text.replace("Л", 'ж')
	text = text.replace("М", 'з')
	text = text.replace("t", 'и')
	text = text.replace("2",' ')
	text = text.replace("Ь", 'о')
	text = text.replace("Ы", 'н')
	text = text.replace(">", 'с')
	text = text.replace("О", 'т')
	text = text.replace("<", 'м')
	text = text.replace("Й", 'к')
	text = text.replace("Я", 'п')
	text = text.replace("1", 'я')
	text = text.replace("Ч", 'л')
	text = text.replace("0", 'у')
	text = text.replace("a", 'ч')
	text = text.replace("Х", 'ю')
	text = text.replace("c", 'щ')
	text = text.replace("8", 'ы')
	text = text.replace(",", 'ь')
	text = text.replace("3", 'х')
	text = text.replace(".", 'ф')
	text = text.replace("b", 'ш')
	text = text.replace("9", 'ц')
	text = text.replace("?", ' ')
	text = text.replace("Ф", 'э')


if __name__ == '__main__':
	main()
