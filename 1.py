ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def get_uniq_tags(tags):
    uniq_tags = []
    for user in tags:
        for t in tags[user]:
            if t not in uniq_tags:
                uniq_tags.append(t)

    return uniq_tags


print(get_uniq_tags(ids))
