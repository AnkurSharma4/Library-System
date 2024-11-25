# Skill Circle Library System

Welcome to the **Skill Circle Library System**! This is a simple Python program that provides information about books in the *Diary of a Wimpy Kid* series, allowing users to view details such as title, author, and price. The system provides an interactive user experience, where users can choose books and decide whether to continue or exit.

## Features

- **Book Information:** Users can view details for several books in the *Diary of a Wimpy Kid* series, including title, author, and price.
- **Continue or Exit:** After viewing book details, users are given the option to continue browsing or exit the system.
- **Interactive Interface:** The program allows users to interact through numeric choices, making it easy to navigate.

## Instructions

1. **Start the System:** The program starts by displaying the library system's title and then prompts the user to select a book.
2. **Select a Book:** The user can choose from six available books, each offering the following details:
   - Book Title
   - Author
   - Price
3. **Continue or Exit:** After each book's information is displayed, the user is asked if they want to continue to see another book or exit the system.

## How to Run the Program

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `library_system.py` file is located.
4. Run the program using Python by typing:
   ```bash
   python library_system.py
   ```
5. Follow the on-screen prompts to explore the library.

## Example System

```
                                                 Skill Circle Library System                                                         

Press 1 for 101 Book Information
Press 2 for 102 Book Information
Press 3 for 103 Book Information
Press 4 for 104 Book Information
Press 5 for 105 Book Information
Press 6 for 106 Book Information: 1

Book Title:-Diary of a Wimpy Kid, The Ugly Truth
Author:-Jeff Kinney
Price:-$5.00

Do you wish to continue?
Press 1 for Again
Press 2 to Exit: 1

Press 1 for 101 Book Information
Press 2 for 102 Book Information
Press 3 for 103 Book Information
Press 4 for 104 Book Information
Press 5 for 105 Book Information
Press 6 for 106 Book Information: 2

Book Title:-Diary of a Wimpy Kid, The Third Wheel
Author:-Jeff Kinney
Price:-$4.00

Do you wish to continue?
Press 1 for Again
Press 2 to Exit: 2

Goodbye
```

In this example:
- The user selects book 1 and sees its details.
- They are then asked if they want to continue. Choosing "1" brings them back to the book selection.
- If they choose "2" after any book, the program ends with a "Goodbye."

## Code Breakdown

1. **Initial Prompt:** The program prints the welcome message "Skill Circle Library System" and shows the options to view book information.
2. **Book Selection:** The user is prompted to input a number (1 to 6) to select a book.
3. **Information Display:** Depending on the selected number, the program prints the book's title, author, and price.
4. **Continue or Exit:** After displaying the book details, the program asks if the user wants to continue or exit. If the user chooses "1," the process restarts; if "2," the program ends.

## Requirements

- **Python 3.x** is required to run the program.
- No additional libraries are needed; the program uses basic Python functionality.

## How to Contribute

1. Fork the repository to your own GitHub account.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Submit a pull request describing your changes.

## License

This project is licensed under the MIT License.

---

This README provides an overview of how to interact with the Skill Circle Library System, instructions on running it, and sample gameplay, making it suitable for users and contributors on GitHub.
