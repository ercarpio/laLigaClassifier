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
                        ' 1:' + str((words[5])) + \
                        ' 2:' + str((words[6])) + \
                        ' 3:' + str((words[7])) + \
                        ' 4:' + str((words[8])) + \
                        ' 5:' + str((words[9])) + \
                        ' 6:' + str((words[10])) + \
                        ' 7:' + str(teams.index(words[2])) + \
                        ' 8:' + str(teams.index(words[3])) + \
                        ' 9:' + str((words[11])) + \
                        ' 10:' + str((words[12])) + \
                        ' 11:' + str((words[13])) + \
                        ' 12:' + str((words[14])) + \
                        ' 13:' + str((words[15])) + \
                        ' 14:' + str((words[16])) + \
                        ' 15:' + str((words[17])) + \
                        ' 16:' + str((words[18])) + \
                        ' 17:' + str((words[19])) + \
                        ' 18:' + str((words[20]))
            outTrain += '\n'
            out += str(int(words[4])) + \
                      ' 1:' + str((words[5])) + \
                      ' 2:' + str((words[6])) + \
                      ' 3:' + str((words[7])) + \
                      ' 4:' + str((words[8])) + \
                      ' 5:' + str((words[9])) + \
                      ' 6:' + str((words[10])) + \
                      ' 7:' + str(teams.index(words[2])) + \
                      ' 8:' + str(teams.index(words[3])) + \
                      ' 9:' + str((words[11])) + \
                      ' 10:' + str((words[12])) + \
                      ' 11:' + str((words[13])) + \
                      ' 12:' + str((words[14])) + \
                      ' 13:' + str((words[15])) + \
                      ' 14:' + str((words[16])) + \
                      ' 15:' + str((words[17])) + \
                      ' 16:' + str((words[18])) + \
                      ' 17:' + str((words[19])) + \
                      ' 18:' + str((words[20]))
            out += '\n'
        else:
            outTest += str(int(words[4])) + \
                       ' 1:' + str((words[5])) + \
                       ' 2:' + str((words[6])) + \
                       ' 3:' + str((words[7])) + \
                       ' 4:' + str((words[8])) + \
                       ' 5:' + str((words[9])) + \
                       ' 6:' + str((words[10])) + \
                       ' 7:' + str(teams.index(words[2])) + \
                       ' 8:' + str(teams.index(words[3])) + \
                       ' 9:' + str((words[11])) + \
                       ' 10:' + str((words[12])) + \
                       ' 11:' + str((words[13])) + \
                       ' 12:' + str((words[14])) + \
                       ' 13:' + str((words[15])) + \
                       ' 14:' + str((words[16])) + \
                       ' 15:' + str((words[17])) + \
                       ' 16:' + str((words[18])) + \
                       ' 17:' + str((words[19])) + \
                       ' 18:' + str((words[20]))
            outTest += '\n'
            out += str(int(words[4])) + \
                   ' 1:' + str((words[5])) + \
                   ' 2:' + str((words[6])) + \
                   ' 3:' + str((words[7])) + \
                   ' 4:' + str((words[8])) + \
                   ' 5:' + str((words[9])) + \
                   ' 6:' + str((words[10])) + \
                   ' 7:' + str(teams.index(words[2])) + \
                   ' 8:' + str(teams.index(words[3])) + \
                   ' 9:' + str((words[11])) + \
                   ' 10:' + str((words[12])) + \
                   ' 11:' + str((words[13])) + \
                   ' 12:' + str((words[14])) + \
                   ' 13:' + str((words[15])) + \
                   ' 14:' + str((words[16])) + \
                   ' 15:' + str((words[17])) + \
                   ' 16:' + str((words[18])) + \
                   ' 17:' + str((words[19])) + \
                   ' 18:' + str((words[20]))
            out += '\n'
    with open('../../data/ProcessedData/RFInput/' + str(fileCounter) +
                      '_inFile_' + str(fileCounter + 5) + "-" + str(fileCounter + 6), 'w+') as infile:
        infile.writelines(out)
    fileCounter += 1
#print outTrain
print outTest
#
with open('../../data/ProcessedData/outTrainRF', 'w+') as infile:
    infile.writelines(outTrain)
with open('../../data/ProcessedData/outTestRF', 'w+') as infile:
    infile.writelines(outTest)
