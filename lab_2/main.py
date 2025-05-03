import nist_test
import const


def read_file(filename: str):
	with open(filename, "r") as file:
		sequence = file.read()
	return sequence


def write_results(freq_cpp, freq_java,
				  runs_cpp, runs_java,
				  # long_cpp, long_java,
				  results: str):
	with open(results, 'w') as file:
		file.write("Frequency bitwise test:\n")
		file.write(f"cpp: {freq_cpp}\n")
		file.write(f"java: {freq_java}\n\n")

		file.write("A test for identical consecutive bits:\n")
		file.write(f"cpp: {runs_cpp}\n")
		file.write(f"java: {runs_java}\n\n")

		# file.write("Test for the longest sequence of units in a block:\n")
		# file.write(f"cpp: {long_cpp}\n")
		# file.write(f"java: {long_java}\n")


def main():
	freq_cpp = nist_test.frequency_test(read_file(const.bin_seq_cpp))
	freq_java = nist_test.frequency_test(read_file(const.bin_seq_java))
	runs_cpp = nist_test.runs_test(read_file(const.bin_seq_cpp))
	runs_java = nist_test.runs_test(read_file(const.bin_seq_java))
	write_results(freq_cpp,freq_java,runs_cpp,runs_java,const.res)



if __name__ == "__main__":
	main()
