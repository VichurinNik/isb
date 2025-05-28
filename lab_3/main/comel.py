import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


class CamelliaCBC:
	"""
	Класс для шифрования и дешифрования данных с использованием алгоритма Camellia в режиме CBC.
	Поддерживаются ключи длиной 128, 192 и 256 бит (16, 24 и 32 байта соответственно).
	"""

	@staticmethod
	def generate_key(key_size: int) -> bytes:
		"""
		Генерация случайного ключа для алгоритма Camellia.

		:param key_size: Размер ключа в байтах (16, 24 или 32)
		:return: Случайный ключ
		:raises ValueError: Если указан неправильный размер ключа
		"""
		if key_size not in {16, 24, 32}:
			raise ValueError(
				"Размер ключа должен быть 16, 24 или 32 байта "
				"для Camellia-128, Camellia-192 или Camellia-256 соответственно"
			)
		return os.urandom(key_size)

	@staticmethod
	def encrypt(key: bytes, plaintext: bytes) -> bytes:
		"""
		Шифрование данных с использованием Camellia в режиме CBC.

		:param key: Ключ шифрования (16, 24 или 32 байта)
		:param plaintext: Данные для шифрования
		:return: Вектор инициализации (IV) + зашифрованные данные
		:raises ValueError: Если указан ключ неправильного размера
		"""
		if len(key) not in {16, 24, 32}:
			raise ValueError(
				"Размер ключа должен быть 16, 24 или 32 байта "
				"для Camellia-128, Camellia-192 или Camellia-256 соответственно"
			)

		# Генерация вектора инициализации
		iv = os.urandom(16)

		# Дополнение данных по стандарту PKCS7
		padder = padding.PKCS7(128).padder()
		padded_data = padder.update(plaintext) + padder.finalize()

		# Шифрование данных
		cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
		encryptor = cipher.encryptor()
		ciphertext = encryptor.update(padded_data) + encryptor.finalize()

		return iv + ciphertext

	@staticmethod
	def decrypt(key: bytes, ciphertext: bytes) -> bytes:
		"""
		Дешифрование данных, зашифрованных с использованием Camellia в режиме CBC.

		:param key: Ключ шифрования (16, 24 или 32 байта)
		:param ciphertext: Зашифрованные данные (IV + ciphertext)
		:return: Расшифрованные данные
		:raises ValueError: Если указан ключ неправильного размера
		"""
		if len(key) not in {16, 24, 32}:
			raise ValueError(
				"Размер ключа должен быть 16, 24 или 32 байта "
				"для Camellia-128, Camellia-192 или Camellia-256 соответственно"
			)

		# Извлечение вектора инициализации
		iv = ciphertext[:16]
		encrypted_data = ciphertext[16:]

		# Дешифрование данных
		cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
		decryptor = cipher.decryptor()
		padded_plaintext = decryptor.update(encrypted_data) + decryptor.finalize()

		# Удаление дополнения PKCS7
		unpadder = padding.PKCS7(128).unpadder()
		plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

		return plaintext
