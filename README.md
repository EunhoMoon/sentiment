# Sentiment Analysis
- Google Cloud Natural Language API를 이용한 감정 분석 서비스
- FastAPI를 이용한 서버 구축
- 추후 dairly와 연동해서 사용할 예정
### Requirements
- Python 3.11
- FastAPI
- Google Cloud Natural Language API
- MySQL(예정)
#### [Google Cloud Console](https://cloud.google.com/?hl=ko)
- service-account.json 발급 필요

#### Docker

- .env 파일 생성 및 환경 변수 설정
  ```dotenv
  SERVER_PORT={your-port}
  SERVICE_ACCOUNT_FILE={your-service-account-file-path}
  ```
- `docker compose up -d`

#### Swagger
- http://{your-ip}:{your-port}/docs

#### TODO
- [ ] Docker 환경 구축
  - [x] Docker Image 내부에 GCP 인증
- [ ] MySQL 연동
- [ ] 패키지 구조 변경
- [ ] jwt 토큰 인증