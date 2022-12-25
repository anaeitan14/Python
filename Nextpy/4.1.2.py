def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}

    text = (words[word] for word in sentence.split())
    translated_text = ""
    for word in text:
        translated_text+=word+" "

    return translated_text

if __name__ == "__main__":
    print(translate("el gato esta en la casa"))

