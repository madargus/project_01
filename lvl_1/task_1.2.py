# Задача 1.2.

# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random
import datetime

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

songs = random.sample(my_favorite_songs, 3)
total_time = sum(song[1] for song in songs)
total_time_f = float("{:.2f}".format(total_time))
print(f"Три песни звучат {total_time_f} минут")

# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
print('-' * 50)
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

three_random_song = sum(random.sample(list(my_favorite_songs_dict.values()), k=3))
ran_song = float("{:.2f}".format(three_random_song))
print(f'Три песни звучат {ran_song} минут.')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
print('-' * 50)


def generate_random_song():
    song_title = random.choice(list(my_favorite_songs_dict.keys()))
    song_long = my_favorite_songs_dict[song_title]
    return f'{song_title} - {song_long}'


for song in range(5):
    print(generate_random_song())

# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime

print('-' * 50)
s = float(ran_song) * 60
delta = datetime.timedelta(seconds=s)
dt = datetime.datetime(1, 1, 1) + delta
form_time = dt.strftime("%M минут %S секунд")
print(" Три случайные песни звучат ", form_time)
