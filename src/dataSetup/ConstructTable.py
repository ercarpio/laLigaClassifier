# coding=utf-8

teams = ['Alavés', 'Almería', 'Athletic Club', 'Atlético de Madrid', 'Barcelona', 'Betis',
         'Celta de Vigo', 'Cádiz', 'Córdoba', 'Deportivo de La Coruña', 'Eibar', 'Elche',
         'Espanyol', 'Getafe', 'Gimnàstic de Tarragona', 'Granada', 'Hércules', 'Levante',
         'Mallorca', 'Murcia', 'Málaga', 'Numancia', 'Osasuna', 'Racing de Santander',
         'Rayo Vallecano', 'Real Madrid', 'Real Sociedad', 'Real Zaragoza',
         'Recreativo de Huelva', 'Sevilla', 'Sporting de Gijón', 'Tenerife', 'Valencia',
         'Valladolid', 'Villarreal', 'Xerez', 'Las Palmas']
with open('../../data/ProcessedData/SVMInput/outTest') as infile:
    test = infile.readlines()
with open('../../data/Predictions/out.predict') as infile:
    out = infile.readlines()
counter = 0
correct = 0.0
pts = [0] * len(teams)
for line in test:
    lout = out[counter]
    counter += 1
    words = line.split()
    lindex = 7
    vindex = 44
    for i in range(7, 44):
        if int(words[i][len(str(i)) + 1:]) == 1:
            lindex = i
    for i in range(44, 80):
        if int(words[i][3:]) == 1:
            vindex = i
    if int(lout) == 0:
        pts[lindex-7] += 3
    elif int(lout) == 1:
        pts[lindex-7] += 1
        pts[vindex-44] += 1
    elif int(lout) == 2:
        pts[vindex-44] += 3
    if int(words[0]) == int(lout):
        correct += 1
        #print words, lout
table = []
for i in range(0, len(teams)):
    table.append([str(pts[i]), teams[i]])
table.sort(None, None, True)
posCounter = 1
for i in table:
    if int(i[0]) != 0:
        print u'{:<2} {:<23} {:<3}'.format(str(posCounter), str(i[1]).decode('utf8'), i[0])
    else:
        print u'{:<2} {:<23}'.format("-", str(i[1]).decode('utf8'))
    posCounter += 1
print correct, counter, correct/counter
