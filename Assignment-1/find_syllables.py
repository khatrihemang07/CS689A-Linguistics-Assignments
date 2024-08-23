vowels=['ऊ',
 'ॢ',
 'ॠ्',
 'ए',
 'ॡ',
 'औ',
 'अं',
 'ऌ',
 'अ',
 'ई',
 'उ',
 'ॣ',
 'ऑ',
 'ऎ',
 'इ',
 'ॄ',
 #'ह्',
 'ॠ',
 'ऒ',
 'ऐ',
 'ओ',
 'ॉ',
 'आ',
 '़']

def find_syllables(word):
    syllables=[]
    curr=[]
    for a in word:
        #print(a)
        curr.append(a)
        if a in vowels:
            syllables.append(curr)
            curr=[]
        #print(curr)
        #print(syllables)
    if curr:
        syllables.append(curr)
        curr=[]
    
    return syllables
