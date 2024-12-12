import pandas as pd
from translate import Translator

# Load the language codes from the Excel file
file_path = "Languages.xlsx"  # Replace with the path to your file
try:
    languages_df = pd.read_excel(file_path)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()

# Validate that the required columns exist
if 'Language Name' not in languages_df.columns or 'Code' not in languages_df.columns:
    print("Error: The Excel file must contain 'Language Name' and 'Code' columns.")
    exit()

print("Language translation program started.")

# Loop to allow repeated translation or exit
while True:
    # Get the source language input from the user
    start_language_name = input("Enter the source language (e.g., 'English', 'German') or 'exit' to quit: ").strip()

    # If the user wants to exit the program
    if start_language_name.lower() == "exit":
        print("Exiting the program.")
        break

    # Find the corresponding ISO code for the source language
    try:
        start_language_code = languages_df.loc[
            languages_df['Language Name'].str.casefold() == start_language_name.casefold(), 'Code'
        ].values[0]
    except IndexError:
        print(f"Error: '{start_language_name}' is not a valid language. Please try again.")
        continue

    # Get the target language input from the user
    end_language_name = input("Enter the target language (e.g., 'French', 'Spanish') or 'exit' to quit: ").strip()

    # If the user wants to exit the program
    if end_language_name.lower() == "exit":
        print("Exiting the program.")
        break

    # Find the corresponding ISO code for the target language
    try:
        end_language_code = languages_df.loc[
            languages_df['Language Name'].str.casefold() == end_language_name.casefold(), 'Code'
        ].values[0]
    except IndexError:
        print(f"Error: '{end_language_name}' is not a valid language. Please try again.")
        continue

    # Get the text to translate
    input_text = input("Enter a phrase to translate: ")

    # Create a Translator instance with the retrieved ISO codes
    translator = Translator(from_lang=start_language_code, to_lang=end_language_code)

    # Perform the translation
    try:
        converted_text = translator.translate(input_text)
        print("Translated text:", converted_text)
    except Exception as e:
        print("Error during translation:", e)
