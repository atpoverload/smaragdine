FROM python:3.8

# Install debian packages
RUN apt-get install -y git

# Grab the repo
RUN git clone https://github.com/project-smaragdine/smaragdine.git

# Setup python
RUN cd smaragdine && bash setup.sh

# Setup eflect
ENTRYPOINT modprobe msr && /bin/bash
