import streamlit as st
from knowledge_base import KnowledgeBaseClient

# Page config
st.set_page_config(page_title="Shellkode Bedrock Knowledge Base Chatbot", page_icon="🤖")

# Initialize client
@st.cache_resource
def get_kb_client():
    return KnowledgeBaseClient()

kb_client = get_kb_client()

# Sidebar
st.sidebar.title("Options")
mode = st.sidebar.radio(
    "Choose mode:",
    ["Retrieve", "Retrieve & Generate"]
)

# Main interface
st.title("🤖 Shellkode Bedrock Chatbot")
st.write(f"Current mode: **{mode}**")

# Input
user_query = st.text_input("Enter your question:", placeholder="Ask me anything...")

if st.button("Submit") and user_query:
    with st.spinner("Processing..."):
        try:
            if mode == "Retrieve":
                response = kb_client.retrieve(user_query)
                st.subheader("Retrieved Documents:")
                for i, result in enumerate(response.get('retrievalResults', []), 1):
                    with st.expander(f"Document {i}"):
                        st.write(result.get('content', {}).get('text', 'No content'))
                        if 'location' in result:
                            st.caption(f"Source: {result['location'].get('s3Location', {}).get('uri', 'Unknown')}")
            
            else:  # Retrieve & Generate
                response = kb_client.retrieve_and_generate(user_query)
                st.subheader("Generated Response:")
                st.write(response.get('output', {}).get('text', 'No response generated'))
                
                # Show sources if available
                citations = response.get('citations', [])
                if citations:
                    st.subheader("Sources:")
                    for i, citation in enumerate(citations, 1):
                        with st.expander(f"Source {i}"):
                            for ref in citation.get('retrievedReferences', []):
                                st.write(ref.get('content', {}).get('text', 'No content'))
        
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Instructions
with st.expander("ℹ️ How to use"):
    st.write("""
    1. **Retrieve**: Get relevant documents from the knowledge base
    2. **Retrieve & Generate**: Get an AI-generated answer based on the knowledge base
    3. Enter your question and click Submit
    """)