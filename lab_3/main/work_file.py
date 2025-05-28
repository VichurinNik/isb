from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from typing import Optional


class FileWorker:
	"""
	Класс для работы с файлами: чтение/запись данных и сериализация/десериализация RSA ключей.
	"""

	@staticmethod
	def read_file(file_path: str) -> bytes:
		"""
		Чтение содержимого файла в бинарном режиме.

		:param file_path: Путь к файлу
		:return: Содержимое файла в виде bytes
		:raises IOError: Если произошла ошибка при чтении файла
		"""
		try:
			with open(file_path, "rb") as file:
				return file.read()
		except IOError as e:
			raise IOError(f"Ошибка при чтении файла {file_path}: {str(e)}")

	@staticmethod
	def write_file(data: bytes, file_path: str) -> None:
		"""
		Запись данных в файл в бинарном режиме.

		:param data: Данные для записи
		:param file_path: Путь к файлу
		:raises IOError: Если произошла ошибка при записи файла
		"""
		try:
			with open(file_path, "wb") as file:
				file.write(data)
		except IOError as e:
			raise IOError(f"Ошибка при записи файла {file_path}: {str(e)}")

	@staticmethod
	def save_private_key(private_key: rsa.RSAPrivateKey,
						 file_path: str,
						 password: Optional[bytes] = None) -> None:
		"""
		Сериализация приватного RSA ключа в файл в формате PEM.

		:param private_key: Приватный ключ
		:param file_path: Путь для сохранения ключа
		:param password: Пароль для шифрования ключа (None - без шифрования)
		:raises ValueError: Если произошла ошибка сериализации
		"""
		try:
			encryption = (serialization.NoEncryption() if password is None
						  else serialization.BestAvailableEncryption(password))

			pem_data = private_key.private_bytes(
				encoding=serialization.Encoding.PEM,
				format=serialization.PrivateFormat.PKCS8,
				encryption_algorithm=encryption
			)
			FileWorker.write_file(pem_data, file_path)
		except Exception as e:
			raise ValueError(f"Ошибка сериализации приватного ключа: {str(e)}")

	@staticmethod
	def save_public_key(public_key: rsa.RSAPublicKey, file_path: str) -> None:
		"""
		Сериализация публичного RSA ключа в файл в формате PEM.

		:param public_key: Публичный ключ
		:param file_path: Путь для сохранения ключа
		:raises ValueError: Если произошла ошибка сериализации
		"""
		try:
			pem_data = public_key.public_bytes(
				encoding=serialization.Encoding.PEM,
				format=serialization.PublicFormat.SubjectPublicKeyInfo
			)
			FileWorker.write_file(pem_data, file_path)
		except Exception as e:
			raise ValueError(f"Ошибка сериализации публичного ключа: {str(e)}")

	@staticmethod
	def load_private_key(file_path: str, password: Optional[bytes] = None) -> rsa.RSAPrivateKey:
		"""
		Загрузка приватного RSA ключа из файла.

		:param file_path: Путь к файлу с ключом
		:param password: Пароль для расшифровки ключа (если требуется)
		:return: Загруженный приватный ключ
		:raises ValueError: Если произошла ошибка загрузки ключа
		"""
		try:
			key_data = FileWorker.read_file(file_path)
			return serialization.load_pem_private_key(key_data, password=password)
		except Exception as e:
			raise ValueError(f"Ошибка загрузки приватного ключа: {str(e)}")

	@staticmethod
	def load_public_key(file_path: str) -> rsa.RSAPublicKey:
		"""
		Загрузка публичного RSA ключа из файла.

		:param file_path: Путь к файлу с ключом
		:return: Загруженный публичный ключ
		:raises ValueError: Если произошла ошибка загрузки ключа
		"""
		try:
			key_data = FileWorker.read_file(file_path)
			return serialization.load_pem_public_key(key_data)
		except Exception as e:
			raise ValueError(f"Ошибка загрузки публичного ключа: {str(e)}")