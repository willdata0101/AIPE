# Importing libraries
import boto3
from botocore.exceptions import ClientError

from pydantic import BaseModel
from langchain_community.llms import Bedrock
from langchain_aws import ChatBedrock
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
#from langchain.retrievers import WikipediaRetriever  # Example for RAG
from langchain_community.retrievers import WikipediaRetriever
from langchain_aws.retrievers import AmazonKnowledgeBasesRetriever
from langchain.memory import ConversationBufferMemory
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

import requests

import getpass

import json

import pprint as pp

# Setting session and region variables
session = boto3.Session()
region = session.region_name
bedrock_client = boto3.client('bedrock-runtime', region_name = region)

class Assistant():
    def __init__(self, bedrock_client):
        self.bedrock_client = bedrock_client  # Amazon Bedrock client for LLM
        #self.supported_languages = ["en", "es", "fr", "de"]  # Example language support
        self.memory = ConversationBufferMemory()  # Memory to track conversation flow
        self.retriever = WikipediaRetriever() # Example for RAG integration
        
    def handle_query(self, user_query):
        # Use Amazon Bedrock to generate a response
        llm = ChatBedrock(model_id="anthropic.claude-3-5-sonnet-20240620-v1:0")
        
        # Creating a system prompt to instruct the model how to answer the query
        system_prompt = (
            """
            You are an historical archives assistant
            tasked with answering questions based on
            archival records. Use the following
            historical documents to answer the question.
            If you don't know the answer, say you don't
            know. Keep the answer between 500-1000 words.
            If you're using a bulleted or numbered list,
            use a new line for each list item.
            \n\n
            {context}
            """
        )
            
        print("Researching your question...")

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}")
    
            ]
        )

        retriever = WikipediaRetriever()

        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        response = rag_chain.invoke({"input": user_query})
        return response


# user_query = "Tell me about D-Day in WWII."

# assistant = MultilingualHistoricalAssistant(user_query)

# response = assistant.handle_query(user_query)
# response = response['answer']
# clean_response = "".join(response)
# print(clean_response)
        
import streamlit as st

# Building streamlit app
st.title("Multilingual Historical Archive Assistant")

def run_assistant():
    with st.sidebar:
        with st.chat_message("assistant"):
            st.write("Hello 👋! Ask me anything about your historical documents.")

            with st.form("my_form"):
                text = st.text_area(
                    "Enter text:",
                )
                submitted = st.form_submit_button("Submit")
    
    if submitted:
        assistant = Assistant(bedrock_client)
        # Handle the query
        response = assistant.handle_query(text)
        clean_response = response['answer']
        clean_response = "".join(clean_response)
        st.write(clean_response)
    else:
        print()

run_assistant()