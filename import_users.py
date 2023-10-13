import pandas as pd
import os
import django

# Настройка Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pr.settings")
django.setup()

# Импорт модели пользователя Django
from django.contrib.auth.models import User

# Чтение данных Excel
df = pd.read_excel('newusers.xlsx', engine='openpyxl')

# Создание пользователей
for index, row in df.iterrows():
    username = row['username']
    password = row['password']

    # Проверка на существование пользователя
    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username=username, password=password)
