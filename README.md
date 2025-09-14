
## 项目使用
### 1.安装依赖
```
pip install -r requirements.txt
```

### 2.启动项目
```
uvicorn src.main:app --reload
```

## docker
### build
```
docker build -t gis-api .
```

## run
```
docker run -d -p 8000:8000 --name gis-api-container gis-api
```

### docker-compose
```
version: "3.9"
services:
  gis-api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./src:/app/src
      - ./config:/app/config
    env_file:
      - ./config/.env
```