from ascii_art.generator import text_to_ascii
def test_text_to_ascii():
    # Test with a simple string
     result = text_to_ascii("Hi")
     assert isinstance(result, str)
     assert len(result)> 0
    