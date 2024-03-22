def words_b(filename):
    """
    Find 3 letter words in the file and print them
    :param filename: name of the file
    :return: nothing
    """
    punctuation =",!?.\n"
    # open the file
    with open(filename, "r") as file:
        # go over the file line by line
        for line in file:
            # replace each punctuation mark with nothing
            for p in punctuation:
                line = line.replace(p,"")
            # get the words in the line
        words = line.split(" ")
        for word in words:
            if len(word) == 3 and word.startswitch("b"):
                print(word)
    return
