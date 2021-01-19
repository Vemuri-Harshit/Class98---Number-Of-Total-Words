def countWords():
    file_name = input("File Location:")
    file = open(file_name)
    number_of_words = 0
    file_lines = file.readlines()
    for l in file_lines:
        word_in_line = l.split() 
        number_of_words += len(word_in_line)
    print(number_of_words)

countWords()            

