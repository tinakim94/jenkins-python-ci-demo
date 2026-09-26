# Jenkins Python CI Demo

GitHub 저장소와 Jenkins를 연동하여 Python 애플리케이션의 테스트를 수행하는
기초 CI Pipeline 실습 프로젝트입니다.

단순히 Jenkins를 설치하는 데 그치지 않고,
테스트 실패 시 이후 Stage가 중단되는 흐름을 확인하고
코드를 수정한 뒤 정상 빌드로 복구하는 과정까지 실습했습니다.

---

## Project Goal

- Jenkins Pipeline 기본 구조 이해
- GitHub 저장소와 Jenkins SCM 연동
- Jenkinsfile 기반 Pipeline 구성
- Python unittest 자동 실행
- 테스트 실패 시 Pipeline 중단 확인
- 코드 수정 후 재빌드를 통한 정상 상태 복구

---

## CI Pipeline

```text
GitHub Repository
        |
        v
Jenkins SCM Checkout
        |
        v
Read Jenkinsfile
        |
        v
      Test
python -m unittest -v
        |
   +----+----+
   |         |
Success    Failure
   |         |
   v         v
  Run      Stop
python     Pipeline
app.py