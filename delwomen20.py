import os
import json
import os
import numpy as np
import matplotlib.pyplot as plt


# JSON 파일이 있는 폴더 경로 설정
folder_path = "C:/skt/project/label_train_valid" 

# 폴더 내의 모든 JSON 파일 검색 및 데이터 처리를 위한 리스트 초기화
sexs = []
ages = []
sexs_ages = []
dialect_sentences = []
women_20 = []

# 폴더 내의 모든 JSON 파일 순회
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        
        # JSON 파일 불러오기
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            
        # 여성이면서 20대인 발화자가 있는지 확인하기 위한 플래그
        is_woman_20 = False

        for speaker in data['speaker']:
            sex = speaker['sex']
            age = int((speaker['age'])[:2])
            
            if sex:
                sexs.append(sex)
                ages.append(age)
                sexs_ages.append([sex,age])
                
            # 모든 발화자가 여성이면서 20대인지 확인
            if sex == '여성' and age == 20:
                is_woman_20 = True
            else:
                # 한 명이라도 조건에 맞지 않으면 False로 설정
                is_woman_20 = False
                break  # 한 명이라도 조건에 맞지 않으면 더 이상 확인할 필요 없음
                
        # 해당 파일의 모든 발화자가 여성이면서 20대인 경우만 women_20에 추가
        if is_woman_20:
            women_20.append(data['id'])
            
# 모든 파일에 대한 처리가 끝난 후 결과 출력
print(ages[:10], sexs[:10], sexs_ages[:10])
print(np.unique(ages), np.unique(sexs), np.unique(sexs_ages))
print(len(women_20))
print(women_20[:10])

for file_name in women_20[0:651]:
    # 파일명에 확장자 ".json"을 추가
    file_name_with_extension = file_name + ".json"
    file_path = os.path.join(folder_path, file_name_with_extension)

    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_name_with_extension}를 삭제했습니다.")
    else:
        print(f"{file_name_with_extension}가 존재하지 않습니다.")
