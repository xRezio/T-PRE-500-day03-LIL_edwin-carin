sentence = "This is a test. Is it possible to fly? Good things come to those who never give up."
sentences = sentence.replace("?", ".").split('.')
first_words = []

for s in sentences:
    words = s.strip().split()
    if words:
        first_words.append(words[0])

join_sentence = ' '.join(first_words)
print(join_sentence)