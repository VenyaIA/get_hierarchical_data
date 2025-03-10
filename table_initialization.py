import json


def create_table(conn):
    """
    Создание таблицы для импорта данных
    """
    create_table_sql = '''
    create table organization_structure (
      id int generated by default as identity primary key,
      parent_id int,
      name text not null,
      type int not null
    )
    '''

    with conn.cursor() as cursor:
        cursor.execute(create_table_sql)
        conn.commit()


def insert_data(conn):
    """
    Импорт данных из json в таблицу SQL organization_structure
    """

    with open('data/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    insert_data_sql = '''
    insert into organization_structure
    values
    (%s, %s, %s, %s)
    '''
    data = [tuple(el.values()) for el in data]

    with conn.cursor() as cursor:
        cursor.executemany(insert_data_sql, data)
        conn.commit()
