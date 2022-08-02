FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY ./ /code
WORKDIR /code
RUN pip3 install -r requirement.txt

EXPOSE 8000

CMD ["/bin/bash", "start_api.sh"]
