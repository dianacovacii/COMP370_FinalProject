'''
Usage: python3 analysis.py
'''
import pandas as pd
from collections import Counter
import string
import matplotlib.pyplot as plt

# Load annotated CSV
df = pd.read_csv("data/annotated_character_lines.csv")



## Word Counts and Percentages for Top 10 Words

# Top 10 words per topic (from TF-IDF)
top_words_per_topic = {
    'HR': ['company', 'hr', 'branch', 'fired', 'corporate', 'offer', 'policy', 'lawyer', 'behavior', 'review'], 
    'Humour': ['pies', 'queen', 'princess', 'baby', 'weirdo', 'sleeping', 'caterer', 'help', 'god', 'blake'], 
    'Interpersonal': ['son', 'stressed', 'senator', 'worth', 'calling', 'thinking', 'feel', 'help', 'talking', 'phyllis'], 
    'Logistics': ['party', 'branch', 'planning', 'office', 'work', 'committee', 'mifflin', 'hour', 'board', 'corporate'], 
    'Opinions': ['nope', 'people', 'better', 'hot', 'art', 'kind', 'angry', 'deserves', 'coincidence', 'fun'], 
    'Personal': ['gay', 'wife', 'senator', 'cat', 'sprinkles', 'wedding', 'husband', 'knew', 'love', 'wanted']    
    }
    

results = {}


for topic, top_words in top_words_per_topic.items():
    # Select all lines in this topic
    lines = df[df["category"] == topic]["line"].str.lower()
    # Remove punctuation from each line
    lines_clean = lines.apply(lambda x: x.translate(str.maketrans("", "", string.punctuation)))
    # Count words
    word_counts = Counter(" ".join(lines_clean).split())
    # Keep only top_words
    counts = {w: word_counts.get(w, 0) for w in top_words}
    # Calculate percentages
    total_words = sum(word_counts.values())
    percentages = {w: round(c / total_words * 100, 2) for w, c in counts.items()}
    results[topic] = {"counts": counts, "percent": percentages}

# Print data
for topic, data in results.items():
    print(f"Topic: {topic}")
    print("Counts:", data["counts"])
    print("Percentages:", data["percent"])
    print()




## Topic Distribution per Character

# Count number of lines per character per topic
char_topic_counts = df.groupby(["speaker", "category"])["line"].count().unstack(fill_value=0)

# Plot stacked bar chart
char_topic_counts.plot(kind='bar', stacked=True, figsize=(10,6))
plt.title("Number of lines per topic per character")
plt.xlabel("Character")
plt.ylabel("Number of lines")
plt.legend(title="Topic", bbox_to_anchor=(1.05,1), loc='upper left')
plt.tight_layout()
plt.show()
