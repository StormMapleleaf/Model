from flask import Flask, render_template, jsonify, request
import sqlite3
import random

app = Flask(__name__, template_folder='templates')

# 数据库初始化
def initialize_database():
    conn = sqlite3.connect('lottery.db')
    cursor = conn.cursor()
    
    # 创建学校表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS schools (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')

    # 创建学生表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gender TEXT NOT NULL,
            student_number TEXT NOT NULL UNIQUE,
            major TEXT NOT NULL,
            school_id INTEGER,
            FOREIGN KEY (school_id) REFERENCES schools (id)
        )
    ''')

    # 清空学生表，确保没有重复数据
    cursor.execute('DELETE FROM students')
    
    # 初始化学校数据
    schools = ['武汉大学', '华中科技大学', '江汉大学']
    cursor.executemany('INSERT OR IGNORE INTO schools (name) VALUES (?)', [(name,) for name in schools])

    # 初始化学生数据（请确保包含每个学校的足够学生）
    students_data = [
        ('张三', '男', '000001', '计算机科学', '武汉大学'),
        ('李四', '男', '000002', '电子工程', '武汉大学'),
        ('王五', '女', '000003', '机械工程', '武汉大学'),
        ('赵六', '男', '000004', '土木工程', '华中科技大学'),
        ('钱七', '女', '000005', '生物科学', '华中科技大学'),
        ('孙八', '男', '000006', '化学工程', '江汉大学'),
        ('周九', '女', '000007', '法学', '江汉大学'),
        ('吴十', '男', '000008', '数学', '武汉大学'),
        ('郑十一', '男', '000009', '物理', '华中科技大学'),
        ('冯十二', '女', '000010', '心理学', '江汉大学'),
        # 可以继续添加更多学生...
    ]

    # 将学生数据插入数据库
    for student in students_data:
        cursor.execute('''
            INSERT INTO students (name, gender, student_number, major, school_id)
            VALUES (?, ?, ?, ?, (SELECT id FROM schools WHERE name = ?))
        ''', (student[0], student[1], student[2], student[3], student[4]))

    conn.commit()
    conn.close()



initialize_database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw')
def draw_lottery():
    conn = sqlite3.connect('lottery.db')
    cursor = conn.cursor()
    results = {}

    for school in ['武汉大学', '华中科技大学', '江汉大学']:
        results[school] = {'男生': [], '女生': []}

        cursor.execute('''
            SELECT * FROM students WHERE school_id = (SELECT id FROM schools WHERE name = ?)
            AND gender = '男'
        ''', (school,))
        boys = cursor.fetchall()

        cursor.execute('''
            SELECT * FROM students WHERE school_id = (SELECT id FROM schools WHERE name = ?)
            AND gender = '女'
        ''', (school,))
        girls = cursor.fetchall()

        # 随机抽取
        selected_boys = random.sample(boys, min(12, len(boys)))
        selected_girls = random.sample(girls, min(6, len(girls)))

        results[school]['男生'] = selected_boys
        results[school]['女生'] = selected_girls

    conn.close()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
