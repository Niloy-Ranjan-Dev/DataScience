import wordcloud
from matplotlib import pyplot as plt


def filehandling(fileName):
    fileRead = open(fileName, 'r')  # opening file to read
    fileContent = fileRead.read()  # retriving file contents
    fileRead.close()
    return fileContent


def bag_of_words(fileName):
    print(fileName)
    txt = filehandling(fileName)  # Data stored

    punctuations = ''''!()-[]{};:''\,<>./?@#$%^&*_~'''  # Punctuations
    uninteresting_words = ['the', 'a', 'to', 'if', 'is', 'it', 'of', 'and', 'or', 'an', 'as', 'i', 'me', 'my', 'we','our', 'ours', 'you', 'your', 'yours', 'he', 'she', 'him', 'his', 'her', 'hers', 'its' , 'they', 'them', 'their', 'what', 'which', 'who', 'whom', 'then', 'than', 'now', 'this', 'these', 'those', 'still', 'till', 'yet', 'until', 'about', 'may', 'us', 'that', 'be','shall', 'would', 'am', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'but', 'in', 'on', 'for', 'so', 'thou', 'thy', 'vs', 'd', 's', 'th', 'i', 'at', 'by', 'with', 'from', 'here', 'when', 'where', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'some', 'such', 'no', 'nor', 'not', 'too', 'very', 'can', 'will', 'just']  # We will delete these words from our file content

    txt_process = txt
    txt_process = txt_process.lower()

    # filtering out all kind of punctuation symblos
    for p in punctuations:
        txt_process = txt_process.replace(p, ' ')

    # filtering out all kind of numbers
    for i in range(0, 9):
        txt_process = txt_process.replace(str(i), ' ')

    # spiting the string into words
    txt_process = txt_process.split()

    # filtering out all unwanted words from our collected words and create a bag of words
    # length = len(txt_process)
    # for index in range(0, length):
    #     if txt_process[index] in uninteresting_words:
    #         print(txt_process[index])
    #         txt_process[index] = ''

    # filtering out all unwanted words from our collected words and create a bag of words
    for word in uninteresting_words:
        count = txt_process.count(word)
        if count != 0:
            # print(word, count)
            for i in range(0, count):
                txt_process.remove(word)

    bag_of_words = txt_process.copy()
    return bag_of_words


def calculate_frequncy(bag_of_words):
    txt_process = bag_of_words.copy()
    txt_process_temp = txt_process.copy()

    word_dictionary = dict()
    count = 0
    length = len(txt_process_temp)
    #print(txt_process_temp)
    # print(txt_process_temp[count], count, length)

    # Calculating frquencies for each of the words in bag of words
    while length > 0:
        value = txt_process[count]
        if not value in txt_process_temp:
            count += 1
            continue
        frequency_count = txt_process_temp.count(value)
        word_dictionary[value] = frequency_count

        for i in range(0, frequency_count):
            txt_process_temp.remove(value)

        count += 1
        length = len(txt_process_temp)
        # print('count: ', count, 'Length: ', length)

    word_frequency = word_dictionary  # storing frequencies for each words
    return word_frequency


def create_wordCloud(word_frequency):
    word_frequency_temp = word_frequency
    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_frequency_temp)
    myimage = cloud.to_array()
    plt.imshow(myimage, interpolation='nearest')
    plt.axis('off')
    plt.show()
