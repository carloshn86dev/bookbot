def count_num_words(text):
    words = text.split() 
    return len(words)

def get_num_times_in_string(text):
    chars = {}
    for c in text:
        lower_char = c.lower()
        try:
            val = chars[lower_char]
            chars[lower_char] = val + 1
        except KeyError:
            chars[lower_char] = 1
        except Exception as e:
            print(e)
    return chars

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    sorted_dict = []
    for k in dict:
        sorted_dict.append({
            "char" : k,
            "num" : dict[k]
        })
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict