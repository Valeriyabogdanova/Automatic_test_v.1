from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pytest

db_connection_string = "postgresql://postgres:postgres@localhost:5432/testQA"
db = create_engine(db_connection_string)



def test_select():
    connection = db.connect()
    result = connection.execute(text('SELECT * FROM users'))
    row1 = result.mappings().first()
    assert row1["user_id"] == 42568

    connection.close()

    # добавить пользователя
def test_insert():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("INSERT into users (\"user_id\" , \"user_email\") VALUES(:new_id, :new_email)")
    connection.execute(sql,{"new_id": 777777, "new_email": "test_test@ya.ru"})
    result = connection.execute(text("SELECT * FROM users"))
    rows = result.mappings().all()
    row1 = rows[-1]
    assert row1["user_id"] == 777777

    transaction.commit()
    connection.close()

    # обновить пользователя

def test_update():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("UPDATE users SET user_email = :descr WHERE user_id = :user_id")
    connection.execute(sql, {"descr": 'NNN@34.ru', "user_id": 42568})
    result = connection.execute(text("SELECT * FROM users WHERE user_id = 42568"))
    rows = result.mappings().first()
    assert rows["user_email"] == "NNN@34.ru"
    transaction.commit()
    connection.close()

    # удалить пользователя
def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM users WHERE user_id= :user_id")
    connection.execute(sql, {"user_id": 777777})
    result = connection.execute(text("SELECT * FROM users WHERE user_id = 777777"))
    rows = result.mappings().first()
    assert rows is None


    transaction.commit()
    connection.close()