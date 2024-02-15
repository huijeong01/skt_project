#특정 폴더 안에 있는 Json 파일들의 speaker의 성별 나이의 분포도를 있도록 하는 코드

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

        for speaker in data['speaker']:
            sex = speaker['sex']
            age = int((speaker['age'])[:2])
            
            if sex:
                sexs.append(sex)
                ages.append(age)
                sexs_ages.append([sex,age])
            
# 성별 및 연령대별 데이터 집계
sex_age_count = {}
for sex, age in sexs_ages:
    key = (sex, age)
    if key in sex_age_count:
        sex_age_count[key] += 1
    else:
        sex_age_count[key] = 1

# 데이터를 시각화하기 위한 준비
labels = [f"{sex}, {age}" for sex, age in sex_age_count.keys()]
counts = [count for count in sex_age_count.values()]


plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# 막대그래프 그리기
plt.figure(figsize=(10, 8))  # 그래프 크기 설정
bars = plt.bar(labels, counts, color='skyblue')  # 막대그래프 그리기
plt.xlabel('Sex, Age')  # x축 라벨
plt.ylabel('Count')  # y축 라벨
plt.title('Count of Each Sex and Age Combination')  # 그래프 제목
plt.xticks(rotation=45)  # x축 라벨 회전

# 막대 위에 정확한 수치 추가
for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width() / 2, count, str(count), ha='center', va='bottom')

plt.show()


