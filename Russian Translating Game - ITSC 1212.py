import random

# русско-англйсский словарб - The Russian to English dictonary using begginers phrases.
russian_words = {
    "Привет": "Hello",
    "Пожалуйста": "Please",
    "Спасибо": "Thank you",
    "Извините": "Sorry",
    "Да": "Yes",
    "Нет": "No",
    "Доброе утро": "Good morning",
    "Добрый день": "Good afternoon",
    "Добрый вечер": "Good evening",
    "Спокойной ночи": "Good night",
    "До свидания": "Goodbye",
    "Как дела?": "How are you?",
    "Очень хорошо": "Very well",
    "Не очень": "Not very well",
    "Понимаю": "I understand",
    "Не понимаю": "I don't understand",
    "Где...?": "Where is...?",
    "Сколько это стоит?": "How much does it cost?",
    "Я люблю тебя": "I love you",
    "Помогите!": "Help!",
    "Что это?": "What is this?",
    "Я не знаю": "I don't know",
    "Можно?": "May I?",
    "Конечно": "Of course",
    "Извините, где...?": "Excuse me, where is...?",
    "Вода": "Water",
    "Еда": "Food",
    "Чай": "Tea",
    "Кофе": "Coffee",
    "Молоко": "Milk",
    "Хлеб": "Bread",
    "Сыр": "Cheese",
    "Мясо": "Meat",
    "Рыба": "Fish",
    "Овощи": "Vegetables",
    "Фрукты": "Fruits",
    "Суп": "Soup",
    "Завтрак": "Breakfast",
    "Обед": "Lunch",
    "Ужин": "Dinner",
    "Комната": "Room",
    "Дом": "House",
    "Квартира": "Apartment",
    "Гостиница": "Hotel",
    "Улица": "Street",
    "Магазин": "Store",
    "Рынок": "Market",
    "Аптека": "Pharmacy",
    "Больница": "Hospital",
    "Поликлиника": "Clinic",
    "Машина": "Car",
    "Автобус": "Bus",
    "Поезд": "Train",
    "Самолет": "Airplane",
    "Транспорт": "Transport",
    "Вокзал": "Train station",
    "Аэропорт": "Airport",
    "Билет": "Ticket",
    "Паспорт": "Passport",
    "Полиция": "Police",
    "Скорая помощь": "Ambulance",
    "Апельсин": "Orange",
    "Яблоко": "Apple",
    "Банан": "Banana",
    "Виноград": "Grapes",
    "Клубника": "Strawberry",
    "Малина": "Raspberry",
    "Арбуз": "Watermelon",
    "Кот": "Cat",
    "Собака": "Dog",
    "Птица": "Bird",
    "Рыба": "Fish",
    "Лошадь": "Horse",
    "Курица": "Chicken",
    "Корова": "Cow",
    "Свинья": "Pig",
    "Кролик": "Rabbit",
    "Овца": "Sheep",
    "Лев": "Lion",
    "Тигр": "Tiger",
    "Слон": "Elephant",
    "Медведь": "Bear",
    "Волк": "Wolf",
    "Лиса": "Fox",
    "Зебра": "Zebra",
    "Обезьяна": "Monkey",
    "Змея": "Snake",
    "Черепаха": "Turtle",
    "Книга": "Book",
    "Газета": "Newspaper",
    "Журнал": "Magazine",
    "Тетрадь": "Notebook",
    "Ручка": "Pen",
    "Карандаш": "Pencil",
    "Резинка": "Eraser",
    "Линейка": "Ruler",
    "Словарь": "Dictionary",
    "Учитель": "Teacher",
    "Ученик": "Student",
    "Школа": "School",
    "Университет": "University",
    "Класс": "Class",
    "Урок": "Lesson",
    "Задание": "Homework",
    "Экзамен": "Exam",
    "Праздник": "Holiday",
    "Рождество": "Christmas",
    "Новый год": "New Year",
    "День рождения": "Birthday",
    "Каникулы": "Vacation",
    "Лето": "Summer",
    "Зима": "Winter",
    "Осень": "Autumn",
    "Весна": "Spring",
    "Понедельник": "Monday",
    "Вторник": "Tuesday",
    "Среда": "Wednesday",
    "Четверг": "Thursday",
    "Пятница": "Friday",
    "Суббота": "Saturday",
    "Воскресенье": "Sunday",
    "Вчера": "Yesterday",
    "Сегодня": "Today",
    "Завтра": "Tomorrow",
    "Утро": "Morning",
    "День": "Day",
    "Вечер": "Evening",
    "Ночь": "Night",
    "Время": "Time",
    "Час": "Hour",
    "Минута": "Minute",
    "Секунда": "Second",
    "Свет": "Light",
    "Темно": "Dark",
    "Солнце": "Sun",
    "Луна": "Moon",
    "Звезда": "Star",
    "Небо": "Sky",
    "Земля": "Earth",
    "Море": "Sea",
    "Океан": "Ocean",
    "Река": "River",
    "Озеро": "Lake",
    "Гора": "Mountain",
    "Лес": "Forest",
    "Дерево": "Tree",
    "Цветок": "Flower",
    "Трава": "Grass",
    "Куст": "Bush",
    "Лист": "Leaf",
    "Корень": "Root",
    "Погода": "Weather",
    "Дождь": "Rain",
    "Снег": "Snow",
    "Ветер": "Wind",
    "Туман": "Fog",
    "Облако": "Cloud",
    "Град": "Hail",
    "Шторм": "Storm",
    "Деньги": "Money",
    "Рубль": "Ruble",
    "Кошелек": "Wallet",
    "Банк": "Bank",
    "Карта": "Card",
    "Телефон": "Phone",
    "Компьютер": "Computer",
    "Интернет": "Internet",
    "Электричество": "Electricity",
    "Вода": "Water",
    "Город": "City",
    "Деревня": "Village",
    "Мост": "Bridge",
    "Парк": "Park",
    "Площадь": "Square",
    "Почта": "Post office",
    "Библиотека": "Library",
    "Музей": "Museum",
    "Ресторан": "Restaurant",
    "Кафе": "Cafe",
    "Театр": "Theater",
    "Кинотеатр": "Cinema",
    "Стадион": "Stadium",
    "Парк аттракционов": "Amusement park",
    "Зоопарк": "Zoo",
    "Церковь": "Church",
    "Собор": "Cathedral",
    "Мечеть": "Mosque",
    "Синагога": "Synagogue",
    "Больница": "Hospital",
    "Аптека": "Pharmacy",
    "Поликлиника": "Clinic"
}

