def reverse_words(s):
    h=s.split(" ")
    return h
sentence=input()
result=reverse_words(sentence)


join=" ".join(result[::-1])
print(join)

# def reverse_words(sentence):
    # return " ".join(sentence.split()[::-1])
# at first split kore then ulataya dey then sob join kore space diya