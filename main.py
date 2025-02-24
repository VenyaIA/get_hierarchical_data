import psycopg2

from table_initialization import create_table, insert_data
from employee_operations import get_all_employees_by_office
from validate_input import input_validator

if __name__ == '__main__':
    with psycopg2.connect(
        dbname='db_organizations',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    ) as conn:

        # Создание таблицы и заполнение её данными из json
        # create_table(conn)
        # insert_data(conn)

        print("Введите идентификатор сотрудника:")
        id_employee = None

        # Проверка входных данных вводимых пользователем, на то что
        # это число и что такой идентификатор сотрудника присутствует в таблице organization_structure
        while True:
            try:
                id_employee = int(input())
            except ValueError:
                print("Требуется идентификатор сотрудника в виде числа:")
                continue
            if input_validator(conn, id_employee):
                break
            else:
                print("Сотрудника с таким идентификатором не существует, попробуйте ещё раз:")

        # Получаем город офиса и список имён всех сотрудников
        name_organization, employees_list = get_all_employees_by_office(conn, id_employee)

        # выводим город офиса и имена всех сотрудников через запятую,
        print(f'{name_organization}: ', end='')
        need_comma = False
        for emp in employees_list:
            if not need_comma:
                need_comma = True
                print(f'{emp}', end='')
            else:
                print(f', {emp}', end='')
        print('.')
