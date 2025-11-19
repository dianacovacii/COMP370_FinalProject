import pandas as pd

df = pd.read_csv('data/character_lines_1.csv')

characters_of_interest = ['Jan', 'Oscar', 'Angela', 'Toby']
char_df = df[df['speaker'].isin(characters_of_interest)]

print("=== CURRENT LINE COUNTS ===\n")
for char in characters_of_interest:
    count = len(char_df[char_df['speaker'] == char])
    print(f"{char}: {count} lines")

print(f"\nTotal lines: {len(char_df)}")

print("\n=== NEED TO REMOVE ===\n")
for char in characters_of_interest:
    count = len(char_df[char_df['speaker'] == char])
    to_remove = max(0, count - 500)
    print(f"{char}: Remove ~{to_remove} lines (keep 500)")