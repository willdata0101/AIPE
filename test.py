from MHAA import assistant
import streamlit as st

with st.sidebar:
    with st.chat_message("assistant"):
        st.write("Hello 👋! Ask me anything about your historical documents.")

        with st.form("my_form"):
            text = st.text_area(
                "Enter text:",
            )
            submitted = st.form_submit_button("Submit")
    
    if submitted:
        message = st.chat_message("assistant")
        message.write("Researching your question...")
        assistant = Assistant(bedrock_client)
        # Handle the query
        response = assistant.handle_query(text)
        clean_response = response['answer']
        clean_response = "".join(clean_response)
        st.write(clean_response)
    else:
        print()