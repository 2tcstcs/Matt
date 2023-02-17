"""
File: my_upper.py
Name:
----------------------
This file shows how python
built-in s.upper() is implemented
"""


def main():
	s = '123JeRrY123'
	print(upper(s))


def upper(s):
	s2=''
	for i in range(len(s)):
		ch=s[i]
		if ch.islower():
			s2=s2+ch.upper()
		else:
			s2=s2+ch
	return s2



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
