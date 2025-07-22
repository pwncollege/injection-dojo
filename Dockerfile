FROM pwncollege/challenge-legacy:latest

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libxml2-dev libxslt-dev python3-dev python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install lxml

USER hacker