import pickle 
import dill

file = open('model.pickle', 'rb')
model = dill.load(file)
file.close()


# print(dict(model['I','am']))

def gen_sentence(starting_words):
	import random

	 

	# starting words
	text = starting_words.split()
	sentence_finished = False
	 
	while not sentence_finished:
	  # select a random probability threshold  
	  r = random.random()
	  accumulator = 0.01 # the minimum probability for a word to be added in text

	  for word in model[tuple(text[-2:])].keys():
	      accumulator += model[tuple(text[-2:])][word]
	      # select words that are above the probability threshold
	      if accumulator >= r:
	          text.append(word)
	          break

	  if text[-2:] == [None, None]:
	      sentence_finished = True
	 
	return ' '.join([t for t in text if t])

# print(gen_sentence())

