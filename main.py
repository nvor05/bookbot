import sys
from stats import get_book_text
from stats import get_num_words
from stats import each_character_num
from stats import sorted_report

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_text = get_book_text(sys.argv[1])
character_num = each_character_num(book_text)
final_report=sorted_report(character_num)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}")
print("----------- Word Count ----------")
print(f"Found {get_num_words(book_text)} total")
print("--------- Character Count -------")

for report in final_report: 
    character = report["char"]
    count = report["num"]
    if character.isalpha():
        print(f"{character}: {count}")

print("============= END ===============")