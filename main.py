import sys
from collections import Counter

def get_book_text(path):
    """Read contents"""
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    return file_contents

def get_word_count(text):
    """Split text into words"""
    words = text.split()

    """Length is word count"""
    return len(words)

def get_character_count(text):
    """Convert to lower case"""
    lower_text = text.lower()

    """Count characters"""
    counter = Counter(lower_text)

    return counter

def filter_character_count(count):
    """Filter count to only alphabet characters
       and convert to list of dictionaries"""
    filtered_count = []

    for key in count:
        if key.isalpha():
            item = { "character": key, "count" : count[key] }
            filtered_count.append(item)

    return filtered_count

def sort_on(dict):
    """Sort on count field of dictionary"""
    return dict["count"]

def create_report(book_path, word_count, sorted_count):
    """Report header"""
    report = f"--- Begin report of {book_path} ---\n"
    
    """Word count"""
    report += f"{word_count} words found in the document\n\n"

    """Character counts"""
    for item in sorted_count:
        character = item['character']
        count = item['count']
        
        report += f"The '{character}' character was found {count} times\n"
        
    """Footer"""
    report += "--- End report ---"
    
    return report

def main() -> int:
    book_path = "books/frankenstein.txt"

    """Read contents"""
    book_text = get_book_text(book_path)

    """Count words"""
    word_count = get_word_count(book_text)

    """Count characters"""
    character_count = get_character_count(book_text)

    """Filter"""
    filtered_character_count = filter_character_count(character_count)

    """Sort"""
    filtered_character_count.sort(reverse=True, key=sort_on)

    """Create report"""
    report = create_report(book_path, word_count, filtered_character_count)

    print(report)

if __name__ == '__main__':
    sys.exit(main())
