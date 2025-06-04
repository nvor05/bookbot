def get_book_text(file_path):
    with open(str(file_path)) as f:
        return f.read() 

def get_num_words(text):
    words=text.split()
    num_words=len(words)
    return num_words


def each_character_num(content):
    character_dict = {}
    for character in content.lower():
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict


def sort_on(dict):
    return dict["num"]

def sorted_report(dictionary):
    list_of_dict=[]
    for char, num in dictionary.items():
        dict = {"char": char , "num":num}
        list_of_dict.append(dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict
   