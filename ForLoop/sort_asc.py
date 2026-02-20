import logging
logging.basicConfig(
    filename="sort_asc.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def sort_asc(lis: list) -> str:
    """
    Checks whether the given list is in ascending order
    Parameter: lis (list)
    Returns: message (str)
    """
    logging.info("Started checking list order")
    count = 0
    length = len(lis)
    for i in range(0, length-1):
        if lis[i] <= lis[i + 1]:
            count += 1
    if count == length-1:
        logging.info("List is in ascending order")
        return "Ascending Order"
    else:
        logging.info("List is not in ascending order")
        return "Not Ascending Order"
result = sort_asc([5, 4, 3, 2])
print(result)