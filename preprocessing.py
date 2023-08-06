import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from string import punctuation
ps = PorterStemmer()

def transform_text(text):
    # lowercase
    text = text.lower()
    # tokenization
    text = nltk.word_tokenize(text)
    
    # Removing special characters
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y.copy()
    y.clear()
    
    #Removing stop words and punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in punctuation:
            y.append(i)
            
    text = y.copy()
    y.clear()
    
    #Stemming
    for i in text:
        y.append(ps.stem(i))
    
            
    return " ".join(y)