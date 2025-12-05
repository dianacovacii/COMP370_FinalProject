# Side Chaaracter Dialogue Analysis in *The Office (US)*

This repository contains all files and resources used for the analysis of dialogue from four side characters (Jan, Oscar, Angela, and Toby) in The Office (US). The project aims to identify the topics each character tends to discuss and quantify their attention to these topics. This is the final project for COMP 370 (Introduction To Data Science) at McGill University. 

Contributors: 
Diana Covaci, Nara Yun, Hanjing Zheng


## Data 
- **'annotated_character_lines.csv'** - Finalized annotated dataset. 
- **'character_lines.csv'** - Uncleaned dataset of lines for the characters of interest. Includes trivial dialogue. 
- **'character_lines_1.csv'** - Cleaned dataset of lines for the characters of interest. Trivial dialogue was removed. 
- **'The-Office-Lines-V4.csv'** - Original dataset taken from Kaggle. 

---

## Code / Analysis

- **'analysis.py'** - Script for generating top word percentages and generating the stacked bar chart (Figure 7) for the report
- **'characterize.py'** - Script for computing tf-idf scores and saves top ten for each category in 'top_words_per_topic.json'
- **'collect_transcripts.py'** - Script that uses Kaggle API to obtain dataset, subsets on characters of interest and filters out short lines as preliminary trivial dialogue cleaning.
- **'count_lines.py'** - Script that gives a total for each character's lines. 
- **'COMP370_FinalReport.pdf'** - Final report write-up for the entire project. 
- **'LLM_summaries.md'** - The LLM generated summaries for every topic based on the top ten words of each cateogries (according to tf-idf score)
- **'top_words_per_topic.json'** - Top ten words of each topic according to tf-idf scores. 
- **'typology_starting_point.md'** - Topic starting point to be refined by open coding. 

--- 

## References

- **Dataset:** nasirkhalid24. (n.d.). *The Office (US) Complete Dialogue/Transcript* [Data set]. Kaggle. https://www.kaggle.com/datasets/nasirkhalid24/the-office-us-complete-dialoguetranscript
- **API Documentation:** Kaggle. (n.d.). *Kaggle API documentation: Interacting with Datasets* [Documentation]. Kaggle. https://www.kaggle.com/docs/api#interacting-with-datasets
