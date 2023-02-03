stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

def get_top_channel(data):
    sorted_data = sorted(data.items(), key=lambda x:x[1], reverse=True)

    if len(sorted_data) > 0:
        print('Максимальный объем продаж на рекламном канале: ',sorted_data[0][0])

get_top_channel(stats)
