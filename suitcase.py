import regex as re
import mmh3

def OwnBagWords(datalines):
        #Initializing a list which will hold lists, one for every text request
    wordlines = []
    #Initializing a set holding all unique words
    allwords = set()
    
    for stringline in datalines:    

        clean_text = GetOnlyWords(stringline)
        #Collect each word list of every text request
        wordlines.append(clean_text)
        #Collect all the words that appear
        allwords = allwords.union(clean_text)
    
    #Create a dictionary to know where each word should be in the word list
    word_list = sorted(list(allwords)) #All the unique words in a list sorted
    values = list(range(len(allwords))) # [0,1,2,3,....]
    dct = dict(zip(word_list, values))
        
    #The counting "matrix" (lists in a list) created
    mat=list()
    
    #Loop through each text_request line
    for j in range(len(wordlines)):
        
        #Initialize a list with zeros as long a the number of unique words
        lst = list([0]*len(word_list))
        
        #Loop through all words in text_request line and put the correct number in.
        for word in wordlines[j]:
            lst[dct[word]] +=1
        
        #Append the counting list into the "counting matrix"
        mat.append(list(lst))

    return mat

def OwnBagWordsHashing(datalines,buckets):
    #The counting "matrix" (lists in a list) created
    mat=list()
    
    for stringline in datalines:   
        #Initialize a list with zeros as long a the number of unique words
        lst = list([0]*buckets) 

        #Get the words in string e.g. ['hi','I','am','nice']
        clean_text = GetOnlyWords(stringline)

        for word in clean_text:
            hashed_token = mmh3.hash(word) % buckets
            lst[hashed_token] += 1
        mat.append(list(lst))

    return mat


def GetOnlyWords(stringline):
    #Get the correct text string and convert to lower case
    textstr = stringline.lower()
    #Use regex to clean words and convert the string into list of words
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',textstr)
    #regex for getting words but still include word with apostrophe e.g. "can't" and no underscores.
    reg = r'\b[^\W_]*\'?[^\W_]+\b'
    clean_text = re.findall(reg,textstr.strip())
    #Add the emoticons to the line as a word.
    clean_text = clean_text + emoticons
    
    return clean_text




