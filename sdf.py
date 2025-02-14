import mysql.connector
from datetime import datetime, timedelta

# Задаем параметры подключения
host = "127.0.0.1"
user = ""
password = "YES"
database = "ecotaxidb"

# Задаем даты
from_date = datetime.strptime("2025-01-01", "%Y-%m-%d")
to_date = from_date + timedelta(days=1)

# Устанавливаем соединение с базой данных
conn = mysql.connector.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=database
)

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Формируем SQL-запрос
query = f"""
    SELECT
        drivers.name,
        COUNT(charges.id) AS charge_count
    FROM charges
    LEFT JOIN drivers ON charges.driverId = drivers.id
    WHERE charges.carId = %s
    AND charges.date BETWEEN '{from_date.strftime("%Y-%m-%d")}' AND '{to_date.strftime("%Y-%m-%d")}'
    GROUP BY drivers.name
    ORDER BY charge_count DESC;
"""

# Выполняем запрос с carId
car_id = 1  # Замените на нужное значение
cursor.execute(query, (car_id,))

# Получаем результаты
results = cursor.fetchall()
for row in results:
    print(f"Driver: {row[0]}, Charge Count: {row[1]}")

# Закрываем соединение
cursor.close()
conn.close()
