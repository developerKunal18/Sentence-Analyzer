sentence = input("Enter a sentence: ")

characters = len(sentence)
words = len(sentence.split())
vowels = 0
consonants = 0

for char in sentence.lower():
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("\nSentence Analysis")
print("Characters:", characters)
print("Words:", words)
print("Vowels:", vowels)
print("Consonants:", consonants)
