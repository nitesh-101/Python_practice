#Print frequency of each character in a string
import logging
logging.basicConfig(
    filename="freq_char.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def count_frequency(s: str) -> dict:
    """
    Count the frequency of each character in a given string.
    Parameters:
        s (str): Input string
    Returns:
        dict: Dictionary containing character frequencies.
    """
    logging.info("Counting frequency of characters in the string")
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    logging.info(f"Character frequency calculated: {freq}")
    return freq
s = input("Enter the string: ")
result = count_frequency(s)
print("Character Frequency:")
for ch in result:
    print(ch, ":", result[ch])