## 1. 인스턴스 유형 선택 
GPU를 지원하는 인스턴스 유형을 선택해야 합니다. 
예시로 g4dn.xlarge, p3.2xlarge, p4d.24xlarge 등의 인스턴스를 사용할 수 있습니다.
-> 현재 서버 스펙
- g4dn.xlarge
- vCPU : 4


## 2. 인스턴스 접속
알아서 ssh로

## 3. Nvidia 드라이버 설치
- system update
```bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y build-essential
```

- Driver 설치
```bash
sudo apt-get install -y nvidia-driver-525
sudo reboot
```
- 재부팅 후 다시 SSH로 접속합니다.
- Driver 버전 확인
```bash
nvidia-smi
```
## 4. CUDA 툴킷 설치

```bash
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
sudo sh cuda_11.8.0_520.61.05_linux.run
```
- 설치 과정에서 드라이버 설치는 건너뛰고 CUDA 툴킷만 설치합니다.
## 5. 환경 변수 설정
```bash
echo 'export PATH=/usr/local/cuda-11.8/bin${PATH:+:${PATH}}' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
source ~/.bashrc
```
## 6. Docker 설치
```bash
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce
```

## 7. NVIDIA Container Toolkit 설치
```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

## 8. Docker Compose 설치
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## 9. 프로젝트 클론 및 설정
```bash
git clone <file 경로>
cd <file 경로>
```

## 10. Docker 컨테이너 빌드 및 실행
```bash
sudo docker-compose up --build
```