# 목표 : chatgpt finetuning을 위해 jsonl 파일을 만든다.
# 1. 한 json 파일의  dialect_form, standard_form 을 추출한다.
#      이때, json dialect_form에 (),*,&가 있는 경우의 dialect_form은 제거.
# 2. 여러 json 파일의 dialect_form, standard_form을 하나의 jsonl 파일로 만든다
# 3. 만든 jsonl 파일을 openai에 올린다.
# 4. fine-tuning 진행
# few-shot learning(실행할 때마다 mapping data를 실행한다.) vs fine-tuning (완전히 새로운 model을 만든다)

# ---------
# 여러 json 파일의 dialect_form, standard_form을 가져온다. 

import os
import json

# JSON 파일이 있는 실제 디렉토리 경로로 변경하세요.
directory_path = 'C:/skt/project/label_train_valid_original'

# 괄호, *, &를 제외한 dialect_form과 그에 대응하는 standard_form을 담을 리스트
filtered_dialect_forms = []
filtered_standard_forms = []

for filename in os.listdir(directory_path):
    if filename.endswith('.json'):
        with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            for utterance in data.get('utterance', []):
                dialect_form = utterance.get('dialect_form', '').strip()
                standard_form = utterance.get('standard_form', '').strip()
                
                # 괄호, &, *가 없고, 공백이 양 끝에 없는 경우 리스트에 추가
                if not any(char in dialect_form for char in ['[', ']', '(', ')', '{', '}', '&', '*']):
                    filtered_dialect_forms.append(dialect_form)
                    filtered_standard_forms.append(standard_form)

# 결과 출력
print("filtered_dialect_forms count : " + str(len(filtered_dialect_forms)))
print("filtered_standard_forms count : " + str(len(filtered_standard_forms)))

# JSONL 파일 경로 설정
output_file_path = 'C:/skt/project/code/skt_project/front_function/finetuningdata.jsonl'

with open(output_file_path, 'w', encoding='utf-8') as outfile:
    for standard_form, dialect_form in zip(filtered_standard_forms, filtered_dialect_forms):
        # 각각의 문장에 대한 메시지 객체 생성
        message_obj = {
            "messages": [
                {"role": "system", "content": "You translate standard Korean to Jeju dialect"},
                {"role": "user", "content": f"Translate from Korean to Jeju dialect the following text: {standard_form}"},
                {"role": "assistant", "content": dialect_form}
            ]
        }
        # JSONL 파일에 한 줄로 쓰기
        json.dump(message_obj, outfile, ensure_ascii=False)
        outfile.write('\n')  # 각 객체 후에 줄바꿈 추가

print(f"Data has been written to {output_file_path}")
