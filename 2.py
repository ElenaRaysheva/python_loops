queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

def get_stat(queries):
    info = {}
    total = 0

    for query in queries:
        query_length = len(query.split())

        if query_length in info:
            info[query_length] += 1
        else:
            info[query_length] = 1
        total += 1

    for stat in info:
        percentage = round(info[stat] / total * 100, 2)
        print('Поисковых запросов, содержащих',stat,' слов(а): ',percentage,'%')

get_stat(queries)
