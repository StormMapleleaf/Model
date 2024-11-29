from flask import Flask, request, render_template, send_file
import sqlite3
import pandas as pd
from io import BytesIO

app = Flask(__name__)

# 创建数据库表（如果尚未创建）
def create_table():
    conn = sqlite3.connect('usage_records.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS equipment_usage (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        class TEXT,
                        name TEXT,
                        time TEXT,
                        content TEXT)''')
    conn.commit()
    conn.close()

# 根路径，渲染 index.html 页面
@app.route('/')
def index():
    return render_template('index.html')  # 确保 index.html 文件在正确位置

# 提交登记信息
@app.route('/submit_usage', methods=['POST'])
def submit_usage():
    date = request.form['date']
    class_name = request.form['class']
    name = request.form['name']
    time = request.form['time']
    content = request.form['content']

    conn = sqlite3.connect('usage_records.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO equipment_usage (date, class, name, time, content) VALUES (?, ?, ?, ?, ?)",
                   (date, class_name, name, time, content))
    conn.commit()
    conn.close()
    return 'Success', 200

# 导出数据为 Excel
@app.route('/export_to_excel', methods=['GET'])
def export_to_excel():
    conn = sqlite3.connect('usage_records.db')
    query = "SELECT * FROM equipment_usage"
    df = pd.read_sql_query(query, conn)
    conn.close()

    # 将 DataFrame 写入 Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Usage Records')
    output.seek(0)

    return send_file(output, as_attachment=True, download_name="开心实验室使用登记.xlsx", mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
