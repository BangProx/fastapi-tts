FROM python 3.10

RUN apt-get update && apt-get install -y \

WORKDIR /code

# Python 패키지 설치
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 애플리케이션 코드 복사
COPY . /code

# FastAPI 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
