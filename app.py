
import cv2
import numpy as np
import streamlit as st
import requests
import os
import nltk
#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Home UI 

def main():

    st.set_page_config(layout="wide")

    font_css = """
        <style>
        button[data-baseweb="tab"] {
        font-size: 26px;
        }
        </style>
        """

    st.write(font_css, unsafe_allow_html=True)
    translate()

# POS_TAGGER_FUNCTION 
def pos_tagger(word,nltk_tag):
    if word.endswith("ing"):
        return wordnet.VERB
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:         
        return None
    
def translate():
    st.header("English to ISL Translation")
    txt = st.text_input('Engligh Text')

    st.write("Input text is", txt)
    
    lemmatizer = WordNetLemmatizer()
    stop_words_isl = {"a", "an" ,"the", "is", "am", "are"}
    tokenized = sent_tokenize(txt)
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    
    st.subheader("English Text")
    
    for i in tokenized:
      
        # Word tokenizers is used to find the words 
        # and punctuation in a string
        wordsList = nltk.word_tokenize(i)
    
        # removing stop words from wordList
        wordsList = [w for w in wordsList if not w in stop_words_isl] 


        #  Using a Tagger. Which is part-of-speech 
        # tagger or POS-tagger. 
        tagged = nltk.pos_tag(wordsList)
  
        #print(tagged)
        # we use our own pos_tagger function to make things simpler to understand.
        wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[0],x[1])), tagged))
        #print(wordnet_tagged)

        lemmitization_dict = dict()

        for word, tag in wordnet_tagged:
            if tag is None:
                # if there is no available tag, append the token as is
                lemmatized_sentence.append(word)
            else:       
                # else use the tag to lemmatize the token
                lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
                lemmitization_dict[word] = lemmatizer.lemmatize(word, tag)
    
        st.write(lemmatized_sentence)

    
      
    st.subheader("ISL Gloss")
    st.subheader("ISL Vid")

   
if __name__ == "__main__":
    main()
