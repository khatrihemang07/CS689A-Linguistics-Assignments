Question 1: 
import "correction.py" and use the method "correction".

Dependencies for Question 1: 
1) indic_transliteration
2) re

correction function takes String as input(without unicode correction) and give list of character as output(with unicode correction done). 

Question 2:
Run "Question2.ipynb"

Dependencies for Question 2:
1) custom_func.py
2) Counter from collections 

custom_func have 5 methods:
1) sort_dict(dictionary,reverse=True): 
Input: dictionary
Output: Sorted dictionary

2) uni_dict(tokens):
Input: list of tokens
Output: dictionary of frequency of unigram tokens

3) bi_dict(tokens):
Input: list of tokens
Output: dictionary of frequency of bigram tokens

4) syll_list(tokens):
Input: list of tokens
Output: list of all syllables

5) char_list(tokens):
Input: list of tokens
Output: list of all characters

custom_func use correction.py and find_syllables.py

find_syllables.py contains method find_syllables:
Input: list of characters(I have passed it after unicode correction)
Output: list of list of syllables


Question 3: Question3.txt

Question 4:
Run Question4.ipynb

Dependencies:
1) custom_func.py
2) indic_transliteration -> sanskrit
3) sentencepiece
4) collections -> Counter
5) transformers -> BertTokenizer, AutoModel, AutoTokenizer
6) nltk.tokenize -> WhitespaceTokenizer

Question 5:
Run Question5.ipynb

Dependencies:
Same as Question 4

Question 6:
Open Question6.txt


