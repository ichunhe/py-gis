# 1. 베이스 이미지
FROM python:3.11-slim

# 환경변수 설정 → apt가 항상 비대화형 모드로 동작
ENV DEBIAN_FRONTEND=noninteractive

# 2. 작업 디렉토리 생성
WORKDIR /app

# 3. 시스템 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gdal-bin \
    && rm -rf /var/lib/apt/lists/*

# 4. 의존성 복사 및 설치
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 5. 소스 코드 복사
COPY ./src ./src

# 6. 환경 변수
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# 7. FastAPI 서버 실행
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
