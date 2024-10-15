## 1. 인스턴스 유형 선택 
GPU를 지원하는 인스턴스 유형을 선택해야 합니다. 
예시로 g4dn.xlarge, p3.2xlarge, p4d.24xlarge 등의 인스턴스를 사용할 수 있습니다.

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
# Add NVIDIA package repository
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
sudo apt-get install -y wget
wget https://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb

# Install the NVIDIA driver and CUDA
sudo apt-get update
sudo apt-get -y install cuda-drivers
```

- Driver 버전 확인
```bash
nvidia-smi
```
