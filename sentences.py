import random
def main():
   test(1, "past")
   test(1, "present")
   test(1, "future")
   test(69, "past")
   test(420, "present")
   test(666, "future")
 
def test(quantity, tense):
    determinator = get_determinator(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    phase = get_prepositional_phrase(quantity)
    print(f"{determinator} {noun} {verb} {phase}.")
    
def get_determinator(quantity):
    # """Return a randomly chosen determiner. A determiner is
    # a word like "the", "a", "one", "some", "many".
    # If quantity == 1, this function will return either "a",
    # "one", or "the". Otherwise this function will return
    # either "some", "many", or "the".

    # Parameter
    #     quantity: an integer.
    #         If quantity == 1, this function will return a
    #         determiner for a single noun. Otherwise this
    #         function will return a determiner for a plural
    #         noun.
    # Return: a randomly chosen determiner.
    # """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    # """Return a randomly chosen noun.
    # If quantity == 1, this function will
    # return one of these ten single nouns:
    #     "bird", "boy", "car", "cat", "child",
    #     "dog", "girl", "man", "rabbit", "woman"
    # Otherwise, this function will return one of
    # these ten plural nouns:
    #     "birds", "boys", "cars", "cats", "children",
    #     "dogs", "girls", "men", "rabbits", "women"

    # Parameter
    #     quantity: an integer that determines if
    #         the returned noun is single or plural.
    # Return: a randomly chosen noun.
    # """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    # Randomly choose and return a noun
    
    word=random.choice(words)
    return word

def get_verb(quantity, tense):
    #  """Return a randomly chosen verb. If tense is "past",
    # this function will return one of these ten verbs:
    #     "drank", "ate", "grew", "laughed", "thought",
    #     "ran", "slept", "talked", "walked", "wrote"
    # If tense is "present" and quantity is 1, this
    # function will return one of these ten verbs:
    #     "drinks", "eats", "grows", "laughs", "thinks",
    #     "runs", "sleeps", "talks", "walks", "writes"
    # If tense is "present" and quantity is NOT 1,
    # this function will return one of these ten verbs:
    #     "drink", "eat", "grow", "laugh", "think",
    #     "run", "sleep", "talk", "walk", "write"
    # If tense is "future", this function will return one of
    # these ten verbs:
    #     "will drink", "will eat", "will grow", "will laugh",
    #     "will think", "will run", "will sleep", "will talk",
    #     "will walk", "will write"

    # Parameters
    #     quantity: an integer that determines if the
    #         returned verb is single or plural.
    #     tense: a string that determines the verb conjugation,
    #         either "past", "present" or "future".
    # Return: a randomly chosen verb."""
    if quantity == 1: 
        past_tense = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    else:
        print()

        if quantity == 2:
            present_tense = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    
            if quantity == 3:
                future_tense = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
            else:
                print() 
 
    word=random.choice(tense)
    return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    preposition = ("about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without")
    
    preposition = random.choice(preposition)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determinator = get_determinator(quantity)
    noun= get_noun(quantity)
    prepositional_phrase = (f"{preposition} {determinator} {noun}")
    return prepositional_phrase
main()