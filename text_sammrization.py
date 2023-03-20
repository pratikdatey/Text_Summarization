import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq  import nlargest

from flask import Flask,request,render_template

stop_words=list(STOP_WORDS)
app=Flask(__name__)

nlp=spacy.load('en_core_web_sm')

texts='''Summarization is the task of condensing a piece of text to a shorter version, reducing the size of the initial text while at the same time preserving key informational elements and the meaning of content. Since manual text summarization is a time expensive and generally laborious task, the automatization of the task is gaining increasing popularity and therefore constitutes a strong motivation for academic research. There are important applications for text summarization in various NLP related tasks such as text classification, question answering, legal texts summarization, news summarization, and headline generation. Moreover, the generation of summaries can be integrated into these systems as an intermediate stage which helps to reduce the length of the document. In the big data era, there has been an explosion in the amount of text data from a variety of sources. This volume of text is an inestimable source of information and knowledge which needs to be effectively summarized to be useful. This increasing availability of documents has demanded exhaustive research in the NLP area for automatic text summarization. Automatic text summarization is the task of producing a concise and fluent summary without any human help while preserving the meaning of the original text document. It is very challenging, because when we as humans summarize a piece of text, we usually read it entirely to develop our understanding, and then write a summary highlighting its main points. Since computers lack human knowledge and language capability, it makes automatic text summarization a very difficult and non-trivial task. Various models based on machine learning have been proposed for this task. Most of these approaches model this problem as a classification problem which outputs whether to include a sentence in the summary or not. Other approaches have used topic information, Latent Semantic Analysis (LSA), Sequence to Sequence models, Reinforcement Learning and Adversarial processes. In general, there are two different approaches for automatic summarization: extraction and abstraction.'''

op='''There are important applications for text summarization in various NLP related tasks such as text classification, question answering, legal texts summarization, news summarization, and headline generation. Automatic text summarization is the task of producing a concise and fluent summary without any human help while preserving the meaning of the original text document. Since manual text summarization is a time expensive and generally laborious task, the automatization of the task is gaining increasing popularity and therefore constitutes a strong motivation for academic research. Summarization is the task of condensing a piece of text to a shorter version, reducing the size of the initial text while at the same time preserving key informational elements and the meaning of content. Since computers lack human knowledge and language capability, it makes automatic text summarization a very difficult and non-trivial task. '''


punctuation=punctuation+'\n'
@app.route('/')
def page():
    return render_template('index1.html', input=texts,output=op)


@app.route('/',methods=['POST'])
def text():
    if request.method=="POST":
        percentage=int(request.form['percent'])
        percentage=(percentage/100)

        text=request.form['text']

        doc=nlp(text)
        word_frequency={}
        for word in doc:
            if word.text.lower() not in stop_words:
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequency:
                        word_frequency[word.text]=1
                    else:
                        word_frequency[word.text]+=1


        max_word_fre=max(word_frequency.values())

        for i in word_frequency.keys():
            word_frequency[i]=word_frequency[i]/max_word_fre

        sent_tokens=[sent for sent in doc.sents]

        sent_score={}
        for sent in sent_tokens:
            for word in sent:
                if word.text in word_frequency.keys():
                    if sent not in sent_score.keys():
                        sent_score[sent]=word_frequency[word.text]
                    else:
                        sent_score[sent]+=word_frequency[word.text]

        summary_percenatge=int(len(sent_score)*percentage)
        summary=nlargest(summary_percenatge,sent_score,key=sent_score.get)
        final=' '.join(sent.text for sent in summary)
        return render_template('index1.html',output=final,input=text)

if __name__=='__main__':
    app.run(debug=True)




