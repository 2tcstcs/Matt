"""
File: longest_line.py
Name:
---------------------------
This file shows how we can find
the longest line in romeojuliet.txt
through Python code
"""

# This constant shows the file path to romeojuliet.txt
FILEPATH = 'text/romeojuliet.txt'


def main():
	filepath = "text/romeojuliet.txt"
	with open(filepath,'r') as f:
		longest_line =''
		longest_count = 0
		for line in f:
			if len(line) > longest_count:
				longest_line = line
				longest_count = len(line)
		print(longest_line)



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
