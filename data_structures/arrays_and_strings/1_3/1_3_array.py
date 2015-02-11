__author__ = 'Joel'


def is_permutation(string1, string2):
    """0(n)"""
    if len(string1) != len(string2):
        return False
    char_tracker_array_string1 = [0] * 256
    char_tracker_array_string2 = [0] * 256
    for ch in string1:
        char_tracker_array_string1[ord(ch)] += 1

    for ch2 in string2:
        char_tracker_array_string2[ord(ch2)] += 1

    for i in range(0, 255):
        if char_tracker_array_string2[i] != char_tracker_array_string1[i]:
            return False

    return True


def main():
    #true
    print(is_permutation("ABC", "BAC"))
    #false
    print(is_permutation("ABC", "BCC"))
    #True
    print(is_permutation("ABC", "BCA"))
    #true
    print(is_permutation("silent","listen"))

if __name__ == "__main__":
    main()