import multiprocessing
from clickhouse_driver import Client

# Функция для выполнения запросов
def execute_query(query):
    client = Client(host='g2.plzvpn.ru',
                    user='default',
                    password='1',
                    port='9000',
                    database='test',
                    settings={'use_numpy': True}
    )

    result = client.execute(query)
    for row in result:
        print(row)

# Запросы, которые выполняются параллельно
if __name__ == '__main__':
    queries = [
        'SELECT * FROM Operatory LIMIT 4',
        'SELECT * FROM Potrebiteli LIMIT 2',
    ]

    # пул процессов, раынй кол-ву запросов
    pool = multiprocessing.Pool(processes=len(queries))

    # запуск параллельных запросов
    pool.map(execute_query, queries)

    # окончание пула
    pool.close()
    pool.join()
