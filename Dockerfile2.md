Dockerfile```
# CUDA를 지원하는 Python 이미지 사용
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# 필요한 시스템 패키지 설치 및 Python 3.10 설치
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y \
    python3.10 \
    python3.10-distutils \
    python3.10-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Python 3.10을 기본 Python으로 설정
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
RUN update-alternatives --set python3 /usr/bin/python3.10

# pip 업그레이드
RUN python3 -m pip install --upgrade pip

WORKDIR /code

# Python 패키지 설치
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

# PyTorch와 torchvision 설치 (CUDA 11.8 지원 버전)
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# 애플리케이션 코드 복사
COPY . /code

# FastAPI 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```