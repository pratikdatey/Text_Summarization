FROM python:3.9.16-slim-buster
COPY . D:\DATA_SCIENCE\Extra_Projects\Text_Summarization
EXPOSE 9000
WORKDIR D:\DATA_SCIENCE\Extra_Projects\Text_Summarization
RUN pip install -r requirements.txt
RUN python -m spacy download en
CMD python text_sammrization.py