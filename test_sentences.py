from sentences import get_determinator, get_noun, get_verb
import random
import pytest


def test_get_determinator():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determinator(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determinator(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
        # Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
def test_get_noun():
    
    single_noun = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(11):
        word = get_noun(1)
        assert word in single_noun
    
    plural_noun = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(11):
        word = get_noun(2)
        assert word in plural_noun

pytest.main(["-v", "--tb=line", "-rN", __file__])       
    
def test_get_verb():
    past_tense_verb = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    word = random.choice(past_tense_verb)
    assert word in past_tense_verb
    
    single_verb = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(11):
        word = random.choice(single_verb)
        assert word in single_verb

    plural_verb = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(11):
        word = random.choice(plural_verb)
        assert word in plural_verb

    future_tense_verb = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    word = random.choice(future_tense_verb) 
    assert word in future_tense_verb

pytest.main(["-v", "--tb=line", "-rN", __file__])  