# PROBELM 4 - Jumbled Up

all_inputs_list = [] # stores sublists containing words with potential anagrams.

while True:
    user_input = input()
    if user_input == '0': break
    if len(user_input) > 1:
        sublist_of_words = user_input.split(' ')
        all_inputs_list.append(sublist_of_words)

# returns a dictionary where the key is the original word, and the value is a list of words it's an anagram with.
def group_anagrams(sublist_of_words):
    hashmap = dict()
    for word in sublist_of_words:
        word_to_list_format = list(word)
        word_to_list_format.sort()
        sorted_word = ''.join(word_to_list_format)
        if sorted_word not in hashmap:
            hashmap[sorted_word] = []
        hashmap[sorted_word].append(word)
    return hashmap

# If the length of a value is only 1, it tells us we have a unique word in our sublist which is what we want.
for sublist in all_inputs_list:
    dict_for_this_list = group_anagrams(sublist)
    unique_words_list = [] # stores unique words
    print('Results:')

    for x, y in dict_for_this_list.items(): # Iterate through map and look for value lists of len 1.
        if len(y) == 1:
            unique_words_list.append(y[0])

    unique_words_list.sort()

    for unique_word in unique_words_list: # display final results
        print(unique_word)




