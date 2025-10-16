import tkinter as tk
import sqlite3 

root = tk.Tk()
root.title('Integration')
root.geometry("300x350")  

# 學生 ID
label_id = tk.Label(root, text='Student ID')
label_id.pack(pady=(10, 5))
entry_id = tk.Entry(root, width=25)
entry_id.pack()

# 學生名字
label_name = tk.Label(root, text='Student Name')
label_name.pack(pady=(10, 5))
entry_name = tk.Entry(root, width=25)
entry_name.pack()

def print_student():
    student_id = entry_id.get()
    student_name = entry_name.get()

    print('Student ID:{}'.format(student_id))
    print('Student Name:{}'.format(student_name))
    print('_'*30)

button_print = tk.Button(root, text='Print', command=print_student)
button_print.pack(pady=15)

# 建立 DB 連線
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

def create_student():
    student_id = entry_id.get()
    student_name = entry_name.get().lower()
    cursor.execute(
        'INSERT INTO db_student (db_student_id, db_student_name) VALUES (?, ?)',
        (student_id, student_name)
    )
    conn.commit()
    print('student id {}'.format(student_id))
    print('student Name {}'.format(student_name))
    print('_'*30)

def overview_student():
    cursor.execute('SELECT * FROM db_student')
    records = cursor.fetchall()
    print("=== Overview Student ===")
    for r in records:
        print(r)
    print("="*30)

# 按鈕
button_create = tk.Button(root, text='Create', command=create_student)
button_create.pack(pady=10)

button_overview = tk.Button(root, text='Overview', command=overview_student)
button_overview.pack(pady=25)

root.mainloop()


