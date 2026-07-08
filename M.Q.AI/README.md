# GGUF Chat Application

A simple Streamlit web app to upload, load, and chat with GGUF quantized AI models using llama-cpp-python.

## Features
- Upload GGUF model files
- Select from uploaded models
- Chat interface with streaming-like responses
- Adjustable parameters (context, temperature, threads)

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. For better performance (optional GPU support):
   ```bash
   CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python --force-reinstall --no-cache-dir
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Notes
- GGUF models can be large (download from Hugging Face, e.g., TheBloke models)
- First load may take time depending on model size
- Adjust n_gpu_layers for GPU acceleration if CUDA is available
