#Find the second largest element in a list using a for loop
import logging
logging.basicConfig(
    filename="sec_largest.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def sec_lar(n: list) -> int:
    """
    Finding second largest element in a list
    Parameters:
        nums (list): Input list
    Returns:
        int: Second Largest element in the list
    """
    logging.info("Finding second largest element in a list")
    second=n[0]
    largest=n[0]
    for i in n:
        if i>largest:
            second=largest
            largest=i
        elif i>second and i!=largest:
            second=i
    logging.info(f"Second largest element calculated: {second}")
    return second
            
n=eval(input("Enter string in list format: "))
print("Second largest element is: ",sec_lar(n))
