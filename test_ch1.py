#function that takes a string argument
#and returns the vowels on it

def vowel_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for ch in string.lower():
        if ch in vowels:
            count += 1
    return count


def test_with_my_first_name():
    assert vowel_count('mario') == 3
   
def test_with_my_last_name():
    assert vowel_count('gamboa') == 3
