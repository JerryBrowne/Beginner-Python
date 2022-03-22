def count(character_to_count, word):

    # "a", "abba"

    count = 0
    for letter in word:
        if letter == character_to_count:
            count += 1

    return count

def occurs(character, word):

    for letter in word:
        if character == letter:
            return True

    return False

print(occurs("a", "abba"))
print(occurs("c", "abba"))


#print(count("a", "abba"))
#print(count("z", "zoo"))

