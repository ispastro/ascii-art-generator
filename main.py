# main.py

from ascii_art.generator import text_to_ascii

def main():
    user_input = input("Enter text to convert to ASCII art: ")  # This line is critical
    result = text_to_ascii(user_input)
    print("\nASCII Art:\n")
    print(result)

if __name__ == "__main__":
    main()
