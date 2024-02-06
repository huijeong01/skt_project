#Json 파일의 utterance['dialect_form']에 괄호,&,* 셋 중 하나라도 있으면 그 json 파일을 삭제하는 코드

import os
import json

# JSON 파일이 있는 실제 디렉토리 경로로 변경하세요.
directory_path = 'C:/skt/project/label_train_valid'

dialect_forms_count = 0
dialect_forms_without_brackets_and_star = 0

for filename in os.listdir(directory_path):
    if filename.endswith('.json'):
        with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as file:
            data = json.load(file)
            for utterance in data.get('utterance', []) :
                dialect_forms_count += 1
                dialect_form = utterance.get('dialect_form', '')
                    
                # 괄호 또는 '&' 또는 '*가 없는 경우의 개수 세기
                if not any(char in dialect_form for char in ['[', ']', '(', ')', '{', '}', '&', '*']):
                    dialect_forms_without_brackets_and_star += 1

                
                    
print(f'전체 dialect_form 전체 개수 : {dialect_forms_count}')
print(f"괄호, &, *가 없는 dialect form의 개수: {dialect_forms_without_brackets_and_star}")