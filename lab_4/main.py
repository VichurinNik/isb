import os
import sys
from typing import List
from time_test import PerformanceBenchmark
from hash_card import CardSearcher
from const import *


def main():
	print("Программа для поиска номера карты по хешу")

	# Выбор режима работы
	while True:
		print("\nДоступные режимы:")
		print("1 - Тестирование производительности")
		print("2 - Поиск номера карты")
		print("3 - Выход")

		choice = input("Выберите режим (1-3): ").strip()

		if choice == "1":
			# Режим тестирования производительности
			benchmark = PerformanceBenchmark(BINS)
			max_proc = int(os.cpu_count() * 1.5)
			print(f"\nЗапуск тестов для 1-{max_proc} процессов...")
			benchmark.run_tests(max_proc)
			benchmark.plot_performance()

		elif choice == "2":
			# Режим поиска номера карты
			print("\nПараметры поиска:")
			print(f"Хеш: {CARD_HASH}")
			print(f"Последние 4 цифры: {LAST_4_DIGITS}")
			print(f"BIN-коды: {', '.join(BINS)}")

			# Выбор количества процессов
			while True:
				try:
					nproc = int(input("\nВведите количество процессов (0 для авто): "))
					if nproc == 0:
						nproc = os.cpu_count()
						print(f"Используется {nproc} процессов (по числу ядер)")
					break
				except ValueError:
					print("Ошибка: введите число")

			# Выполнение поиска
			searcher = CardSearcher()
			result, duration = searcher.search_card_number(nproc)

			if result:
				print(f"\nНайден номер карты: {result}")
				print(f"Время поиска: {duration:.2f} сек.")

				# Сохранение результата
				save = input("Сохранить результат? (y/n): ").lower()
				if save == 'y':
					searcher.save_result(result)
			else:
				print("\nНомер карты не найден")

		elif choice == "3":
			print("Выход из программы")
			break

		else:
			print("Некорректный выбор, попробуйте снова")


if __name__ == "__main__":
	main()