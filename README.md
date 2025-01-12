# backend-lab-1

(Демчик Дмитро ІМ-21)

Запуск: source env/bin/activate && pip install -r requirements.txt && python run.py

З docker: docker build -t app . && docker run -it --rm --network=host app

З docker-compose: docker-compose up --build

Посилання на render: https://backend-lab-2-1bbz.onrender.com

Посилання на флоу: https://www.postman.com/ddemchyk/workspace/backend-labs/flow/6784130765332d003d5aea7d


Нотатка: render.com не дозволяє параметри в тілі get запиту, 
тому отримання колекції та фільтрування записів краще тестувати локально