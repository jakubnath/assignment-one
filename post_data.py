post_data = [
    {
        "userId":  "Alex Gates",
        "id": 1,
        "title": "sunt aut facere repellat provident",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    },
    {
        "userId":  "Alex Gates",
        "id": 2,
        "title": "qui est esse ",
        "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    },
    {
        "userId":  "Alex Gates",
        "id": 3,
        "title": "ea molestias quasi exercitationem ",
        "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
    },
    {
        "userId":  "Alex Gates",
        "id": 4,
        "title": "eum et est occaecati ",
        "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
    },
    {
        "userId":  "Alex Gates",
        "id": 5,
        "title": " nesciunt quas odio",
        "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
    },
    {
        "userId":  "Alex Gates",
        "id": 6,
        "title": "dolorem eum magni eos aperiam quia ",
        "body": "ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae"
    }, ]

# Your Code Start from here
"""
title = (post_data[5].get('title'))
slug = title.strip()

while '  ' in slug:
    slug = slug.replace('  ', ' ')
slug = slug.lower().replace(' ','-')
data = post_data[5]


data['slug'] = slug
print(data)

"""
post_data = post_data[1]

title = (post_data.get('title'))

def Convert(string):
    li = list(string.split(" "))
    return li

str_title = title
list_title = (Convert(str_title))
list_type = (list_title[:3])


list_to_string = ' '.join(list_type)


slug = list_to_string.strip()

while '  ' in slug:
    slug = slug.replace('  ', ' ')
slug = slug.lower().replace(' ','-')
post_data['slug'] = slug
print(post_data)














# Your code ends here

# print(post_data[4])
