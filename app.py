import streamlit as st
import google.generativeai as genai
import os

# Configure the API key
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.warning("GEMINI_API_KEY 환경 변수가 설정되지 않았습니다. .env 파일이나 시스템 환경 변수를 확인해주세요.")

st.set_page_config(page_title="AI 텍스트 던전", page_icon="🗡️", layout="centered")

st.title("🗡️ AI 텍스트 던전")
st.markdown("인공지능과 함께하는 텍스트 어드벤처 게임입니다. 당신의 선택이 이야기를 만들어갑니다.")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
    # System prompt for the Dungeon Master
    system_prompt = """당신은 판타지 세계의 텍스트 던전 마스터(Dungeon Master)입니다. 
플레이어에게 생생하고 흥미진진한 상황을 묘사하고, 항상 플레이어가 선택할 수 있는 행동 2~3가지를 제시해주세요. 
처음에는 플레이어가 깨어난 어두운 던전 입구에서 시작합니다. 항상 한국어로 대답하세요."""
    
    # Initialize the chat session if API key is present
    if api_key:
        model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_prompt)
        st.session_state.chat = model.start_chat(history=[])
        
        # Get the initial story
        response = st.session_state.chat.send_message("게임을 시작합니다. 첫 번째 상황을 묘사해주세요.")
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    else:
        st.session_state.messages.append({"role": "assistant", "content": "던전에 입장하려면 API 키가 필요합니다..."})

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("당신의 행동을 입력하세요... (예: 왼쪽 문으로 간다, 검을 뽑는다)"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate and display assistant response
    if api_key and "chat" in st.session_state:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            response = st.session_state.chat.send_message(prompt)
            message_placeholder.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    else:
        with st.chat_message("assistant"):
            st.markdown("시스템: AI가 응답할 수 없습니다. API 키를 확인해주세요.")
