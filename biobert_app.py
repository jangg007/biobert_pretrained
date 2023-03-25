import streamlit as st
import numpy as np
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

@st.cache_resource
def get_model():

    tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-large-cased-v1.1-squad")
    model = AutoModelForQuestionAnswering.from_pretrained("dmis-lab/biobert-large-cased-v1.1-squad")
    return tokenizer,model

tokenizer, model = get_model()

user_input1 = st.text_area('Enter Question to analyze')
user_input2 = st.text_area('Enter the context text')
button = st.button('Analyze')


if user_input1 and user_input2 and button:
    test_sample = tokenizer([user_input1], [user_input2], return_tensors='pt')
    # test_sample
    outputs = model(**test_sample)
    answer_start_index = outputs.start_logits.detach().argmax()
    answer_end_index = outputs.end_logits.detach().argmax()

    predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
    ans = tokenizer.decode(predict_answer_tokens)

    st.write("Answer : ",ans)



# pip install -r .\requirements.txt
# streamlit run .\biobert_app.py

# git init
# git add .\biobert_app.py .\requirements.txt
# git commit -m 'first commit'
# git branch -M main
# git push -u origin main