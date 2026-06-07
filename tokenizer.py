# Bengali Strata Tokenizer
# Classifies words into tatsama, tadbhava, desi


def classify_word(word):
    """

    Returns the stratum for a Bengali word.
    tatsama = direct Sanskrit loan
    tadbhava = Sanskrit modified through prakrit
    desi = indigenous
    """


    # Tatsama examples - direct Sanskrit
    tatsama = ["pita","surya","karma","chandra","krishna","bidyut"]


    # Tadbhava examples - Sanskrit word modified through prakrit
    tadbhava = ["rat","hat","kan","dham","aj"] # from ratri, hasta, karna, dharma, adya


    # Desi examples - native Bengali
    desi = ["khoka","khal","doba","chingri","dhol","kukur"]


    if word in tatsama:
       return "tatsama"
    elif word in tadbhava:
       return "tadbhava"
    elif word in desi:
       return "desi"
    else:
       return "unknown"


# Test it
print(classify_word("surya")) # should print: tatsama
print(classify_word("rat")) # should print: tadbhava
print(classify_word("khoka")) # should print: desi

def classify_sentence(sentence):
    words = sentence.split()
    return [classify_word(word) for word in words]

# Test with sentences - demo data only, meaning not important
print(classify_sentence("aj surya doba"))
print(classify_sentence("khoka rat bidyut"))
print(classify_sentence("pita dhol dham"))
