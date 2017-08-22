#
# generate_text.py
# Generates text based word or character dictionary created in parse_text.py
# Last Modified: 8/22/2017
# Modified By: Andrew Roberts
#

import numpy as np

def weighted_sample(n_gram_counts):
	total = sum(list(n_gram_counts.values()))
	rnd = np.random.randint(low=0, high=total)

	for token, count in n_gram_counts.items():
		rnd -= n_gram_counts[token]
		if rnd < 0:
			return token

def make_text(start, length, markov_dict):
	
	current_gram = start
	result = start 
	n = len(list(markov_dict.keys())[0])

	for i in range(length):
		options = markov_dict[current_gram]
	
		if not options:
			break

		choice = weighted_sample(options)
		result += choice
		current_gram = result[-n:]	

	return result
	

