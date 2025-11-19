from kaggle.api.kaggle_api_extended import KaggleApi
import os
import pandas as pd


def get_kaggle_dataset(): 
  file_path = 'data/The-Office-Lines-V4.csv'
  if not os.path.exists(file_path): 
    api = KaggleApi()
    api.authenticate()

    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)

    dataset = "nasirkhalid24/the-office-us-complete-dialoguetranscript"
    api.dataset_download_files(dataset, path=file_path, unzip=True)


def get_lines_of_interest(all_lines): 
  characters_of_interest = ['Jan', 'Oscar', 'Angela', 'Toby']
  lines_of_interest = all_lines[all_lines['speaker'].isin(characters_of_interest)]
  return lines_of_interest


def remove_short_lines(lines): 
  long_lines = lines[lines['line'].str.split().str.len() > 2]
  return long_lines


if __name__ == '__main__': 
  get_kaggle_dataset()
  all_lines = pd.read_csv('data/The-Office-Lines-V4.csv')
  character_lines = get_lines_of_interest(all_lines)
  character_lines = remove_short_lines(character_lines)
  character_lines.to_csv('data/character_lines_1.csv', index=False)