import streamlit as st
import os
from langchain.vectorstores import Pinecone
import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

def generate_response(question):
    text_field = "text"

    pinecone.init(api_key=st.secrets["PINECONE_API_KEY"],environment='gcp-starter')
    # switch back to normal index for langchain
    index = pinecone.Index(st.secrets["INDEX_NAME"] )
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

    vectorstore = Pinecone(index, OpenAIEmbeddings(), text_field)

    #LLM setup
    llm = OpenAI(temperature=0, model_name='gpt-3.5-turbo', openai_api_key=st.secrets["OPENAI_API_KEY"])

    #previous model
    qa_with_sources = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )

    #current model
    prompt_template = """
    Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you 
    don't know or ask the user to provide more context. Do not ever try to make up an answer and always provide a source document. 
    All of the questions asked here are only related to Veeva CRM administration, so always answer as if you’re talking to a Veeva CRM administrator.
    {context}
    Question: {question}
    """

    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    chain_type_kwargs = {"prompt": PROMPT}
    
    qa = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=vectorstore.as_retriever(search_type="mmr", search_kwargs={'fetch_k': 30, 'k':4},chain_type_kwargs=chain_type_kwargs), 
        return_source_documents=True)

    result = qa({"query": question})

    return result

def app():
    st.set_page_config(page_title="🤖🔗 AdminHelpep")
    st.title('🤖🔗 AdminHelper')

    st.markdown("How can I help you? Ask your question below.")

    user_input = st.text_area("Question:")
    if st.button("Submit"):
        if user_input:
            response = generate_response(user_input)
            
            # Response Section
            st.header("Response")
            st.write(response['result'].strip())
            st.write("---")  # Horizontal line as a separator

            # Source(s) Section
            st.header("Source(s)")
            for document in response['source_documents']:
                st.text(f"{document.metadata['title']}")
                with st.expander("Show more"):
                    st.write(document.page_content)
                st.markdown(f"**Source:** {document.metadata['source']}")
                st.write("---")  # Horizontal line as a separator

        else:
            st.error("Please enter your question.")

if __name__ == "__main__":
    app()
