def char_to_ascii(char):
    """Convert a single character to its ASCII representation."""
 
    CHAR_MAP = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
    index = ord(char) % len(CHAR_MAP)
    return CHAR_MAP[index]
def text_to_ascii(text):
   
   result =[]
   for char in text:
      if char == ' ':
         result.append(' ')
      else:
        
            ascii_char = char_to_ascii(char)
            result.append(ascii_char)
   return ''.join(result)
