from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from typing import Tuple


class RSA:
	"""
	Класс для работы с RSA шифрованием:
	- генерация ключевой пары
	- шифрование/дешифрование симметричных ключей
	"""

	# Стандартные параметры для генерации ключей
	PUBLIC_EXPONENT = 65537
	KEY_SIZE = 2048
	HASH_ALGORITHM = hashes.SHA256()

	@staticmethod
	def generate_key_pair() -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
		"""
		Генерация пары RSA ключей (приватный и публичный).

		:return: Кортеж (приватный_ключ, публичный_ключ)
		:raises ValueError: При ошибке генерации ключей
		"""
		try:
			private_key = rsa.generate_private_key(
				public_exponent=RSA.PUBLIC_EXPONENT,
				key_size=RSA.KEY_SIZE
			)
			public_key = private_key.public_key()
			return private_key, public_key
		except Exception as e:
			raise ValueError(f"Ошибка генерации RSA ключей: {str(e)}")

	@staticmethod
	def encrypt_data(data: bytes, public_key: rsa.RSAPublicKey) -> bytes:
		"""
		Шифрование данных с использованием RSA публичного ключа.

		:param data: Данные для шифрования (обычно симметричный ключ)
		:param public_key: Публичный RSA ключ
		:return: Зашифрованные данные
		:raises ValueError: При ошибке шифрования
		"""
		try:
			return public_key.encrypt(
				data,
				padding.OAEP(
					mgf=padding.MGF1(algorithm=RSA.HASH_ALGORITHM),
					algorithm=RSA.HASH_ALGORITHM,
					label=None
				)
			)
		except Exception as e:
			raise ValueError(f"Ошибка шифрования данных: {str(e)}")

	@staticmethod
	def decrypt_data(encrypted_data: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
		"""
		Дешифрование данных с использованием RSA приватного ключа.

		:param encrypted_data: Зашифрованные данные
		:param private_key: Приватный RSA ключ
		:return: Расшифрованные данные
		:raises ValueError: При ошибке дешифрования
		"""
		try:
			return private_key.decrypt(
				encrypted_data,
				padding.OAEP(
					mgf=padding.MGF1(algorithm=RSA.HASH_ALGORITHM),
					algorithm=RSA.HASH_ALGORITHM,
					label=None
				)
			)
		except Exception as e:
			raise ValueError(f"Ошибка дешифрования данных: {str(e)}")

	# Методы-обертки для совместимости со старым кодом
	@staticmethod
	def generate_rsa_keys() -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
		"""Алиас для generate_key_pair (совместимость)"""
		return RSA.generate_key_pair()

	@staticmethod
	def encrypt_symmetric_key(symmetric_key: bytes, public_key: rsa.RSAPublicKey) -> bytes:
		"""Алиас для encrypt_data (совместимость)"""
		return RSA.encrypt_data(symmetric_key, public_key)

	@staticmethod
	def decrypt_symmetric_key(encrypted_key: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
		"""Алиас для decrypt_data (совместимость)"""
		return RSA.decrypt_data(encrypted_key, private_key)