# QA Bot
- What is Question-Answering?
- What is Semantic Search?
- What is BERT?
- How to develop a QA chatbot
- How to use the transformers library
- How to use the tensorflow-hub library

## 0. Question Answering
Write a function ``def question_answer(question, reference):`` that finds a snippet of text within a reference document to answer a question:

`- ``question`` is a string containing the question to answer
reference is a string containing the reference document from which to find the answer
Returns: a string containing the answer
If no answer is found, return None
Your function should use the bert-uncased-tf2-qa model from the tensorflow-hub library
Your function should use the pre-trained BertTokenizer, bert-large-uncased-whole-word-masking-finetuned-squad, from the transformers library

# Versions
Python 3.9
tensorflow-hub 0.16.1
transformers 4.37.2
