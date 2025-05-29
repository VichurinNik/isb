import const as const
from comel import CamelliaCBC
from work_file import *
from rsa import RSA
from typing import NoReturn, Optional


class Performance:
	"""
	Класс для управления процессами генерации ключей, шифрования и дешифрования данных.
	Объединяет функциональность RSA и Camellia алгоритмов.
	"""

	@staticmethod
	def _validate_key_size(size_str: str) -> int:
		"""
		Валидация введенного размера ключа.

		:param size_str: Введенная пользователем строка с размером ключа
		:return: Валидный размер ключа
		:raises ValueError: Если введен некорректный размер ключа
		"""
		if size_str not in {"16", "24", "32"}:
			raise ValueError("Размер ключа должен быть 16, 24 или 32 байта")
		return int(size_str)

	@staticmethod
	def generate_keys() -> None:
		"""
		Генерация асимметричных RSA ключей и симметричного Camellia ключа.
		Ключи сохраняются в файлы, указанные в константах.
		"""
		try:
			# Генерация и сохранение RSA ключей
			private_key, public_key = RSA.generate_rsa_keys()
			FileWorker.save_private_key(private_key, const.PATH_TO_PRIVATE_KEY)
			FileWorker.save_public_key(public_key, const.PATH_TO_PUBLIC_KEY)
			print("Асимметричные ключи успешно сгенерированы и сохранены.")

			# Запрос и валидация размера ключа Camellia
			while True:
				try:
					size_input = input("Введите размер ключа (16, 24 или 32 байта): ")
					key_size = Performance._validate_key_size(size_input)
					break
				except ValueError as e:
					print(f"Ошибка: {e}")

			# Генерация и сохранение ключа Camellia
			symmetric_key = CamelliaCBC.generate_key(key_size)
			encrypted_sym_key = RSA.encrypt_symmetric_key(symmetric_key, public_key)
			FileWorker.write_file(encrypted_sym_key, const.PATH_TO_SYM_KEY)
			print("Симметричный ключ успешно сгенерирован и сохранен.")

		except Exception as e:
			print(f"Ошибка при генерации ключей: {str(e)}")
			raise

	@staticmethod
	def _check_required_files() -> bool:
		"""
		Проверка наличия необходимых файлов с ключами.

		:return: True если все файлы существуют и не пустые, иначе False
		"""
		required_files = [
			const.PATH_TO_SYM_KEY,
			const.PATH_TO_PRIVATE_KEY,
			const.PATH_TO_PUBLIC_KEY
		]
		return all(FileWorker.read_file(file_path) for file_path in required_files)

	@staticmethod
	def encrypt_text() -> None:
		"""
		Шифрование текста из файла с использованием Camellia.
		Требует наличия сгенерированных ключей.
		"""
		try:
			if not Performance._check_required_files():
				print("Ошибка: Сначала необходимо сгенерировать ключи.")
				return

			# Загрузка ключей
			private_key = FileWorker.load_private_key(const.PATH_TO_PRIVATE_KEY)
			encrypted_sym_key = FileWorker.read_file(const.PATH_TO_SYM_KEY)
			symmetric_key = RSA.decrypt_symmetric_key(encrypted_sym_key, private_key)

			# Шифрование данных
			plaintext = FileWorker.read_file(const.PATH_TO_PLAINTEXT)
			if not plaintext:
				print("Ошибка: Файл с исходным текстом пуст или не существует.")
				return

			ciphertext = CamelliaCBC.encrypt(symmetric_key, plaintext)
			FileWorker.write_file(ciphertext, const.PATH_TO_CIPHERTEXT)
			print("Текст успешно зашифрован и сохранен.")

		except Exception as e:
			print(f"Ошибка при шифровании: {str(e)}")
			raise

	@staticmethod
	def decrypt_text() -> None:
		"""
		Дешифрование текста из файла с использованием Camellia.
		Требует наличия сгенерированных ключей и зашифрованного файла.
		"""
		try:
			if not Performance._check_required_files():
				print("Ошибка: Необходимы ключи для дешифрования.")
				return

			# Загрузка ключей
			private_key = FileWorker.load_private_key(const.PATH_TO_PRIVATE_KEY)
			encrypted_sym_key = FileWorker.read_file(const.PATH_TO_SYM_KEY)
			symmetric_key = RSA.decrypt_symmetric_key(encrypted_sym_key, private_key)

			# Дешифрование данных
			ciphertext = FileWorker.read_file(const.PATH_TO_CIPHERTEXT)
			if not ciphertext:
				print("Ошибка: Файл с зашифрованным текстом пуст или не существует.")
				return

			decrypted_text = CamelliaCBC.decrypt(symmetric_key, ciphertext)
			FileWorker.write_file(decrypted_text, const.PATH_TO_ENCRYPTED_TEXT)
			print("Текст успешно дешифрован и сохранен.")

		except Exception as e:
			print(f"Ошибка при дешифровании: {str(e)}")
			raise