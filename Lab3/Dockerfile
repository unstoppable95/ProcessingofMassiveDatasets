FROM python:3.6-slim
#FROM ubuntu:latest

# Install latest updates
#RUN apt-get update
#RUN apt-get upgrade -y

#install software
RUN pip install pysqlite3

# Set working dir
WORKDIR .

# Copy dataset to working dir
COPY unique_tracks.txt .
COPY triplets_sample_20p.txt .

# Copy your code
COPY lab3.py .

# Set starting command (run your code)
CMD python lab3.py
