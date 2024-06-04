FROM python:alpine3.11 AS PipenvStage

WORKDIR /tmp
RUN --mount=type=cache,target=/root/.cache/pip,mode=775 pip3 install pipenv

COPY Pipfile* .
RUN --mount=type=cache,target=/root/.cache/pipenv,mode=775 pipenv requirements > ./requirements.txt

FROM python:3.11-slim

WORKDIR /opt/app/
COPY --from=PipenvStage /tmp/requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip,mode=775 pip3 install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip,mode=775 pip3 install -r requirements.txt

COPY document-search-api .

EXPOSE 8000

CMD uvicorn main:app --reload --host 0.0.0.0