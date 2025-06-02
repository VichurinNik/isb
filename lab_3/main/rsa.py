from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from typing import Tuple


class RSA:
	"""
	Класс для асимметричного шифрования RSA с поддержкой операций с симметричными ключами.
	"""

	_PUBLIC_EXPONENT = 65537  # Стандартная публичная экспонента
	_KEY_SIZE = 2048  # Размер ключа в битах
	_HASH_ALGORITHM = hashes.SHA256()  # Алгоритм хеширования
	_PADDING = padding.OAEP(
		mgf=padding.MGF1(algorithm=hashes.SHA256()),
		algorithm=hashes.SHA256(),
		label=None
	)

	@staticmethod
	def generate_rsa_keys() -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
		"""Генерирует пару RSA ключей (приватный и публичный).

		Возвращает:
			Кортеж (приватный_ключ, публичный_ключ), где:
			- приватный_ключ: RSAPrivateKey
			- публичный_ключ: RSAPublicKey
		"""
		private_key = rsa.generate_private_key(
			public_exponent=RSA._PUBLIC_EXPONENT,
			key_size=RSA._KEY_SIZE
		)
		return private_key, private_key.public_key()

	@staticmethod
	def encrypt_symmetric_key(
			symmetric_key: bytes,
			public_key: rsa.RSAPublicKey
	) -> bytes:
		"""Шифрует симметричный ключ с использованием RSA публичного ключа.
		Аргументы:
			symmetric_key: Симметричный ключ для шифрования (в байтах)
			public_key: Публичный RSA ключ для шифрования
		"""
		try:
			return public_key.encrypt(symmetric_key, RSA._PADDING)
		except Exception as e:
			raise ValueError(f"Ошибка шифрования симметричного ключа: {str(e)}")

	@staticmethod
	def decrypt_symmetric_key(
			encrypted_key: bytes,
			private_key: rsa.RSAPrivateKey
	) -> bytes:
		"""Дешифрует симметричный ключ с использованием RSA приватного ключа.

		Аргументы:
			encrypted_key: Зашифрованный симметричный ключ (в байтах)
			private_key: Приватный RSA ключ для дешифрования
		"""
		try:
			return private_key.decrypt(encrypted_key, RSA._PADDING)
		except Exception as e:
			raise ValueError(f"Ошибка дешифрования симметричного ключа: {str(e)}")
