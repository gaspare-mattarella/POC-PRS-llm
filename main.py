import os
import streamlit as st
import mailtrap as mt
from utils import doc_loader, summary_prompt_creator, doc_to_final_summary
from my_prompts import file_map, file_combine, file_combine_long
from streamlit_app_utils import check_gpt_4, check_key_validity, create_temp_file, create_chat_model, token_limit, token_minimum
import markdown as md

#st.set_page_config(layout="wide")


def main():
    """
    The main function for the Streamlit app.

    :return: None.
    """
    st.logo('ecb-logo_RGB_SymbolOnly.png',link = '', icon_image = 'ecb-logo_RGB_SymbolOnly.png')
    st.html("""
        <style>
        [alt=Logo] {
            height: 4rem;
                }
        </style>
            """)
    
    
    
    st.title("Hermes - A Document Summariser")
    st.write("Powered by SupTech")
    #st.divider()
    api_key = st.secrets['openai_key']
    use_gpt_4 = False #st.checkbox("Use GPT-4 for the final prompt (STRONGLY recommended, requires GPT-4 API access - progress bar will appear to get stuck as GPT-4 is slow)", value=True)
    #find_clusters = st.sidebar.checkbox('Find optimal clusters (experimental, could save on token usage)', value=False)
    find_clusters = False
    
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True

    
    uploaded_file = st.file_uploader("Upload a document to summarize:", type=['txt', 'pdf'])
    st.button('Summarize', on_click=click_button)

    if st.session_state.clicked:
        process_summarize_button(uploaded_file, api_key, use_gpt_4, find_clusters)


def process_summarize_button(file_or_transcript, api_key, use_gpt_4, find_clusters, file=True, lenght='default'):
    """
    Processes the summarize button, and displays the summary if input and doc size are valid

    :param file_or_transcript: The file uploaded by the user

    :param api_key: The API key entered by the user

    :param use_gpt_4: Whether to use GPT-4 or not

    :param find_clusters: Whether to find optimal clusters or not, experimental

    :return: None
    """
    if not validate_input(file_or_transcript, api_key, use_gpt_4):
        return

    with st.spinner("Summarizing... please wait..."):
        if file:
            temp_file_path = create_temp_file(file_or_transcript)
            doc = doc_loader(temp_file_path)
            map_prompt = file_map
            combine_prompt = file_combine_long
        
        llm = create_chat_model(api_key, use_gpt_4)
        initial_prompt_list = summary_prompt_creator(map_prompt, 'text', llm)
        final_prompt_list = summary_prompt_creator(combine_prompt, 'text', llm)

        if not validate_doc_size(doc):
            if file:
                os.unlink(temp_file_path)
            return

        
        summary = doc_to_final_summary(doc, 10, initial_prompt_list, final_prompt_list, api_key, use_gpt_4)
        st.header("Keypoints and Summary for " + str(file_or_transcript.name))

        #color_summary = ''':gray-background[%s]''' %summary
        st.markdown(summary, unsafe_allow_html=True)


        mail = mt.Mail(
                    sender=mt.Address(email="mailtrap@demomailtrap.com", name="LLM Newsletter Agent"),
                    to=[mt.Address(email="ai.research.agent@gmail.com")],
                    subject="Keypoints and Summary for " + str(file_or_transcript.name),
                    html = md.markdown(summary)
                    )   
        # create client and send
        client = mt.MailtrapClient(token = st.secrets['maildrop'])
        client.send(mail)
        #st.code(summary,language='html')
        if file:
            os.unlink(temp_file_path)


def validate_doc_size(doc):
    """
    Validates the size of the document

    :param doc: doc to validate

    :return: True if the doc is valid, False otherwise
    """
    if not token_limit(doc, 800000):
        st.warning('File or transcript too big!')
        return False

    if not token_minimum(doc, 0):
        st.warning('File or transcript too small!')
        return False
    return True


def validate_input(file_or_transcript, api_key, use_gpt_4):
    """
    Validates the user input, and displays warnings if the input is invalid

    :param file_or_transcript: The file uploaded by the user or the YouTube URL entered by the user

    :param api_key: The API key entered by the user

    :param use_gpt_4: Whether the user wants to use GPT-4

    :return: True if the input is valid, False otherwise
    """
    if file_or_transcript == None:
        st.warning("Please upload a file.")
        return False

    if not check_key_validity(api_key):
        st.warning('Key not valid or API is down.')
        return False

    if use_gpt_4 and not check_gpt_4(api_key):
        st.warning('Key not valid for GPT-4.')
        return False

    return True


if __name__ == '__main__':
    main()

