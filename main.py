#
# markov_interface.py
# Simple interface for Markov text generator
# Last Modified: 8/22/2017
# Modified By: Andrew Roberts
#

import generate_text
import parse_text
import sys

def main():
	text = parse_text.parse_file("obama_speech_transcripts.txt", True)	
	d = parse_text.create_char_dict(text, 6)

	print("'", generate_text.make_text("thank ", 100, d), "'")	

	"""
	num_args = get_num_args()
	if valid:
		word_dict = read_file()
		store_word_dict(word_dict)
	"""

def get_num_args():
	return len(sys.argv)
	

main()
