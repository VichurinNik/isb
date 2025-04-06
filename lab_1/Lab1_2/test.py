import constants


def read_file(file):
	with open(file, "r", encoding="utf-8") as f:
		return f.read()


def calculate_char_percentages(text):
	text_len = len(text)
	uniq = set(list(text))
	for char in uniq:
		count = 0
		for char in text:


	return uniq


def main():
	text = read_file(constants.PATH_TO_ENCRYPTED_TEXT)
	print(calculate_char_percentages(text))



if __name__ == '__main__':
	main()
