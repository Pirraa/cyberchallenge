FROM python:3.10 as python-base
RUN mkdir backend
WORKDIR  /backend
COPY /pyproject.toml /backend
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
COPY . .
EXPOSE 8888/tcp
CMD ["poetry", "run", "start"]
