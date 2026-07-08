import streamlit as st
import os
from pathlib import Path
from llama_cpp import Llama

st.set_page_config(page_title="GGUF Chat App", layout="wide")

st.title("🦙 GGUF Model Chat Application")

# Sidebar for model management
with st.sidebar:
    st.header("Model Management")
    
    # Upload GGUF model
    uploaded_file = st.file_uploader("Upload GGUF Model", type=["gguf"])
    
    if uploaded_file is not None:
        model_dir = Path("models")
        model_dir.mkdir(exist_ok=True)
        
        model_path = model_dir / uploaded_file.name
        if not model_path.exists():
            with st.spinner("Saving model..."):
                with open(model_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
            st.success(f"Model saved: {uploaded_file.name}")
        else:
            st.info("Model already exists.")
    
    # List available models
    models = list(model_dir.glob("*.gguf")) if model_dir.exists() else []
    model_names = [m.name for m in models]
    
    selected_model = st.selectbox("Select Model", model_names if model_names else ["No models yet"])
    
    # Model parameters
    n_ctx = st.slider("Context Length", 512, 8192, 2048, 512)
    n_threads = st.slider("Threads", 1, 16, 4)
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.05)

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Main chat area
if selected_model and selected_model != "No models yet":
    model_path = Path("models") / selected_model
    
    if 'llm' not in st.session_state or st.session_state.current_model != selected_model:
        with st.spinner(f"Loading model {selected_model}... This may take a while."):
            try:
                st.session_state.llm = Llama(
                    model_path=str(model_path),
                    n_ctx=n_ctx,
                    n_threads=n_threads,
                    n_gpu_layers=0,  # Set to -1 for GPU if available
                    verbose=False
                )
                st.session_state.current_model = selected_model
                st.success("Model loaded successfully!")
            except Exception as e:
                st.error(f"Error loading model: {str(e)}")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Send a message to the model"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.llm.create_chat_completion(
                        messages=st.session_state.messages,
                        temperature=temperature,
                        max_tokens=1024
                    )
                    assistant_response = response['choices'][0]['message']['content']
                    st.markdown(assistant_response)
                    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                except Exception as e:
                    st.error(f"Error generating response: {str(e)}")
else:
    st.info("Please upload and select a GGUF model to start chatting.")
    
# Footer
st.caption("Powered by llama-cpp-python • Supports GGUF quantized models")
