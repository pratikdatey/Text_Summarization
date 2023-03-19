FROM ubuntu:18.04
COPY . D:/DATA_SCIENCE/Extra_Projects/Text_Summarization
EXPOSE 9000
WORKDIR D:/DATA_SCIENCE/Extra_Projects/Text_Summarization
RUN apt-get update
RUN apt-get remove --purge -y python3.7
CMD python3 text_sammrization.py

