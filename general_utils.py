import pandas as pd

def fill_dict(list_, dict_, grade_dict):
    for major in list_:
        local_semester = major[-1]  # "2018 - 1"
        hour = int(major[4]) # 3
        grade = grade_dict[major[5]] # 4.5
        if grade == None:   # PASS case
            continue

        try:
            local_list = dict_[local_semester] # [3, 13.5]
            first_variable = local_list[0]
            second_variable = local_list[1]
            first_variable += hour
            second_variable += (hour * grade)
            dict_[local_semester] = [first_variable, second_variable]
        
        except:
            dict_[local_semester] = [hour, hour*grade]
    
    for key,value in dict_.items():
        dict_[key] = value[1] / value[0]

# 전공, 학번, 이중유무  # 
def check(class_info, major, num, second): # [['AI융합전공(Software&AI)', 'V41009', ' 운영체제 (Operating System)', '이중', '3', 'B+', '', '', '', "2018 - 1"], ['미네르바교양대학(서울)', 'Y13101', ' Communicative English(1) : L/S (Communicative English(1) : L/S)', '교양', '3', 'B+', '', '', ''], ...]
    

    # committed_list = []
    # for i in class_list:
    #     for j in required_list:
    #         if (i in j) | (j in i):
    #             committed_list.append(i)


    class_list = []   # ['V410090', 'V410091', ...]
    for class_ in class_info:
        # idx = class_[2].rfind('(')
        # class_list.append(class_[2][:idx].replace(' ', ''))
        class_list.append(class_[1])    

    if "ELLT" in major:

        required_list = ['A011273', 'A011283', 'A011210', 'A102031']

        if num >= 2018:

            for i in class_list:

                if "General" in i:
                    required_list.append('A017401')
                    required_list.append('A101041')

                elif "Honors" in i:
                    required_list.append('A017411')
                    required_list.append('A101051')


            if (num >= 2018) and (second == True):
                required_list.remove('A102031')

    elif "Diplomacy" in major:
        required_list = ['C011231', 'C011241', 'C011251', 'C011261', 'C011331', 'C011341']
        
        if num >= 2017:
            required_list.append('C011351')
            required_list.append('C011361')
            required_list.append('C011634')
            required_list.append('C011902')
            required_list.append('C011913')
            required_list.append('C011922')
        if num >= 2023:
            required_list.append('C011931')
            required_list.append('C011991')

    elif "국제학" in major:
        required_list = ['D01101G', 'D01102H', 'K011062', 'K012472', 'K011013']

        if (num >= 2019):
            if (second == True):
                pass
            else:
                required_list.append('K011043')
                required_list.append('K011092')
                required_list.append('K011102')
    
    elif '말레이' in major:
        required_list = ['B031104', 'B031091', 'B034931', 'B034691', 'B031113', 'B031311', 'O031155', 'B032291', 'B031263']
        if num >= 2022:
            required_list.append('B032063')
            required_list.append('O032023')

    
    elif '뉴미디어' in major:
        required_list = ['C045311', 'C045321', 'C045291', 'C045341', 'C034011', 'C073011']

        if num <= 2018:
            required_list.append('C044922')
        else:
            required_list.append('C044751')

    elif '이탈리아' in major:
        required_list = ['A061023']

        if num <= 2018:
            required_list.append('A062123')
            required_list.append('A061023')

        else:
            required_list.append('A061054')
            required_list.append('A061062')

    elif '스페인' in major:
        required_list = ['A054832', 'A054851', 'A054842', 'A054861']

        if num <= 2016:
            required_list.append('A051111')
            required_list.append('A051151')
            required_list.append('A052371')
            required_list.append('A052391')
            required_list.append('A053831')
            required_list.append('A053851')

            required_list.append('A051121')
            required_list.append('A051151')
            required_list.append('A052381')
            required_list.append('A052391')
            required_list.append('A053841')
            required_list.append('A053861')


        if (num >= 2017) and (num <= 2019):
            required_list.append('J110051')
            required_list.append('J110201')


    elif '중국언어문화' in major:
        required_list = ['B013713', 'B012151']

        if num >= 2021:
            required_list.append('B015481')
            required_list.append('B015242')

        if num >= 2023:
            required_list.append('B014243')

    
    elif '스칸' in major:
        required_list = ['A093231', 'A093261']

        if num <= 2020:
            required_list.append('A091072')
            required_list.append('A091082')

        if num >= 2022:
            required_list.append('A093692')
            required_list.append('A091151')
            required_list.append('A092072')
            required_list.append('A093222')
            required_list.append('A093272')
            required_list.append('A093691')

    elif '포르' in major:
        required_list = ['A071151', 'A072072', 'A071342', 'A073171', 'A071162', 'A072082', 'A074661', 'N073272']

        if num == 2016:
            required_list.append('A074671')
            required_list.append('A071361')

        elif (num >= 2017) and (num <= 2020):
            required_list.append('A071361')
            required_list.append('A071361')
            required_list.append('A071012')
            required_list.append('A074652')
            required_list.append('A071461')
            required_list.append('A074671')
            required_list.append('A071382')
            required_list.append('A071022')
        
        elif num == 2021:
            required_list.append('A071361')
            required_list.append('A071361')
            required_list.append('A071012')
            required_list.append('A074652')
            required_list.append('A071382')

        elif (num == 2022) or (num == 2023):
            required_list.append('A071382')
            required_list.append('A074652')

        else:
            pass

    else:
        df = pd.read_excel('전필 및 학수번호.xlsx', index_col=0)
        required_list = df[[(i in major) | (major in i) for i in df['학과명']]]['학수번호'].apply(lambda x: x[:7]).tolist() # [초급프랑스어강독(1), ...]

    committed_list = []
    for i in class_list:
        for j in required_list:
            if (i in j) or (j in i):
                committed_list.append(i)

    if len(required_list) == 0:
        percent = 100
    else:
        percent = len(committed_list) / len(required_list)

    class_names = df['과목명'] 
    class_nums = df['학수번호']
    def find_indexes(series, search_string):
        return series[series.str.contains(search_string)].index

    required_list = pd.Series(required_list).apply(lambda x : find_indexes(class_nums, x)[0]).apply(lambda x: class_names[x]).to_list()
    committed_list = pd.Series(committed_list).apply(lambda x : find_indexes(class_nums, x)[0]).apply(lambda x: class_names[x]).to_list()


    return {'전필과목' : required_list, '수강과목' : committed_list, '수강완료율' : percent}



