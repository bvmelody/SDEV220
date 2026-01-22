# Name: Brenden Melody
# Module 2 Lab


"""
    """
    
    
DEANS_LIST: float = 3.5
DEANS_LIST_MESSAGE: str = "You have made the Dean's List"
HONOR_ROLL: float = 3.23
HONOR_ROLL_MESSAGE: str = "You made the Honor Roll"
SENTINEL: str = 'ZZZ'
INPUT_PROMPT1: str = 'Enter the first name: '
INPUT_PROMPT2: str = 'Enter the GPA: '
    
first_name: str = ''
gpa: float = 0.0

while first_name.upper() != SENTINEL:
    first_name = input(INPUT_PROMPT1)
    if first_name.upper() != SENTINEL:
        gpa = float(input(INPUT_PROMPT2))
        if gpa >= DEANS_LIST:
            print(DEANS_LIST_MESSAGE)
        elif gpa >= HONOR_ROLL:
            print(HONOR_ROLL_MESSAGE)
        else:
            break

        