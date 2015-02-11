__author__ = 'Joel'


def are_characters_unique(string):
    """
    O(n)
    """
    string_dict = {}
    string = string
    for ch in string:
        if ch in string_dict:
            return False
        else:
            string_dict[ch] = True
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