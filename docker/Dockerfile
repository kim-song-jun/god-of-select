FROM ubuntu:22.04

RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/kr.archive.ubuntu.com\/ubuntu\//' /etc/apt/sources.list


# 캐시 클리어 및 패키지 정보 업데이트

RUN rm -rf /var/lib/apt/lists
RUN mkdir /var/lib/apt/lists
RUN apt-get autoclean
RUN apt-get clean
# RUN rm -rf /var/lib/apt/lists/* 
RUN apt-get update -o Acquire::http::No-Cache=True -o Acquire::BrokenProxy=true

# Python 3.8과 관련 도구 설치
RUN apt-get install -y python3 python3-pip python3-distutils 
# tzdata 설정을 위한 환경변수 설정
ENV TZ=UTC

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && apt-get update \
    && apt-get install -y tzdata

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8080

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
