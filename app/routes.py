from flask import render_template, request, redirect, url_for
from app import app


# Список для хранения данных о пользователях
user_data_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Добавление данных в список
        user_data_list.append({
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        })

        # Перенаправление на главную страницу
        return redirect(url_for('index'))

    return render_template('form.html', user_data_list=user_data_list)
