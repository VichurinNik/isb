import math


def frequency_test(bits):
	sum_bit = 0
	for bit in bits:
		if bit == "0":
			sum_bit += -1
		else:
			sum_bit += 1
	normal_sum = sum_bit / math.sqrt(len(bits))
	p_value = math.erfc(normal_sum / math.sqrt(2))
	return p_value


def runs_test(bits):
	share_units = 0
	for bit in bits:
		if bit == "1":
			share_units += 1
	share_units = share_units / len(bits)

	if abs(share_units - 0.5 >= math.sqrt(len(bits))):
		return 0.0

	series = 0
	for i in range(len(bits) - 1):
		if bits[i] != bits[i + 1]:
			series += 1

	numerator = abs(series - 2 * len(bits) * share_units * (1 - share_units))
	denominator = 2 * math.sqrt(2 * len(bits)) * share_units * (1 - share_units)
	p_value = math.erfc(numerator / denominator)
	return p_value
