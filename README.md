# skt_project

## preprocessing

1. delwomen20.py 실행 -> speakers가 모두 20대 여자인 발화자의 json 파일을 삭제 (20대 여자 발화자의 data가 불균형하게 너무 많음으로)

2. deldialect_cutaudio.py 실행
   - Json 파일의 dialect_form에 괄호(),{},[],&,*가 있는 경우 그에 대한 dialect_form 삭제
   - 그 삭제된 거에 맞춰서 audio 파일을 30초에 근접하여 cut - 단, 발화 중간에 잘리지 않도록
       * 매 문장마다 cut하여 zero padding 했을 때
         1) 너무 오래 걸림
         2) zero padding이 너무 많아 제대로 학습되지 X
