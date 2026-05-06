import sqlite3;

connection_instance = None;
cursor = None;

def connect_to_sqlite():
    global connection_instance;
    if(bool(connection_instance) == False):
        connection_instance = sqlite3.connect(r"./basics/data-base/demo.db");

    return connection_instance;

def create_table():
    global cursor;
    instance = connect_to_sqlite();

    # if(instance.)

    if(bool(cursor)):
        return cursor;

    try:
        cursor = instance.cursor();
        
        cursor.execute("create table student(id int primary key, name text, age int)")
        instance.commit();
        return cursor;
    except sqlite3.Error as e:
        print('Unable to connect to DB', e);
    
    return cursor;

def insert_data(id, name, age):
    global cursor;
    cursor = create_table();
    if(bool(cursor)):
        cursor.execute(f"insert into student values({id},'suriya',{age})");
    else:
        print('Data not inserted');

def get_data():
    global cursor;
    cursor = create_table();
    if(bool(cursor)):
        cursor.execute("select * from student")
        print(cursor.fetchall())
        

insert_data(1, 'Suriya', 28)
get_data();