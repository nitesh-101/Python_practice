import logging
logging.basicConfig(
    filename="missing_num.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def missing_num(l: list) -> list:
    """
    Find all missing numbers in a list
    Parameters:
        l (list): Input list
    Returns:
        list: Missing numbers
    """
    logging.info("Started finding missing numbers")
    missing = []
    for i in range(1, max(l) + 1):
        if i not in l:
            missing.append(i)
    logging.info(f"Missing numbers are: {missing}")
    return missing
l = eval(input("Enter the list: "))
print("Missing numbers are:", missing_num(l))