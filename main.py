import re
import json

def load_words_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def check_letters(word, required_letters):
    word = word.lower()
    return all(letter in word for letter in required_letters)

def filter_words(words, pattern, excluded_letters, included):
    filtered_words = []
    for word in words.keys():
        word_lower = word.lower()
        if len(word_lower) == 5 and re.fullmatch(pattern, word_lower) and not any(letter in excluded_letters for letter in word_lower):
            if check_letters(word_lower, included):
                filtered_words.append(word)
    return filtered_words

def main():
    file_path = 'russian_nouns_with_definition.json'
    words_data = load_words_from_json(file_path)

    pattern = input("Введите шаблон слова (используйте '*' для неизвестной буквы): ")
    included = input("Введите буквы, которые можно использовать (без пробелов): ")
    excluded_letters = input("Введите буквы, которые нельзя использовать (без пробелов): ")

    pattern = pattern.replace('*', r'\w')
    excluded_letters = set(excluded_letters)
    included = set(included)

    filtered_words = filter_words(words_data, pattern, excluded_letters, included)

    print("\nСлова, соответствующие заданным условиям:")
    for word in filtered_words:
        print(f"Слово: {word}\n   Объяснение: {words_data[word]['definition']}\n")

if __name__ == "__main__":
    main()
