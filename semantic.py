import spacy

print("_____________________en_core_web_md_____________________")
nlp_md = spacy.load('en_core_web_sm')

word1 = nlp_md("cat")
word2 = nlp_md("monkey")
word3 = nlp_md("banana")

print(word1.similarity(word2))
# Cat and monkey have similarity of 0.59
print(word3.similarity(word2))
# Banana and monkey have similarity of 0.40
print(word3.similarity(word1))
# Banana and cat have similarity of 0.22

# Weirdly enough, a cat is more similar to a monkey than a banana. But even odder is the fact that a banana is mor similar to a monkey than to a cat. Must be because apes are thought to love'nanas more than cats.


# print("_____________________en_core_web_sm_____________________")
nlp_sm = spacy.load('en_core_web_sm')

word1 = nlp_sm("cat")
word2 = nlp_sm("monkey")
word3 = nlp_sm("banana")
# The following prints of similarity will yield the following error:
# UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


# I will try now with three other words:
print("_____________________en_core_web_md_____________________")
nlp_md = spacy.load('en_core_web_sm')

word1 = nlp_md("car")
word2 = nlp_md("wheel")
word3 = nlp_md("bolt")

print(f"Similarity between {word1} and {word2}")
print(word1.similarity(word2))
print(f"Similarity between {word3} and {word2}")
print(word3.similarity(word2))
print(f"Similarity between {word3} and {word1}")
print(word3.similarity(word1))

# Makes sense that bolt is closer to wheel and wheel is closer to car than bolt to car
