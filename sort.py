import re

science = set()
style = set()
culture = set()
life = set()
economics = set()
business = set()
travel = set()
forces = set()
media = set()
sport = set()

with open('news_train.txt', 'r', encoding='utf-8-sig') as file:
    for line in file:
        words = re.split('[;,.,\n,\s,\t,:,-,+,(,),=,/,«,»,@,\d,!,?,",-]', line)
        if words[0] == 'science':
            for i in range(1, len(words)):
                if len(words[i]) > 1:
                    science.add(words[i].lower())
        elif words[0] == 'style':
            for i in range(1, len(words)):
                if len(words[i]) > 1:
                    style.add(words[i].lower())
        elif words[0] == 'culture':
            for i in range(1, len(words)):
                if len(words[i]) > 1:
                    culture.add(words[i].lower())
        elif words[0] == 'life':
            for i in range(1, len(words)):
                if len(words[i]) > 1:
                    life.add(words[i].lower())
        elif words[0] == 'economics':
            for i in range(1, len(words)):
                if len(words[i]) > 1:
                    economics.add(words[i].lower())
        elif words[0] == 'business':
            for i in range(1, len(words)):
                if len(words[i]) > 1:
                    business.add(words[i].lower())
        elif words[0] == 'travel':
            for i in range(1, len(words)):
                if len(words[i]) > 1:
                    travel.add(words[i].lower())
        elif words[0] == 'forces':
            for i in range(1, len(words)):
                if len(words[i]) > 1:
                    forces.add(words[i].lower())
        elif words[0] == 'media':
            for i in range(1, len(words)):
                if len(words[i]) > 1:
                    media.add(words[i].lower())
        elif words[0] == 'sport':
            for i in range(1, len(words)):
                if len(words[i]) > 1:
                    sport.add(words[i].lower())

category = ['' for i in range(10)]
category[0] = 'science'
category[1] = 'style'
category[2] = 'culture'
category[3] = 'life'
category[4] = 'economics'
category[5] = 'business'
category[6] = 'travel'
category[7] = 'forces'
category[8] = 'media'
category[9] = 'sport'

open('output.txt', 'w', encoding='utf-8').close()
with open('news_test.txt', 'r', encoding='utf-8-sig') as file:
    for line in file:
        count = [0 for i in range(10)]
        words = re.split('[;,.,\n,\s,\t,:,-,+,(,),=,/,«,»,@,\d,!,?,",-]', line)
        for word in words:
            if len(word) > 1:
                if word.lower() in science:
                    count[0] += 1
                if word.lower() in style:
                    count[1] += 1
                if word.lower() in culture:
                    count[2] += 1
                if word.lower() in life:
                    count[3] += 1
                if word.lower() in economics:
                    count[4] += 1
                if word.lower() in business:
                    count[5] += 1
                if word.lower() in travel:
                    count[6] += 1
                if word.lower() in forces:
                    count[7] += 1
                if word.lower() in media:
                    count[8] += 1
                if word.lower() in sport:
                    count[9] += 1
        MAX = max(*count)
        for i in range(10):
            if count[i] == MAX:
                index = i
                break
        with open('output.txt', 'a', encoding='utf-8') as file:
            file.write(category[index] + '\n')
