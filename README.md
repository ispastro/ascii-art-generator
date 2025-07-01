# 🎨 ASCII Art Generator

A minimalist and fun Python-based tool that converts plain text into stylized ASCII art using a customizable character map.

---

## 🚀 Features

- 🔤 Converts text into ASCII-style representation
- 🎯 Clean modular code structure using `text_to_ascii()` and `char_to_ascii()` functions
- ✅ Unit-tested with `pytest`
- 📦 Modern Python best practices with virtual environments
- 💻 CLI interface for quick conversion

---

## 📂 Project Structure

ascii-art-generator/
│
├── ascii_art/
│ └── generator.py # Core logic for ASCII art generation
│
├── tests/
│ └── test_generator.py # Unit tests using pytest
│
├── main.py # CLI interface
├── requirements.txt # Python dependencies (optional)
└── README.md # You're here :)



---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/ascii-art-generator.git
cd ascii-art-generator

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate    # On Windows
# Or: source venv/bin/activate   # On Linux/Mac

# Install dependencies
pip install -r requirements.txt
✅ Running the Project
bash

python main.py
You'll be prompted to enter a string. The tool will display the ASCII representation using characters like @, #, %, and .

🧪 Run Tests
on bash
python -m pytest
Make sure all tests pass before making changes to the logic.

🧠 How It Works
Each character from input is transformed using ord() to map it to a character in CHAR_MAP.

Spaces are preserved for clean formatting.

ASCII art is returned as a stylized string.

📄 Example Output
Input: hi

Output:

 ?  +

🧰 Dependencies
Python 3.8+

pytest

flake8 (optional for linting)

📌 Best Practices Used
✅ Modular file structure

✅ Test-driven development

✅ Virtual environment support

✅ Clean, readable code

✅ Follows PEP8 standards

🧑‍💻 Author
Made with ❤️ by Haile Asaye

📃 License
This project is licensed under the MIT License.



---

Let me know if you want to [turn this project into a CLI tool using `argparse`](f), [upload it to GitHub with commit messages](f), or [add more character sets for fonts](f)!








