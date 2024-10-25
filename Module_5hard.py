from time import sleep
class UrTube:
    videos = []
    users = []
    current_user = None
    def __init__(self):
        pass


    def log_in(self, nickname, password):
        if len(self.users) != 0:
            for i in self.users:
                if nickname in i.nickname:
                    if hash(password) == i.password:
                        self.current_user = i
                    else:
                        print('Неправильный пароль!')


    def register(self, nickname, password, age):
        existing_user = False
        if len(self.users) == 0:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)
        else:
            for j in range(len(self.users)):
                for i in self.users:
                    if nickname in i.nickname:
                        existing_user = True
                        break
            if not existing_user:
                self.users.append(User(nickname, password, age))
                self.log_in(nickname, password)
            else:
                print(f'Пользователь {nickname} уже существует')


    def log_out(self):
        self.current_user = None


    def add(self, *args):
        for i in args:
            self.videos.append(i)


    def get_videos(self, search):
        founded_titles = []
        for i in self.videos:
            if search.lower() in i.title.lower():
                founded_titles.append(i.title)
        return founded_titles

    def watch_video(self, video_name):
        for i in self.videos:
            if video_name in i.title:
                if self.current_user is None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                elif i.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for j in range(i.duration):
                        print(j+1, end = ' ')
                        sleep(1)
                    print('Конец видео')


class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User :

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

#print(f'Текущий юзер: {ur.current_user}')
#print(f'Количество юзеров в базе: {len(ur.users)}. А именно:')
#for i in ur.users:
#    print(i.nickname)
