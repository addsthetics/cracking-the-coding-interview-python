def spacify(string):
    string_array = []
    #NOTE: Does not take into account that you know the "true" length of the string.
    #Reread the questions.
    for ch in string:
        if len(string_array) == len(string):
            return "".join(string_array)
        if ch == " ":
            string_array.append("%")
            string_array.append("2")
            string_array.append("0")
        else:
            string_array.append(ch)


def main():
    #true
    print(spacify("Mr John Smith    ") == "Mr%20John%20Smith")
    print(spacify("Mr John Smith    "))
    #true
    print(spacify("Joel  Paulino    ") == "Joel%20%20Paulino")
    print(spacify("Joel  Paulino    "))

if __name__ == "__main__":
    main()