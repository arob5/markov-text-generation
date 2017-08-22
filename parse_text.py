#
# generate_word_dict.py
# Generates n-gram dictionary for Markov text generator
# Last Modified: 8/22/2017
# Modified By: Andrew Roberts
#


import pickle

#
# {"word1" : {"following_word1" : count}, "word2" : {"following_word1" : count, "following_word2": count}}
#

def parse_file(filename, lower_case=False):
	with open(filename, "r") as f:
		contents = f.read().splitlines()
		contents = "".join(contents)

	if lower_case:
		contents = contents.lower()

	return contents

def create_char_dict(text, n=3):
	char_dict = {}

	for i in range(len(text) - n + 1):
		n_gram = text[i:i+n]
		char_dict[n_gram] = char_dict.get(n_gram, dict())			

		if i != (len(text)-n):
			char_dict[n_gram][text[i+n]] = char_dict[n_gram].get(text[i+n], 0) + 1
				
	return char_dict

def save_dict(markov_dict):
	filename = "markov_dict.pickle"
	
	with open(filename, "wb") as f:
		pickle.dump(markov_dict, f, protocol=pickle.HIGHEST_PROTOCOL)	

	print("Saved file as: ", filename)

def load_dict(filename):	
	with open(filename, "rb") as f:
		d = pickle.load(f)	

	return d
