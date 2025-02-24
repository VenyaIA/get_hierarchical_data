def get_all_employees_by_office(conn, id_employee):
    """
    Выполняет основной алгоритм нахождения всех сотрудников офиса
    по идентификатору одного из сотрудников.
    Возвращает название офиса и список его сотрудников
    """

    with (open('sql/get_office_by_employee.sql', 'r') as file1,
          open('sql/get_employees_by_office.sql', 'r') as file2):
        office_by_employee = file1.read()
        employees_by_office = file2.read()

    with conn.cursor() as cursor:
        cursor.execute(office_by_employee, (id_employee,))

        # Получаем id и название нужной организации
        id_organization, name_organization = cursor.fetchall()[0]

        cursor.execute(employees_by_office, (id_organization,))

        # Получаем лист с именами всех сотрудников полученной организации
        employees_list = [el[0] for el in cursor.fetchall()]

    return name_organization, employees_list
