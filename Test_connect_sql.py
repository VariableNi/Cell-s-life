import pymysql
from config import host, name, password, db_name
from tkinter import CENTER
import customtkinter as CTk

main_window = CTk.CTk()
main_window.geometry("700x700")
CTk.set_appearance_mode("dark")

wiew_db = CTk.CTkLabel(master=main_window, text="")
colums_from_db = []
colums_view = "--------------" * 4 + "\n"

try:
    connection = pymysql.connect(
        host = host,
        user = name,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    print("Connect")

    try:
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `data_user` (id_user, name, email, password) VALUES ('1', 'Anna', 'anna@gmail.com',  'qwerty');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `data_user`"
            cursor.execute(select_all_rows)
            desc = cursor.description

            rows = cursor.fetchone()
            for row in rows:
                colums_from_db.append(row)

            colums_view = "\n" + "------------------" * len(colums_from_db) + "\n" + "|" + "  " * len(colums_from_db)

            for i in range(0, len(colums_from_db)):

                if i == len(colums_from_db) - 1:
                    colums_view = colums_view + "  " * len(colums_from_db) + colums_from_db[i] + "  " * len(colums_from_db) + "|"

                elif i == 0:
                    colums_view = "  " * len(colums_from_db) + colums_view + colums_from_db[i] + "  " * len(colums_from_db) + "|"
                
                else:
                    colums_view = colums_view + "  " * len(colums_from_db) +  colums_from_db[i] + "  " * len(colums_from_db) + " | "
                
            colums_view = colums_view + "\n" + "------------------" * len(colums_from_db) + "\n"
                    
            wiew_db.configure(text=colums_view)
            wiew_db.place(relx=0.5, rely=0.5, anchor=CENTER)
             
    finally:
        connection.close()

except Exception as ex:
    print(ex)

main_window.mainloop()