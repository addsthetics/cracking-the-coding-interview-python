def isSubstring(s1, s2):
    return s2 in s1


def isRotation(s1, s2):
    return isSubstring(s1+s1, s2)


def main():
    #true
    print(isRotation("erbottlewat", "waterbottle"))
    #true
    print(isRotation("ducksauce", "ceducksau"))
    #false
    print(isRotation("theman", "thmane"))

if __name__ == "__main__":
    main()