import DataPreprocessingModule as dp

bagOfWords = dp.bag_of_words(r'/home/nrdev/Projects/PythonProjects/Intellij/GoogleCrashCourse/inputFiles/input.txt')

frequencies = dp.calculate_frequncy(bagOfWords)

dp.create_wordCloud(frequencies)
