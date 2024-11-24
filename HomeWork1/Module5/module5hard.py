import hashlib as hl
import time as t

class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = self.hash_password(password)
        self.age = int(age)

    def hash_password(self, password):
        return hl.sha256(password.encode('utf-8')).hexdigest()

    def __eq__(self, other):
        return self.nickname == other.nickname

class Video:
    def __init__(self, title, duration, adult_vode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_vode = adult_vode

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()
    def __str__(self):
        return f"Video(title{self.title}, duration = {self.duration}, adult_mode={self.adult_mode})"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = hl.sha256(password.encode('utf-8')).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {nickname} вошел в систему.")
                return True
            print("Ошибка входа: неверный логин или пароль.")
            return False

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(new_user)
            self.current_user = new_user
            print(f"Пользователь {nickname} успешно зарегистрирован и вошёл в систему.")

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
            else:
                print(f"Видео '{video.title}' уже существует.")

    def get_videos(self, search_video):
        search_video_lower = search_video.lower()
        return [video.title for video in self.videos if search_video_lower in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтоб смотреть видео.")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_vode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for second in range(video.time_now + 1, video.duration +1):
                    print(second, end=' ', flush=True)
                    t.sleep(1)
                    video.time_now = 0
                    return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_vode=True)

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
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')