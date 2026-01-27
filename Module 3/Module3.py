def convert_far_to_cel(far: float) -> float:
    """convert far to cel

    Args:
        far (float): _description_

    Returns:
        float: _description_
    """

def my_func(p1: str, p2: str, p3: int = 0):
    pass

my_func(p1='test', p2='test2')

the_tuple: tuple = (1,2,3,4)

the_list: list = [1,2,3,4]

the_list[0] = 6

letters: dict = {}

ltr: dict = {
    1: 'one',
    2: 'two',
    3: 'three'
}

phrase: str = "The quick brown fox jumps over the lazy dog."

for char in letters:
    if letters.get(char) is None:
        letters[char] = 1
    else:
        letters[char] += 1

for key, value in ltr.items():
    print(key, value)

word = 'letters'
letter_cunts = {letter: word.count(letter) for letter in set(word)}