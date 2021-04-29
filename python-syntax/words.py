def print_upper_words(words, must_start_with):
    """takes word in words and prints word capitalized
    
    For example: 
        print_upper_words(['hello', 'goodbye']) 
        
    should print:

    HELLO
    GOODBYE
    """
    # utilizing python's built in function capitalize()

    for word in words:
        if word[0] in must_start_with:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "yellow"], must_start_with = {'h', 'y'})