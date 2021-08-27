import re

texts = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]


word_counts = {}
for count, i in enumerate(texts):
    cleaned_sentence = re.sub(r"[^a-zA-Z0-9]", " ", i)
    list_of_words = list(cleaned_sentence.lower().split())
    for word in list_of_words:
        if word in word_counts:
            value = word_counts.get(word)
            (count_word, count_sentence) = value
            existing_count = int(count_word)
            word_counts[word] = (existing_count + 1, count_sentence)
        else:
            word_counts[word] = (1, count)
for k, v in word_counts.items():
    values = v
    (count_word, count_sentence) = values
    print(k, count_word, count_sentence)