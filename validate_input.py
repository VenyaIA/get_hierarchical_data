def input_validator(conn, id_employee):
    """
    Выполняет проверку, есть ли сотрудник с таким id в базе данных
    """
    with conn.cursor() as cursor:
        cursor.execute('''
        select id 
        from organization_structure 
        where id = %s and type = 3
        limit 1''', (id_employee,))

        return cursor.fetchone()
