import logging
logging.basicConfig(
    filename="remove_dup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def remove_dup(lis: list) -> list:
    """
    Remove duplicate elements while preserving order
    Parameters:
        lis (list): Input list
    Returns:
        list: List after removing duplicates
    """
    logging.info("Started removing duplicates from list")
    result = []
    for item in lis:
        if item not in result:
            result.append(item)
    logging.info(f"Duplicates removed successfully: {result}")
    return result
lis = eval(input("Enter the list: "))
print("List after removing duplicates:", remove_dup(lis))