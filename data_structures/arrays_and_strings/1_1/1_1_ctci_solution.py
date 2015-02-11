__author__ = 'Joel'


def are_characters_unique(string):
    """
    ASCII characters (256)
    O(n)
    """
    char_checker_array = [False]*256
    for ch in string:
        if char_checker_array[ord(ch)] == True:
            return False
        else:
            char_checker_array[ord(ch)] = True
    return True


def main():
    #false
    print(are_characters_unique('The man is ok.'))
    #true
    print(are_characters_unique('Themanisok.'))
    #false
    print(are_characters_unique('Hello world!'))
    #False
    print(are_characters_unique('Helloworld!'))
    #false
    print(are_characters_unique('abababa'))
    #false
    print(are_characters_unique('aqwerta'))
    #True
    print(are_characters_unique('aqwertxc'))
    #true
    print(are_characters_unique('a'))
    #False
    print(are_characters_unique('  '))


if __name__ == "__main__":
    main()