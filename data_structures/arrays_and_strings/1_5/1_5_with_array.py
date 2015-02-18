def compress_string(string):
    res = []
    temp = ""
    index = 0
    string_length = len(string)

    for ch in string:
        if index + 1 == string_length:
            return string
        elif temp != ch:
            count = 1
            temp = ch
            res.append(temp)
            res.append(str(count))
            index = len(res) - 1
        else:
            count += 1
            res[index] = str(count)

    return "".join(res)


def main():
    #True
    print(compress_string("a") == "a")
    #False
    print(compress_string("aabbcc") == "a2b2c2")
    #True
    print(compress_string("aabcccccaaa") == "a2b1c5a3")
    print(compress_string("aabcccccaaa"))
    print(compress_string("aabccdeeeaa"))


if __name__ == "__main__":
    main()