
def print_all_letters(word):
    for character in word:
        print(character)


def print_letters_with_index(word):

    index = 0
    for letter in word:
        print(index, letter)
        index += 1

def length(some_list):

    count = 0
    for item in some_list:
        count += 1

    return count


# print_all_letters("Word")
# print_letters_with_index("Hello")

my_list = ["bird", "Cat", "Dog"]
print(length(my_list))



