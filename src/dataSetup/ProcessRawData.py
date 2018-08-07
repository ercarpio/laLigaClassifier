# coding=utf-8
from os import listdir

inFiles = listdir('../../data/RawData/Matches/')
teams = ['Alavés', 'Almería', 'Athletic Club', 'Atlético de Madrid', 'Barcelona', 'Betis',
         'Celta de Vigo', 'Cádiz', 'Córdoba', 'Deportivo de La Coruña', 'Eibar', 'Elche',
         'Espanyol', 'Getafe', 'Gimnàstic de Tarragona', 'Granada', 'Hércules', 'Levante',
         'Mallorca', 'Murcia', 'Málaga', 'Numancia', 'Osasuna', 'Racing de Santander',
         'Rayo Vallecano', 'Real Madrid', 'Real Sociedad', 'Real Zaragoza',
         'Recreativo de Huelva', 'Sevilla', 'Sporting de Gijón', 'Tenerife', 'Valencia',
         'Valladolid', 'Villarreal', 'Xerez', 'Las Palmas']
twoWordNames = ['Athletic', 'Real', 'Rayo', 'Las']
threeWordNames = ['Celta', 'Atlético', 'Sporting', 'Racing', 'Recreativo', 'Gimnàstic']
fourWordNames = ['Deportivo']
promotedTeams = [['Cádiz', 'Celta de Vigo', 'Alavés'],
                 ['Recreativo de Huelva', 'Gimnàstic de Tarragona', 'Levante'],
                 ['Valladolid', 'Almería', 'Murcia'],
                 ['Numancia', 'Málaga', 'Sporting de Gijón'],
                 ['Xerez', 'Real Zaragoza', 'Tenerife'],
                 ['Real Sociedad', 'Hércules', 'Levante'],
                 ['Betis', 'Rayo Vallecano', 'Granada'],
                 ['Deportivo de La Coruña', 'Celta de Vigo', 'Valladolid'],
                 ['Elche', 'Villarreal', 'Almería'],
                 ['Eibar', 'Deportivo de La Coruña', 'Córdoba'],
                 ['Betis', 'Sporting de Gijón', 'Las Palmas']]
seasonId = 0
homeWins = 0
awayWins = 0
ties = 0
pts = [0] * len(teams)
formGames = 6
form = [[0 for x in range(formGames)] for y in range(len(teams))]
hForm = [[0 for x in range(formGames/2)] for y in range(len(teams))]
aForm = [[0 for x in range(formGames/2)] for y in range(len(teams))]

with open('../../data/RawData/Teams/Ratings', 'r') as infile:
    ratings = infile.readlines()

for inFile in inFiles:
    out = ''
    with open('../../data/RawData/Matches/' + inFile, 'r') as infile:
        txt = infile.readlines()
    matchDay = '0'
    seasonRatings = ratings[0 + (20 * seasonId):20 + (20 * seasonId)]
    seasonRatingsLocation = [''] * 20
    for i in range(0,20):
        seasonRatingsLocation[i] = seasonRatings[i].split('|')[1]
    for line in txt:
        words = line.split()
        if len(words) > 0:
            if words[0] != 'Data':
                if words[0] == 'Jornada':
                    matchDay = words[1]
                else:
                    homeTeam = words[1]
                    homeScoreIndex = 2
                    if words[1] in twoWordNames:
                        homeTeam += ' ' + words[2]
                        homeScoreIndex = 3
                    elif words[1] in threeWordNames:
                        homeTeam += ' ' + words[2] + ' ' + words[3]
                        homeScoreIndex = 4
                    elif words[1] in fourWordNames:
                        homeTeam += ' ' + words[2] + ' ' + words[3] + ' ' + words[4]
                        homeScoreIndex = 5
                    awayTeam = words[homeScoreIndex + 2]
                    if words[homeScoreIndex + 2] in twoWordNames:
                        awayTeam += ' ' + words[homeScoreIndex + 3]
                    elif words[homeScoreIndex + 2] in threeWordNames:
                        awayTeam += ' ' + words[homeScoreIndex + 3] + ' ' + words[homeScoreIndex + 4]
                    elif words[homeScoreIndex + 2] in fourWordNames:
                        awayTeam += ' ' + words[homeScoreIndex + 3] + ' ' + words[homeScoreIndex + 4] \
                                    + ' ' + words[homeScoreIndex + 5]
                    matchClass = 1
                    if words[homeScoreIndex] > words[homeScoreIndex + 1]:
                        matchClass = 0
                    elif words[homeScoreIndex] < words[homeScoreIndex + 1]:
                        matchClass = 2
                    out += matchDay + '|' + words[0] + '|' + homeTeam + '|' + awayTeam + '|' + str(matchClass) + '|' + \
                           str(pts[teams.index(homeTeam)]) + '|' + str(pts[teams.index(awayTeam)]) + '|' + \
                           str(sum(form[teams.index(homeTeam)])) + '|' + str(sum(form[teams.index(awayTeam)])) + '|' + \
                           str(sum(hForm[teams.index(homeTeam)])) + '|' + str(sum(aForm[teams.index(awayTeam)]))
                    if homeTeam in promotedTeams[seasonId]:
                        out += '|1'
                    else:
                        out += '|0'
                    if awayTeam in promotedTeams[seasonId]:
                        out += '|1'
                    else:
                        out += '|0'
                    hRatings = seasonRatings[seasonRatingsLocation.index(homeTeam)].split('|')
                    for i in range(2, 6):
                        out += '|' + hRatings[i].replace('\n', '')
                    aRatings = seasonRatings[seasonRatingsLocation.index(awayTeam)].split('|')
                    for i in range(2, 6):
                        out += '|' + aRatings[i].replace('\n', '')
                    out += '\n'
                    form[teams.index(homeTeam)].pop(0)
                    form[teams.index(awayTeam)].pop(0)
                    hForm[teams.index(homeTeam)].pop(0)
                    aForm[teams.index(awayTeam)].pop(0)
                    if matchClass == 0:
                        pts[teams.index(homeTeam)] += 3
                        form[teams.index(homeTeam)].append(3)
                        form[teams.index(awayTeam)].append(0)
                        hForm[teams.index(homeTeam)].append(3)
                        aForm[teams.index(awayTeam)].append(0)
                        homeWins += 1
                    elif matchClass == 1:
                        ties += 1
                        pts[teams.index(homeTeam)] += 1
                        pts[teams.index(awayTeam)] += 1
                        form[teams.index(homeTeam)].append(1)
                        form[teams.index(awayTeam)].append(1)
                        hForm[teams.index(homeTeam)].append(1)
                        aForm[teams.index(awayTeam)].append(1)
                    elif matchClass == 2:
                        awayWins += 1
                        pts[teams.index(awayTeam)] += 3
                        form[teams.index(homeTeam)].append(0)
                        form[teams.index(awayTeam)].append(3)
                        hForm[teams.index(homeTeam)].append(0)
                        aForm[teams.index(awayTeam)].append(3)
    with open('../../data/ProcessedData/Matches/' + inFile, 'w+') as infile:
        infile.writelines(out)
        print out
    pts = [0] * len(teams)
    form = [[0 for x in range(formGames)] for y in range(len(teams))]
    hForm = [[0 for x in range(formGames/2)] for y in range(len(teams))]
    aForm = [[0 for x in range(formGames/2)] for y in range(len(teams))]
    seasonId += 1
total = float(homeWins + ties + awayWins)
print homeWins, ties, awayWins, total
print '%.2f %.2f %.2f' % (homeWins / total * 100, ties / total * 100, awayWins / total * 100)
