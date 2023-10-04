import streamlit as st

class Document:
    def __init__(self, page_content, metadata):
        self.page_content = page_content
        self.metadata = metadata

def generate_response(question):
    # Placeholder for your generate_response function
    # Return a list of Document objects for demonstration
    documents = [
        Document("This is the first document's contentqrqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwer.", {"source": "https://google.com", "title": "Title 1"}),
        Document("This is the second document's content.contentqrqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwercontentqrqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwercontentqrqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwercontentqrqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwercontentqrqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwercontentqrqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwerqwer", {"source": "google.com", "title": "Title 2"})
    ]
    return documents

def app():
    st.title("Question Answering App")

    st.markdown("How can I help you? Ask your question below.")

    user_input = st.text_area("Your Question:")
    if st.button("Submit"):
        if user_input:
            response = generate_response(user_input)
            st.header("Source(s)")
            for document in response:
                col1, col2 = st.columns([4, 1])  # Adjust ratio as needed
                with col1.expander(f"{document.metadata['title']} (First 25 words)"):
                    col1.write(document.page_content)
                col2.markdown(f"**Source:** {document.metadata['source']}")
        else:
            st.error("Please enter your question.")

if __name__ == "__main__":
    app()
