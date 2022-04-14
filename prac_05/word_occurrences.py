word_count = {}
text = input("Text: ")
words_in_text = text.split()
for word in words_in_text:
    frequency = word_count.get(word, 0)
    word_count[word] = frequency + 1
words_in_text = list(word_count.keys())
words_in_text.sort()
max_length = max((len(word) for word in words_in_text))
for word in words_in_text:
    print(f"{word:{max_length}} : {word_count[word]}")