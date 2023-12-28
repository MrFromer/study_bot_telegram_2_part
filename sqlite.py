import sqlite3 as sq

async def db_start():
    global db, cur #db - экземпляр (модель) базы данных \\\ cur - чтобы выполнять операции с базой данных

    db = sq.connect('new.db')
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, photo TEXT, age TEXT, desc TEXT, name TEXT)") #тут мы создали саму таблицу и указали для неё поля с типами данных
    #user_id будет уникальным, в photo мы храним индефикатор фото
    db.commit() #сохраняем

async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone() #если пользователь существует, то мы берём копируем его через fetchone. И где поле user_id означает ключ, который в свою очередь через format мы обозначаем, как сам id пользователя, остальные поля пустые
    if not user: #если пользователя ещё не существует 
        cur.execute("INSERT INTO profile VALUES(?, ?, ?, ?, ?)", (user_id, '', '', '', '')) #если пользователь не существует, то мы его создаём и оставляем кроме user_id во всех полях пустые значения
        db.commit() #сохраняем
    
async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE profile SET photo = '{}', age = '{}', desc = '{}', name = '{}' WHERE user_id == '{}'".format(
            data['photo'], data['age'], data['desc'], data['name'], user_id)) #сохраняем изменения в профиле через список data и язык SQL + format
        db.commit()