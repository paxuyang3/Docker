# 파이썬 3.9 슬림 버전 사용
FROM python:3.9-slim

# 컨테이너 내 작업 폴더 설정
WORKDIR /app

# 필요 패키지 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 소스코드 복사
COPY . .

# 내부 포트 8000번 노출
EXPOSE 8000

# FastAPI 서버 실행 (0.0.0.0으로 열어야 외부 접속 가능)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
