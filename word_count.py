import string, re
from collections import Counter


def word_count(s):
    
   	# remove punctuation
	s = s.lower()
	for char in string.punctuation:
		s = s.replace(char, " ")
	s = s.replace('\n', ' ').replace('\t', ' ')

	# split into list 
	s = ''.join(s)
	s = s.split(' ')
	
	# count words, remove empty strings
	# and put in a dict
	result = {}
	for word in s:
		if word == ' ' or word == '':
			continue
		else:
			key = s.count(word)
			result[word] = key
	
	return result

    #reg expression way
    #return dict(Counter(
    #       re.sub(r'[^a-zA-Z0-9 ]', '', self.phrase.lower()).split()
    #   ))   
    
    
    #return Counter(phrase.translate(None, string.punctuation).lower().split())
    #word_including_apostrophe = compile(r"([a-z\d]+(?:'[a-z\d]+)?)") 
    #words = word_including_apostrophe.findall(phrase.lower()) 
    #counter = Counter(words) 
    #return dict(counter)

  
    # for char in ('-.,\n'):
    #     phrase = phrase.replace(char, ' ')
    #     phrase = phrase.lower()

    #     word_list=phrase.split()

    #     d={}
    #     for word in word_list:
    #         d[word]= d.get(word, 0) + 1
            
    # return dict(Counter(phrase.split()))
    