__author__ = 'Joel'


def are_characters_unique(string):
    """
    O(n^2)
    """
    #TODO:Improve this using divide and conquer if manipulation is allowed.
    string_length = len(string)
    i = 0
    if string_length > 1:
        while i < string_length:
            j = i + 1
            while j < string_length:
                if string[i] == string[j]:
                    return False
                j += 1
            i += 1
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