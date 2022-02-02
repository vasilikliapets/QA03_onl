FROM alpine:latest
RUN apk add --update py3-pip
COPY requirements.txt /usr/bin/app/
RUN pip install --no-cache-dir -r /usr/bin/app/requirements.txt
COPY app.py /usr/bin/app
EXPOSE 5000
CMD ["python3", "/usr/bin/app/app.py"]