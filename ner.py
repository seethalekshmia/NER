import streamlit as st
from newspaper import Article
import spacy
from spacy import displacy
nlp= spacy.load("en_core_web_sm")

st.title("NLP DEMO")
url= st.text_input("Enter URL")


st.text('OR')

par=st.text_area('Enter Paragraph')

if st.button('Analyze'):



    if url:
        news= Article(url)
        news.download()
        news.parse()
        doc=nlp(news.text)
        name=displacy.render(doc,style='ent')
        st.markdown(name,unsafe_allow_html=True)
    elif par:
        doc=nlp(par)
        name=displacy.render(doc,style='ent')
        st.markdown(name,unsafe_allow_html=True)
    else:
        pass
        

    
