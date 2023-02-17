"""
File: checkerboard.py
Name:
------------------------
This program prints an alternating 
checkerboard pattern on Console
by nested for loop.
"""

# These constants control the size of the checkerboard
ROW = 5  # The number of rows
COL = 8  # The number of cols


def main():
	for i in range(5):
		for j in range(8g):
			if (i+j)%2==0:
				print('A',end='')
			else:
				print('*', end='')
		print('')

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
