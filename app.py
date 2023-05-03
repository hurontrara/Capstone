from flask import Flask, request, jsonify
from crawling_utils import add_check
from crawling import main
from general_utils import dict_to_variables
from flask_mysqldb import MySQL
import json
import os


app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ.get('CAPSTONE_HOST')
app.config['MYSQL_USER'] = os.environ.get('CAPSTONE_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('CAPSTONE_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('CAPSTONE_DB')
app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)


@app.route('/test', methods=["POST"])
def test():
    print("TEST")

    return "TEST SUCCESSFUL" 


@app.route('/', methods=["POST"]) 
def process():
    param = request.get_json()
    studentNum = param['studentNum']
    password = param['password']
    signUp = param['signup'] # 회원가입이면 True, 동기화면 False

    possiblity = add_check(studentNum, password)
    if not possiblity:
        return "유효하지 않은 학번과 비밀번호"
    else: # 2. 메인 서버로 아이디, 패스워드 보내기
        cur = mysql.connection.cursor()

        dict_object = main(studentNum, password)

        name, major, minor, finished_semester, credit, cultures, scores, final_score, exam_papers, foreigns, major_required, minor_required = \
            dict_to_variables(dict_object)

        credit = json.dumps(credit, ensure_ascii=False, indent=4)
        cultures = json.dumps(cultures, ensure_ascii=False, indent=4)
        scores = json.dumps(scores, ensure_ascii=False, indent=4)
        exam_papers = json.dumps(exam_papers, ensure_ascii=False, indent=4)
        foreigns = json.dumps(foreigns, ensure_ascii=False, indent=4)
        major_required = json.dumps(major_required, ensure_ascii=False, indent=4)
        minor_required = json.dumps(minor_required, ensure_ascii=False, indent=4)  
        studentNum_json = json.dumps(studentNum, ensure_ascii=False, indent=4)
        password_json = json.dumps(password, ensure_ascii=False, indent=4)

        if signUp:
            cur.execute('INSERT INTO students (name, major, minor, finished_semester, credit, cultures, scores, final_score, exam_papers, foreigns, major_required, minor_required, student_num, password) VALUES ' + 
                    f"('{name}', '{major}', '{minor}', '{finished_semester}', '{credit}', '{cultures}', \
                    '{scores}', '{final_score}', '{exam_papers}', '{foreigns}', '{major_required}', '{minor_required}', '{studentNum_json}', '{password_json}' )")
        else: # 동기화 기능
            # cur.execute
        # 테이블 새로 까야됨
        # 동기화 시에, 다른 쿼리
            pass
        mysql.connection.commit()
        cur.close()

        return 'Data added successfully'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