# calls a random word from the translation dictionary
def get_random_word():
    return random.choice(list(russian_words.keys()))

# takes input by converting to lowercase and removing apostrophes
def preprocess(text):
    return text.lower().replace("'", "")

# function to play a round of the game and also defines correct and inccorect answers
def play_game():
    points = 0
    incorrect_answers = 0
    level = 1

    while incorrect_answers < 3:
        print(f"\nLevel {level}")
        word = get_random_word()
        correct_translation = preprocess(russian_words[word])
        
        attempts = 2
        while attempts > 0:
            user_translation = preprocess(input(f"Translate '{word}' into Russian (Attempts left: {attempts}): ").strip())
            
            if user_translation == correct_translation:
                points += 10
                print("Правильный! Your answer is correct.")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print("Heправильный. Try again.")
                else:
                    incorrect_answers += 1
                    print(f"Неправильный. The correct translation was '{correct_translation}'.")
        
        # level up if the user answers correctly 3 times in a row
        if points // 30 >= level:
            level += 1
            print(f"Отличная работа! You've reached level {level}.")
        
        # ends the game if the user has had 3 incorrect answers
        if incorrect_answers >= 3:
            break
    
    print(f"\nGame Over! Your final score is {points} points.")

# main function to start the game
if __name__ == "__main__":
    print("Добро пожаловать в игру-переводчик на русский язык! Вам будет дано слово на русском языке, и вы должны перевести его на английский. У вас есть три попытки до окончания игры, поэтому постарайтесь набрать как можно больше очков!")
    print("Welcome to the Russian Translating Game! You will be given a word in Russian and must translate it to English. You have three tries before the game ends so try to get as many points as you can!")
    play_game()

