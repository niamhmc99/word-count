from collections import Counter


def word_count(phrase):

    word_including_apostrophe = compile(r"([a-z\d]+(?:'[a-z\d]+)?)") 
    words = word_including_apostrophe.findall(phrase.lower()) 
    counter = Counter(words) 
    return dict(counter)
  
    # for char in ('-.,\n'):
    #     phrase = phrase.replace(char, ' ')
    #     phrase = phrase.lower()

    #     word_list=phrase.split()

    #     d={}
    #     for word in word_list:
    #         d[word]= d.get(word, 0) + 1
            
    # return dict(Counter(phrase.split()))
    