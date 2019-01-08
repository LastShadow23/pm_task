import re


def dictionary():
    words = {}
    with open('news_train.txt', 'r', encoding='utf-8-sig') as file:
        for line in file:
            category = ''
            for word in re.split('[;,.,\n,\s,\t,:,-,+,(,),=,/,«,»,@,\d,!,?,",-]', line):
                if len(word) > 1 and category:
                    words[category].add(word.lower())
                elif not category:
                    category = word.lower()
                    if category not in words.keys():
                        words[category] = set()
    return words


def sort(dict):
    amount = {}
    open('output.txt', 'w', encoding='utf-8').close()
    for i in dict.keys():
        amount[i] = 0
    with open('news_test.txt', 'r', encoding='utf-8-sig') as file:
        for line in file:
            for word in re.split('[;,.,\n,\s,\t,:,-,+,(,),=,/,«,»,@,\d,!,?,",-]', line):
                if len(word) > 1:
                    for i in dict.keys():
                        if word.lower() in dict[i]:
                            amount[i] += 1
            key, value = max(amount.items(), key=lambda item: item[1])
            with open('output.txt', 'a', encoding='utf-8') as file:
                file.write(key + '\n')
            for i in amount.keys():
                amount[i] = 0


def main():
    sort(dictionary())


if __name__ == "__main__":
    main()
