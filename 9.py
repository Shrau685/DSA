def binary_search(dictionary, word):
    left, right = 0, len(dictionary) - 1
    while left <= right:
        mid = (left + right) // 2
        if dictionary[mid]['word'] == word:
            return dictionary[mid]['definition']
        elif dictionary[mid]['word'] < word:
            left = mid + 1
        else:
            right = mid - 1
    return None

# Updated dictionary
dictionary = [
    {'word': 'antelope', 'definition': 'A fast-running deer-like mammal found in Africa and Asia.'},
    {'word': 'blueberry', 'definition': 'A small, round, blue-purple fruit that is sweet and juicy.'},
    {'word': 'cucumber', 'definition': 'A long, green vegetable often eaten in salads.'},
    {'word': 'dragonfruit', 'definition': 'A tropical fruit with a scaly pink skin and white or red flesh.'},
    {'word': 'fig', 'definition': 'A soft fruit with a thin skin that is either green or purple.'}
]

# Get word from user and search
word_to_find = input("Enter the word to search for: ").strip().lower()
definition = binary_search(dictionary, word_to_find)
if definition:
    print(f"Definition of '{word_to_find}': {definition}")
else:
    print("Word not found.")
