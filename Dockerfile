FROM python:3.9.16-slim
COPY . D:\DATA_SCIENCE\Extra_Projects\Text_Summarization
WORKDIR D:\DATA_SCIENCE\Extra_Projects\Text_Summarization
RUN pip install -r requirements.txt
RUN python -m spacy download 'en_core_web_sm'
CMD python text_sammrization.py