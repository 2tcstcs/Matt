"""
File: file_reading.py
Name:
---------------------------
This file shows how we can open and
print text files through Python code
"""


def main():
	filepath = "text/JerrySecret5.txt"
	with open(filepath, 'r') as f :
		for line in f:
			print(line, end='')


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