def dict_to_variables(dict_):  # dict_ : json object

    name = dict_['name']
    major = dict_['major']
    minor = dict_['minor']
    finished_semester = dict_['finished_semester']
    credit = dict_['credit'] # 영역별 이수 학점
    cultures = dict_['cultures'] # 교양 영역별 이수 학점
    scores = dict_['scores'] # 학기별 평점
    final_score = dict_['final_score'] # 최종 평점
    exam_papers = dict_['exam_papers']
    foreigns = dict_['foreigns']
    major_required = dict_['1전공']
    minor_required = dict_['이중전공']

    return name, major, minor, finished_semester, credit, cultures, scores, final_score, exam_papers, foreigns, major_required, minor_required



def jsonify(name, major, minor, double_major, credit, class_info, finished_semester, exam_papers, foreign_others, culture_list, num):
    
    global_dict = {}

    # 1. 이름
    global_dict['name'] = name

    # 2. 1전공 
    global_dict['major'] = major

    # 3. 2전공
    global_dict['minor'] = minor

    # 4. 진행학기
    global_dict['finished_semester'] = finished_semester

    # 5. 영역별 이수 학점
    local_list = ['1전공', '이중', '2전공', '실외', '교양', '부전공', '교직', '자선', '총취득', '총평점']
    local_dict = {}
    for i, j in zip(local_list, credit):
        if i != '총평점':
            local_dict[i] = int(j)   # key : '1전공' , value : 12
        else:
            local_dict[i] = float(j)
    global_dict['credit'] = local_dict # [45.0, 12.0, 0.0, 0.0, 30.0, 0.0, 0.0, 0.0, 87.0, 3.89]  # 1전공, 이중, 2전공, 실외, 교양, 부전공, 교직, 자선, 총취득, 총평점

    # 6. 교양 영역별 이수 학점
    local_dict = {}                  # {'인성교육' : 0, '세계시민교육' : 0} ...

    for local_list in culture_list: # [['인성교육', '0', '0', '(None)'], ['세계시민교육', '0', '0', '(None)'], ...]
        name = local_list[0]   # 세계시민교육
        number = int(local_list[2])  # 0
        local_dict[name] = number
    
    required_list = get_culture_required_list(num) #  {'미네르바인문' : 6, '대학외국어' : 6, '신입생세미나' : 1 ...}
    taking_list = {'미네르바인문' : local_dict['미네르바인문'], '대학외국어' : local_dict['대학외국어'],
                    '신입생세미나' : local_dict['신입생세미나'], 'HUFS CAREER' : local_dict['HUFS CARRER'],
                    '핵심인문기초' : local_dict['핵심인문기초'], '소프트웨어' : local_dict['소프트웨어'],
                    }
    
    local_num = 0
    local_list = ['언어와문학', '문화와예술', '역사와철학', '인간과사회', '과학과기술']
    for key, value in local_dict.items():
        if (key in local_list) and (value >= 2):
            local_num += 2
            local_list.remove(key)
    taking_list['핵심교양'] = local_num

    local_dict2 = {}

    local_dict2['교양필수학점'] = required_list
    local_dict2['교필수강학점'] = taking_list 


    global_dict['cultures'] = local_dict2

    # 7. 학기별 평점  [['국제통상학과','D02103',' Mathematics for Economics (Mathematics for Economics)','1전공','3','A+','', '', '', "2018 - 1"], ... ]

    local_major_list = [] # 본전공
    local_minor_list = [] # 이중전공 # 이중전공만 생각 -> 부전 일단 고려 x 
    local_culture_list = [] # 교양
    local_major_dict = {}             # {'2018 - 1' : [10, 45] ...} -> {'2018 - 1' : 4.5, ...}
    local_minor_dict = {}
    local_culture_dict = {}
    sum_dict = {}
    grade_dict = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0, "PASS" : None}

    for lecture in class_info:
        local_variable = lecture[3]

        if local_variable == '1전공':
            local_major_list.append(lecture)
        elif local_variable == '이중':
            local_minor_list.append(lecture)
        elif local_variable == '교양':
            local_culture_list.append(lecture)
    
    fill_dict(local_major_list, local_major_dict, grade_dict)
    fill_dict(local_minor_list, local_minor_dict, grade_dict)
    fill_dict(local_culture_list, local_culture_dict, grade_dict)

    sum_dict['major'] = local_major_dict
    sum_dict['minor'] = local_minor_dict
    sum_dict['culture'] = local_culture_dict

    global_dict['scores'] = sum_dict

    # 8. 최종평점

    final_score = credit[-1]
    global_dict['final_score'] = final_score

    # 9, 10. 1전공 졸업시험/논문 완료 여부 & 2전공 졸업시험/논문 완료 여부

    local_dict = {}
    for i in exam_papers: # [['1', '제1전공', '국제통상학과', '-', '-', '-', '-', '미완료', '-'], ['2', '이중전공', 'AI융합전공(Software&AI)', '-', '-', '-', '-', '미완료', '-']]
        local_dict[i[1]] = i[-2]  # {'제1전공' : '미완료', '이중전공' : '미완료'}

    global_dict['exam_papers'] = local_dict

    # 11. 외국어 인증 완료 여부 -> ?

    local_dict = {}
    for i in foreign_others: # [['1', '-', '-', '-', '미완료', '-']]
        local_dict[i[0]] = i[-2]
    
    global_dict['foreigns'] = local_dict

    # 12. 전필관련 처리
    global_dict['1전공'] = check(class_info, major, num, False)
    global_dict['이중전공'] = check(class_info, minor, num, True)

    return global_dict


def get_culture_required_list(num):  # 사범대 예외;;

    base_dict = {'미네르바인문' : 6, '대학외국어' : 6, '신입생세미나' : 1, 'HUFS CARRER' : 1, 
                 '핵심교양' : 0, '핵심인문기초' : 0, '소프트웨어' : 0}
    
    if num == 2016: # 16학번 대상
        base_dict['핵심교양'] = 6
    elif num <= 2019: # 17, 18, 19학번 대상
        base_dict['핵심교양'] = 4
        base_dict['핵심인문기초'] = 2
    elif num >= 2020: # 20학번 이후
        base_dict['소프트웨어'] = 3
        base_dict['핵심인문기초'] = 2

    return base_dict