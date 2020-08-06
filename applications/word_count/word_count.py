def word_count(s):
    d = {}
    
    for i in s.split(" "):
        i = i.lower()

        if i not in d:
            d[i] = 0
            print(f"This is the object growing, {d}")
        d[i] += 1
    
    return d



if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count('poz poz poz poz poz This is a test of the emergency broadcast network. This is only a test.'))