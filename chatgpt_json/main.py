from fastapi import FastAPI, HTTPException
import httpx
from starlette.responses import JSONResponse

app = FastAPI()

# OpenAI API 설정
OPENAI_API_KEY = "발급받은 openai_api_key 입력"

# 프롬프트 템플릿 정의
def generate_prompt(standard_korean: str) -> str:
    prompt_template = f"""
너는 표준 한국어를 경상도 사투리로 바꾸는 번역기이다. 표준 한국어 문장을 경상도 사투리로 번역해줘.

표준 한국어: "{standard_korean}"
경상도 사투리로 번역:
"""
    return prompt_template

@app.post("/translate/")
async def translate(text: str):
    prompt = generate_prompt(text)
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "다음 문장을 경상도 사투리로 번역해주세요."},
            {"role": "user", "content": prompt}
        ]
    }

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
            if response.status_code == 200:
                # API 응답에서 경상도 사투리 번역 결과를 추출
                translation = response.json()['choices'][0]['message']['content']
                return JSONResponse(content={"translation": translation}, status_code=200)
            else:
                # API 호출 실패 시 오류 메시지 반환
                return JSONResponse(content={"error": "API 호출에 실패했습니다.", "details": response.text}, status_code=response.status_code)
    except Exception as e:
        # 서버 내부 오류 처리
        return JSONResponse(content={"error": "서버 내부 오류가 발생했습니다.", "details": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)