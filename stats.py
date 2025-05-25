def word_count(text):
    text = text.split()
    words_num = len(text)
    return words_num

def char_count(text):
    text = text.lower()
    char_dict = {}
    for ch in text:
        if ch in char_dict:
            char_dict[ch] += 1
        else:
            char_dict[ch] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    chars = []
    for ch in dict:
        if ch.isalpha():
            chars.append({"char": ch, "num": dict[ch]})
    chars.sort(reverse = True, key = sort_on)
    return chars