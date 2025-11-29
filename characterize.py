'''
Usage: python3 characterize.py
'''
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import numpy as np
import json

df = pd.read_csv("data/annotated_character_lines.csv")
# print(df.head())

topic_docs = df.groupby("category")["line"].apply(lambda x: " ".join(x)).to_dict()
# print(topic_docs)




custom_stop_words = [
    "i'm", "you're", "we're", "he's", "she's", "it's", "that's", "there's", 
    "what's", "man", "fine", "certain", "bit",
    "can't", "would", "could", "don't", "didn't", "did", "does", 
    "going", "gonna", "want", "like", "think", "look", "stop", "say", "mean",
    "doing", "cause", "tell", "costs", "thing", 
    "need", "got", "sure", "talk", "let's", "let", "run", "having", "make",
    "just", "oh", "uh", "know", "really", "okay", "ok", "um", "yeah", "hey",
    "right", "wrong", "maybe", "good", "great", "little", "sorry", "new",
    "names", "michael", "pam", "dunder", "andy", "kevin", "oscar", "angela", "chad",
    "le", "dem", "guys", "things", "way", "come", "thought", "time", "yes", 
    "pum", "parum"
]

# Combine with sklearn's default stop words and convert to list
all_stop_words = list(ENGLISH_STOP_WORDS.union(custom_stop_words))

# Create vectorizer with combined stop words
vectorizer = TfidfVectorizer(
    stop_words=all_stop_words,  # pass the set here
    token_pattern=r"\b\w[\w']*\b"  # keep words with apostrophes
)

categories = list(topic_docs.keys())
docs = list(topic_docs.values())

tfidf_matrix = vectorizer.fit_transform(docs)
feature_names = vectorizer.get_feature_names_out()



top_words_per_topic = {}

for i, category in enumerate(categories):
    row = tfidf_matrix[i].toarray().flatten()
    top_indices = row.argsort()[-10:][::-1]
    top_words = [feature_names[idx] for idx in top_indices]
    top_words_per_topic[category] = top_words

top_words_per_topic
print(top_words_per_topic)

for topic, words in top_words_per_topic.items():
    print(f"Topic: {topic}")
    print("Top 10 TF-IDF words:", ", ".join(words))
    print()

with open("top_words_per_topic.json", "w") as f:
    json.dump(top_words_per_topic, f, indent=2)
