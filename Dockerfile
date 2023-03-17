FROM ubuntu:18.04
COPY . D:/DATA_SCIENCE/Extra_Projects/Text_Summarization
EXPOSE 9000
WORKDIR D:/DATA_SCIENCE/Extra_Projects/Text_Summarization
CMD python3 text_sammrization.py

