#Write code to create a list of word lengths for the words in original_str using the 
#accumulation pattern and assign the answer to a variable num_words_list. (You should use the len function).

original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list = []
splitter = original_str.split()
for i in splitter:
    length = len(i)
    num_words_list.append(length)
print(num_words_list)