#utilities of nltk package
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import string, sys

def get_wordnetpos(nltk_pos):
    if nltk_pos.startswith('J'):
        return wordnet.ADJ
    elif nltk_pos.startswith('N'):
        return wordnet.NOUN
    elif nltk_pos.startswith('V'):
        return wordnet.VERB
    elif nltk_pos.startswith('R'):
        return wordnet.ADV
    else:
        return ''
    
def remove_stopwords(content):
    clean_list = list()
    word_list = word_tokenize(content)
    for word in nltk.pos_tag(word_list):
#         print(word)
        if word[0].lower() not in stopwords.words('english'):
            clean_list.append(word[0])

    return ' '.join(clean_list)

def remove_punctuations(content):
    clean_list = list()
    word_list = word_tokenize(content)
    for word in nltk.pos_tag(word_list):
        if word[1] not in string.punctuation and word[0] not in string.punctuation:
            clean_list.append(word[0])
    
    return ' '.join(clean_list)

def remove_numbers(content):
    clean_list = list()
    word_list = word_tokenize(content)
    for word in nltk.pos_tag(word_list):
        if word[1] != 'CD':
            clean_list.append(word[0])
    
    return ' '.join(clean_list)

def lemmatize_content(content):
    wordnet_lemma = WordNetLemmatizer()
    lemma_list = list()
    word_list = word_tokenize(content)
    for word in nltk.pos_tag(word_list):
        wordnet_tag = get_wordnetpos(word[1])
        if wordnet_tag == '':
            lemma_list.append(wordnet_lemma.lemmatize(word[0]))
        else:
            lemma_list.append(wordnet_lemma.lemmatize(word[0], wordnet_tag))
    return ' '.join(lemma_list)

def complete_clean_content(content):
    return remove_numbers(remove_punctuations(remove_stopwords(lemmatize_content(content))))