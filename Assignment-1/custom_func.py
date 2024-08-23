import correction
import find_syllables #will require indic_transliteration 
from collections import Counter

def sort_dict(dictionary,reverse=True):
    return dict(sorted(dictionary.items(),reverse=reverse, key=lambda item: item[1]))

def uni_dict(tokens):
    #Unigram Frequency
    uni_frq=Counter(tokens)
    return uni_frq

def bi_dict(tokens):
    #Bigram Frequency
    bigrams = [f"{tokens[i]} {tokens[i+1]}" for i in range(len(tokens)-1)]
    bi_frq=Counter(bigrams)
    return bi_frq

def syll_list(tokens):
    #syllables
    syllables=[]
    for a in tokens:
        corrected=correction.correction(a)
        temp=(find_syllables.find_syllables(corrected))
        for b in temp:
            temp2=''
            temp2 += ''.join(str(x) for x in b)
            syllables.append(temp2)

    
    return syllables

def char_list(tokens):
    #characters
    characters=[]
    for a in tokens:
        corrected=correction.correction(a)
        for b in corrected:
            characters.append(str(b))
    
    
    return characters
