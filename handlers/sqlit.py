import sqlite3
def reg_user(id,ref):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(""" CREATE TABLE IF NOT EXISTS channel_list (
            name,
            number
            ) """)
    db.commit()
    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id BIGINT,
        status_ref
        ) """)
    db.commit()
    sql.execute(f"SELECT id FROM user_time WHERE id ='{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?)", (id, ref))
        db.commit()


    sql.execute(""" CREATE TABLE IF NOT EXISTS trafik (
            chanel,
            parametr,
            person
            ) """)
    db.commit()
    sql.execute(f"SELECT chanel FROM trafik WHERE chanel = 'channel1'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?)", ('channel1','favorit_film',100))
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?)", ('channel2', 'total_fillm',100))
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?)", ('channel3', 'newfilms_onlain',100))
        db.commit()


    sql.execute(f"SELECT id FROM user_time WHERE id ='{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?)", (id, ref))
        db.commit()

def info_members():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    a = sql.execute(f'SELECT COUNT(*) FROM user_time').fetchone()[0]
    return a


def cheak_traf():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    c1 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel1'").fetchone()[0]
    c2 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel2'").fetchone()[0]
    c3 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel3'").fetchone()[0]
    list = [c1,c2,c3]
    return list


def obnovatrafika(channel1,channel2,channel3):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(f"UPDATE trafik SET parametr= '{channel1}' WHERE chanel = 'channel1'")
    sql.execute(f"UPDATE trafik SET parametr= '{channel2}' WHERE chanel = 'channel2'")
    sql.execute(f"UPDATE trafik SET parametr= '{channel3}' WHERE chanel = 'channel3'")
    db.commit()