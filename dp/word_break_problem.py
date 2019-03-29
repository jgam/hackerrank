#dictionary of words and a string of characters, find if the string of characters can be broken into individual valid words from the dictionary

#dictionary: arrays, dynamic, heaps, IDeserve, learn, learning, linked, list, platform, programming, stacks, trees
#IDeservelearningplatform
#true

dictionary = ['arrays', 'dynamic', 'heaps', 'IDeserve', 'learn', 'learning', 'linked', 'list', 'platforms', 'programming', 'stacks', 'trees']
input_str = 'IDeservelearningplatform'

def word_break(input_str):
    cur_char = ''
    index = -1
    return_index = 0
    for character in input_str:
        index += 1
        cur_char += character
        if cur_char in dictionary:
            if index == len(input_str)-1:
                return True
            return_index = index+1
    if return_index != 0:
        return (word_break(input_str[return_index:]))
    else:
        return False


print(word_break(input_str))