import time
import json


from crawling_utils import entranceSystem, getName, getMajor, getClassNumberList, getClassNumberList, getClassList, getExamPapers, getForeignOthers, getCultures, refresh, close
from general_utils import jsonify


# 예외 처리 아직 안함 ex) 전공심화 -> 차후 처리
def main(id, password):
    entranceSystem(id, password)
    refresh()

    name = getName()
    refresh()

    major,minor,double_major = getMajor() # 국제통상 (International Economics and Law) AI융합전공(Software&AI) (Artificial Intelligence Convergence(Software&AI) ) True
    refresh()

    credit = getClassNumberList() # [45.0, 12.0, 0.0, 0.0, 30.0, 0.0, 0.0, 0.0, 87.0, 3.89]  # 1전공, 이중, 2전공, 실외, 교양, 부전공, 교직, 자선, 총취득, 총평점
    refresh()

    class_info, finished_semester = getClassList()  # [['AI융합전공(Software&AI)', 'V41009', ' 운영체제 (Operating System)', '이중', '3', 'B+', '', '', '', "2018 - 1"], ['미네르바교양대학(서울)', 'Y13101', ' Communicative English(1) : L/S (Communicative English(1) : L/S)', '교양', '3', 'B+', '', '', ''], ...], finished_semester 는 끝난 학기 수(ex) 6학기 재학 중이면 5)
    refresh()  

    exam_papers = getExamPapers() # [['1', '제1전공', '국제통상학과', '-', '-', '-', '-', '미완료', '-'], ['2', '이중전공', 'AI융합전공(Software&AI)', '-', '-', '-', '-', '미완료', '-']]
    refresh()

    foreign_others = getForeignOthers() # [['1', '-', '-', '-', '미완료', '-']]
    refresh()

    culture_list = getCultures()  # [['인성교육', '0', '0', '(None)'], ['세계시민교육', '0', '0', '(None)'], ...]
    close()

    dict_object = jsonify(name, major, minor, double_major, credit, class_info, finished_semester, exam_papers, foreign_others, culture_list)
    
    return dict_object