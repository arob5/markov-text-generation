#
# main.py
# Simple interface for Markov text generator
# Last Modified: 8/22/2017
# Modified By: Andrew Roberts
#

import generate_text
import parse_text
import sys

def main():

	# Parse input text data
	text = parse_text.parse_file("trump_speech_transcripts.txt")	
	d = parse_text.create_n_gram_dict(text, 6, False)

	# Generate new text
	print("'", generate_text.make_text("Thank ", 100, d, False),"'")	

main()
