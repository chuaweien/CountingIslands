FROM python:3.8.2-alpine

ARG PROJECT_USER="jovyan"
ARG PROJECT_GROUP="project"
ARG HOME_DIR="/home/jovyan"
ARG USER_UID=2222
ARG USER_GID=2222

ARG filepath
RUN test -n "${filepath}" || (echo "filepath not set" && false)
ENV filepath=${filepath}

# install bash
RUN apk update && apk add bash

# set shell to bash
SHELL ["/bin/bash", "-c"]

WORKDIR ${HOME_DIR}

# add project user
RUN addgroup -g ${USER_GID} ${PROJECT_GROUP} \
    && adduser -h ${HOME_DIR} -s /bin/bash -G ${PROJECT_GROUP} -u ${USER_UID} ${PROJECT_USER} -D

COPY .  .

# change ownership of files to user
# and make shell script executable
RUN chown -R ${PROJECT_USER} . && chgrp -R ${PROJECT_GROUP} . \
    && chmod +x run.sh \
    && python setup.py install

# change to project user
USER ${PROJECT_USER}

# RUN python setup.py install

ENTRYPOINT ./run.sh ${filepath}

