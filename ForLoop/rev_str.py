import logging
logging.basicConfig(
    filename="rev_str.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def rev_str(s: str) -> str:
    """
    Reverse string
    Parameters:
        s (str): Input string
    Returns:
        str: Reversed string
    """
    logging.info("Started reversing the string")  
    rev = ""
    for ch in s:
        rev = ch + rev
    logging.info(f"String reversed successfully: {rev}")
    return rev
s = input("Enter a string: ")
result = rev_str(s)
print("Reversed string:", result)