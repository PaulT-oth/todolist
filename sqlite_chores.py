import sqlite3

connection = sqlite3.connect('chores.db')

def save_chore(chore):
    cursor = connection.cursor()
    save_chore = (chore['desk'], chore['person'], int(chore['status']))
    ex = cursor.execute('INSERT INTO chores("desk", "person", "status") VALUES (?,?,?)', save_chore)
    lastrowid = cursor.lastrowid
    connection.commit()
    return str(lastrowid)

def get_chores():
    cursor = connection.cursor()
    cursor.execute('SELECT _id, desk, person, status FROM chores')
    chores = [{'_id':str(i), 'desk':d, 'person':p, 'status':s} for (i,d,p,s) in cursor.fetchall()]
    for chore in chores:
        chore['status'] = str(chore['status'])
    return chores

def delete_chore(_id):
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM chores where _id = """+(_id))
    connection.commit()
