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
                st.markdown(f"""
                    <div style='border:2px solid black; padding:10px; margin-bottom:10px; word-wrap: break-word;'>
                        <strong>{document.metadata['title']}</strong> (First 25 words)
                        <br>
                        {document.page_content[:25]}
                        <details>
                            <summary>Show more</summary>
                            {document.page_content[25:]}
                        </details>
                        <br>
                        <strong>Source:</strong> {document.metadata['source']}
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Please enter your question.")

if __name__ == "__main__":
    app()
