from lxml import html
import requests

seasonLink = ['http://sofifa.com/teams/?type=club&na%5B0%5D=45&lg%5B0%5D=53&v=07&e=154818',
              'http://sofifa.com/teams/?type=club&na%5B0%5D=45&lg%5B0%5D=53&v=08&e=155183',
              'http://sofifa.com/teams/?type=club&na%5B0%5D=45&lg%5B0%5D=53&v=09&e=155549',
              'http://sofifa.com/teams/?type=club&na%5B0%5D=45&lg%5B0%5D=53&v=10&e=155914',
              'http://sofifa.com/teams/?type=club&na%5B0%5D=45&lg%5B0%5D=53&v=11&e=156279',
              'http://sofifa.com/teams/?type=club&na%5B0%5D=45&lg%5B0%5D=53&v=12&e=156644',
              'http://sofifa.com/teams/?type=club&na%5B0%5D=45&lg%5B0%5D=53&v=13&e=157011',
              'http://sofifa.com/teams/?type=club&na%5B0%5D=45&lg%5B0%5D=53&v=14&e=157396',
              'http://sofifa.com/teams/?type=club&na%5B0%5D=45&lg%5B0%5D=53&v=15&e=157759',
              'http://sofifa.com/teams/?type=club&na%5B0%5D=45&lg%5B0%5D=53&v=16&e=158127']

results = ''
for k in range(0, len(seasonLink)):
    page = requests.get(seasonLink[k])
    tree = html.fromstring(page.content)
    for i in range(1, 21):
        if (k + 6) < 10:
            results += '0'
        results += str(k+6) + '-'
        if (k + 7) < 10:
            results += '0'
        results += str(k+7) + '|'
        results += tree.xpath('//*[@id="content"]/div/article/div[3]/table/tbody/tr[' + str(i) + ']/td[2]/a/text()')[0] + '|'
        for j in range(3, 7):
            results += tree.xpath('//*[@id="content"]/div/article/div[3]/table/tbody/tr[' + str(i) + ']/td[' + str(j) + ']/span/text()')[0] + '|'
        results += '\n'
print results

# with open('../../data/RawData/Teams/Ratings', 'w+') as infile:
#     infile.writelines(str(results))

page = requests.get('http://www.fifaindex.com/players/fifa06_2/')
tree = html.fromstring(page.content)

