# skt_project 

-------
## preprocessing 
1. 일반적인 whisper model에 넣기 위해 video를 30초 단위로 자른다. 
이때, 주의점!
   audio 파일을 30초에 근접하여 cut - 단, 발화 중간에 잘리지 않도록
       * 매 문장마다 cut하여 zero padding 했을 때
         1) 너무 오래 걸림
         2) zero padding이 너무 많아 제대로 학습되지 X


------
## backend
### whisper + chatgpt api 하여 오디오 파일 넣으면 제주도 방언으로 번역한 결과 나오도록 code 작성
- chatgot_json 폴더의 main.py code 확인 가능
- whisper model에 넣기 전 모든 전처리는 완료되었다는 가정하여 code 작성 (large model 이용시 확실히 성능이 좋음 다만 오래걸려서 이는 좀 생각해봐야할 듯)


-----
## Chatgpt finetuning
- front_function 폴더의 makejsonl.py, chatgpt_finetuning.py에서 code 확인 가능
- Chatgpt api를 그냥 넣었을 경우 제대로 표준어가 제대로 제주도 방언으로 번역되지 않음 -> chatgpt finetuning 진행할 필요 대두됨
1. 기존의 여러 json 파일의 dialect_form, standard_form을 추출하여 모두 가져와 하나의 jsonl 파일로 만듬.
 이때, 여러 json 파일의 dialect_form에 (),*,&가 있는 경우의 dialect_form은 제외하여 jsonl 파일로 만든다
2. 만든 jsonl 파일을 openai에 올린다.
3. fine-tuning 진행
  - few-shot learning(실행할 때마다 mapping data를 실행한다.) vs fine-tuning (완전히 새로운 model을 만든다 - 기존의 chatgpt model + 우리가 추가적으로 mapping한 data -> fine-tuning-model 생성됨, 실행할 때마다 mapping data 필요 X)



<!-- 
주제 변경 후 필요 없어짐
## preprocessing

1. delwomen20.py 실행 -> speakers가 모두 20대 여자인 발화자의 json 파일을 삭제 (20대 여자 발화자의 data가 불균형하게 너무 많음으로)

2. deldialect_cutaudio.py 실행
   - Json 파일의 dialect_form에 괄호(),{},[],&,*가 있는 경우 그에 대한 dialect_form 삭제
   - 그 삭제된 거에 맞춰서 audio 파일을 30초에 근접하여 cut - 단, 발화 중간에 잘리지 않도록
       * 매 문장마다 cut하여 zero padding 했을 때
         1) 너무 오래 걸림
         2) zero padding이 너무 많아 제대로 학습되지 X --> 
