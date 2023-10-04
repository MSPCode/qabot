import streamlit as st

class Document:
    def __init__(self, page_content, metadata):
        self.page_content = page_content
        self.metadata = metadata

def generate_response(question):
    # Placeholder for your generate_response function
    # Return a list of Document objects for demonstration
    documents = [
        Document("This is the first document's content.", {"source": "https://google.com", "title": "Title 1"}),
        Document("This is the second document's content.", {"source": "https://google.com", "title": "Title 2"})
    ]
    return documents

def app():
    st.title("Question Answering App")

    st.markdown("How can I help you? Ask your question below.")

    user_input = st.text_area("Your Question:")
    if st.button("Submit"):
        if user_input:
            response = generate_response(user_input)
            
            # Response Section
            st.header("Response")
            for document in response:
                st.text(document.metadata['title'])
                st.write("---")  # Horizontal line as a separator

            # Source(s) Section
            st.header("Source(s)")
            for document in response:
                st.text(f"{document.metadata['title']} (First 25 words)")
                st.text(document.page_content[:25])
                if len(document.page_content) > 25:
                    with st.expander("Show more"):
                        st.text(document.page_content[25:])
                st.text(f"**Source:** {document.metadata['source']}")
                st.write("---")  # Horizontal line as a separator

        else:
            st.error("Please enter your question.")

if __name__ == "__main__":
    app()
