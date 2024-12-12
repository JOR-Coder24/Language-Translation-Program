# Language Translation Program

## Overview

This program allows users to translate text between various languages using language codes provided in an Excel file. The program supports repeated translations until the user chooses to exit.

## Features

- Reads language codes from an Excel file.
- Validates input to ensure correct language selection.
- Translates text between a user-specified source and target language.
- Allows users to perform multiple translations in a single session.

## Prerequisites

1. **Python Libraries**: Ensure the following libraries are installed:

   - `pandas`
   - `translate`
   - `openpyxl` (required for reading Excel files)

   Install missing libraries using pip:

   ```bash
   pip install pandas translate openpyxl
   ```

2. **Excel File**: An Excel file named `Languages.xlsx` (or another file specified in the `file_path` variable) containing the following columns:

   - `Language Name`: The name of the language (e.g., English, French).
   - `Code`: The corresponding ISO code for the language (e.g., en, fr).

## Usage

### Steps to Run

1. Save the script to a file, for example, `translator.py`.
2. Ensure the Excel file `Languages.xlsx` is in the same directory as the script or update the `file_path` variable to point to the correct file location.
3. Run the script:

   ```bash
   python translator.py
   ```

### Input and Output

1. **Source Language**: Enter the name of the language you want to translate from (e.g., `English`).
2. **Target Language**: Enter the name of the language you want to translate to (e.g., `French`).
3. **Phrase to Translate**: Provide the text you want to translate.
4. **Translation Result**: The program outputs the translated text.

### Example

#### Input:

```
Enter the source language (e.g., 'English', 'German') or 'exit' to quit: English
Enter the target language (e.g., 'French', 'Spanish') or 'exit' to quit: French
Enter a phrase to translate: Hello, how are you?
```

#### Output:

```
Translated text: Bonjour, comment ça va ?
```

## Error Handling

- **File Not Found**: If the specified Excel file is missing, the program exits with an appropriate error message.
- **Invalid Language**: If the user inputs a language not present in the Excel file, they are prompted to try again.
- **Translation Error**: Any issues during translation are caught and displayed to the user.

## Program Flow

1. Load the Excel file containing language codes.
2. Validate the presence of required columns (`Language Name` and `Code`).
3. Enter a loop for repeated translations:
   - Get the source language and find its ISO code.
   - Get the target language and find its ISO code.
   - Translate the user-provided text and display the result.
4. Exit the program when the user types `exit`.

## Notes

- Ensure that the `Languages.xlsx` file contains accurate and up-to-date ISO codes for all supported languages.
- The `translate` library may require an active internet connection to perform translations.

## License

This program is open-source and free to use for personal and educational purposes.

