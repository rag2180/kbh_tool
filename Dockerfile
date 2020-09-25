FROM ubuntu:18.04

ENV TZ=Asia/Kolkata

RUN apt-get update && \
    apt-get dist-upgrade --yes && \
	apt-get install -y python3-dev python3-pip libssl-dev libcurl4-openssl-dev git rabbitmq-server curl p7zip-full man-db && \
	pip3 install --upgrade pip && \
	pip3 install --no-cache-dir --upgrade pyinotify || \
	apt-get autoremove -y && apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

ADD . /root/kbh_tool/
RUN pip3 install --no-cache-dir --trusted-host pypi.python.org -r /root/kbh_tool/requirements.txt

ENTRYPOINT /bin/bash

EXPOSE 8000