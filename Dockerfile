FROM ubuntu:18.04

RUN apt update
RUN apt install -y python3 python3-dev python3-pip python3-venv libmysqlclient-dev virtualenv gcc make

RUN pip3 install jupyter

EXPOSE 8888
WORKDIR /myapp

COPY requirements.txt ./

RUN cat requirements.txt | grep -v "pkg-resources==" > requirements_new.txt
RUN mv requirements_new.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./ /myapp

# run ember server on container start
ENTRYPOINT ["jupyter notebook --no-browser"]
