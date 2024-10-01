#!/usr/bin/env python3

def return_evens(num_list):
    return [num_list[i] for i in range(len(num_list)) if num_list[i] % 2 == 0]
    pass

def make_exclamation(sentence_list):
    return [sentence_list[i] + "!" for i in range(len(sentence_list))]
    pass