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

RUN --mount=target=/var/lib/apt/lists,type=cache,sharing=locked \
    --mount=target=/var/cache/apt,type=cache,sharing=locked \
    rm -f /etc/apt/apt.conf.d/docker-clean \
    && apt-get update \
    && apt-get -y --no-install-recommends install \
    tesseract-ocr tesseract-ocr-spa poppler-utils


COPY app .

EXPOSE 8000

CMD 