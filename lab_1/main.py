letter_rus = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
key = input("Введите ключ:")
text_encoding = list(input("Введите текст для кодировки:").upper())
key = list(key.strip().upper())
for letter in key:
	letter_rus = letter_rus.replace(letter, '')
letter_rus = list(letter_rus)
combined_list = key + letter_rus
table_rus = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None]
]
row = 0
col = 0
for letter in combined_list:
	table_rus[row][col] = letter
	col +=1
	if col ==8:
		col = 0
		row += 1