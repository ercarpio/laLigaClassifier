# coding=utf-8
from os import listdir
inFiles = listdir('../../data/ProcessedData/Matches/')
teams = ['Alavés', 'Almería', 'Athletic Club', 'Atlético de Madrid', 'Barcelona', 'Betis',
         'Celta de Vigo', 'Cádiz', 'Córdoba', 'Deportivo de La Coruña', 'Eibar', 'Elche',
         'Espanyol', 'Getafe', 'Gimnàstic de Tarragona', 'Granada', 'Hércules', 'Levante',
         'Mallorca', 'Murcia', 'Málaga', 'Numancia', 'Osasuna', 'Racing de Santander',
         'Rayo Vallecano', 'Real Madrid', 'Real Sociedad', 'Real Zaragoza',
         'Recreativo de Huelva', 'Sevilla', 'Sporting de Gijón', 'Tenerife', 'Valencia',
         'Valladolid', 'Villarreal', 'Xerez', 'Las Palmas']
#print inFiles
fileCounter = 0
outTrain = ''
outTest = ''
outTest2 = ''
for inFile in inFiles:
    out = ''
    with open('../../data/ProcessedData/Matches/' + inFile) as infile:
        txt = infile.readlines()
    for line in txt:
        while line[-1] in ['\n','\r']:
            line = line[0:len(line)-1]
        words = line.split('|')
        #print words
        if fileCounter < 9:
            outTrain += str(int(words[4])) + \
                        ' 1:' + str((words[7])) + \
                        ' 2:' + str((words[8])) + \
                        ' 3:' + str(teams.index(words[3])) + \
                        ' 4:' + str((words[13])) + \
                        ' 5:' + str((words[14])) + \
                        ' 6:' + str((words[15])) + \
                        ' 7:' + str((words[17])) + \
                        ' 8:' + str((words[18])) + \
                        ' 9:' + str((words[19])) + \
                        ' 10:' + str((words[20]))
            outTrain += '\n'
        elif fileCounter == 9:
            outTest += str(int(words[4])) + \
                       ' 1:' + str((words[7])) + \
                       ' 2:' + str((words[8])) + \
                       ' 3:' + str(teams.index(words[3])) + \
                       ' 4:' + str((words[13])) + \
                       ' 5:' + str((words[14])) + \
                       ' 6:' + str((words[15])) + \
                       ' 7:' + str((words[17])) + \
                       ' 8:' + str((words[18])) + \
                       ' 9:' + str((words[19])) + \
                       ' 10:' + str((words[20]))
            outTest += '\n'
        else:
            outTest2 += str(int(words[4])) + \
                        ' 1:' + str((words[7])) + \
                        ' 2:' + str((words[8])) + \
                        ' 3:' + str(teams.index(words[3])) + \
                        ' 4:' + str((words[13])) + \
                        ' 5:' + str((words[14])) + \
                        ' 6:' + str((words[15])) + \
                        ' 7:' + str((words[17])) + \
                        ' 8:' + str((words[18])) + \
                        ' 9:' + str((words[19])) + \
                        ' 10:' + str((words[20]))
            outTest2 += '\n'
    fileCounter += 1
#print outTrain
print outTest
#
with open('../../data/ProcessedData/SVMInput/outTrainSVM', 'w+') as infile:
    infile.writelines(outTrain)
with open('../../data/ProcessedData/SVMInput/outTestSVM', 'w+') as infile:
    infile.writelines(outTest)
with open('../../data/ProcessedData/SVMInput/outTest2SVM', 'w+') as infile:
    infile.writelines(outTest2)
