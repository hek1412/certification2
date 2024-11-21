import os
import psycopg2

def get_dep():
    connection = psycopg2.connect(
        dbname=os.environ.get('POSTGRES_DB', 'postgres'),
        user=os.environ.get('POSTGRES_USER', 'postgres'),
        password=os.environ.get('POSTGRES_PASSWORD', 'password'),
        host='postgres',
        port=5432
    )

    cursor = connection.cursor()
    create_table_query = """
        CREATE TABLE IF NOT EXISTS dep_table (
            ID SERIAL PRIMARY KEY,
            Name VARCHAR(255),
            Age SMALLINT,
            Department VARCHAR(255)
        );
        """

    insert_data_query = """
        INSERT INTO dep_table (Name, Age, Department)
        VALUES 
            ('John', 25, 'HR'),
            ('Jane', 30, 'Clearing'),
            ('Mike', 35, 'Safety'),
            ('Emily', 40, 'Engineering');
        """

    cursor.execute(create_table_query) # Запрос на создание таблицы
    cursor.execute(insert_data_query) # Запрос на вставку данных
    connection.commit()  # Зафиксировать изменения в базе данных

    # Запрос на выборку данных из таблицы
    select_query = "SELECT * FROM dep_table;"
    cursor.execute(select_query)

    dep_info = cursor.fetchall()  # Для получения всех строк

    column_names = [desc[0] for desc in cursor.description] # Получение заголовков столбцов

    print(f"{' | '.join(column_names)}") # Вывод данных с заголовками
    for row in dep_info:
        print(f"{' | '.join(map(str, row))}")

    cursor.close()
    connection.close()

if __name__ == '__main__':
    get_dep()