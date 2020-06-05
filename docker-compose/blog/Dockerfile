FROM python:3.6-alpine
ENV PYTHONUNBuFFERED 1
WORKDIR /app/ratplanA
COPY . ./
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk update \
    && cat requirements/alpine_requirements.txt | xargs apk add
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements/requirements.txt
EXPOSE 8000
ENTRYPOINT gunicorn --chdir myblog blogproject.wsgi -k gthread -b 127.0.0.1:8000 &>> /var/log/myblog.log
