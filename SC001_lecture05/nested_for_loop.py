"""
File: nested_for_loop.py
Name:
------------------------
This program shows students the basic
concepts of nested (double) for loop
by printing a 4-row-3-col rectangle
"""

# These constants control the diameter of the rectangle
ROW = 4  # The number of rows
COL = 3  # The number of cols


def main():
	for i in range(3):
		for j in range(4):
			print('#',end='')
		print('')


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
