import math

def frequency_test(bits):
	sum_bit = 0
	for bit in bits:
		if bit == "0":
			sum_bit += -1
		else:
			sum_bit +=1
	normal_sum = sum_bit / math.sqrt(len(bits))
	p_value = math.erfc(normal_sum / math.sqrt(2))
	return p_value


