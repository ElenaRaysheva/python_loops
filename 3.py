results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

def add_roi(data):
    for company in data:
        values = data[company]
        roi = round((values['revenue'] / values['cost'] - 1) * 100, 2)
        data[company]['ROI'] = roi

    return data

print(add_roi(results))
