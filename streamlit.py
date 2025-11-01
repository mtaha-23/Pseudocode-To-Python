"""
Simplified Streamlit App for Pseudocode to Code Converter
==========================================================
Alternative entry point for the Streamlit app.
This file can be used if streamlit_app.py doesn't work.
"""

import streamlit as st
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Page config
st.set_page_config(
    page_title="Pseudocode Converter",
    page_icon="💻",
    layout="centered"
)

@st.cache_resource
def load_model():
    """Load model and tokenizer"""
    try:
        tokenizer = GPT2Tokenizer.from_pretrained(".")
        model = GPT2LMHeadModel.from_pretrained(".")
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model.to(device)
        model.eval()
        return tokenizer, model, device
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None, None

def generate_code(pseudo_code, tokenizer, model, device):
    """Generate code from pseudocode"""
    prompt = f"### PSEUDOCODE:\n{pseudo_code}\n### PYTHON CODE:\n"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=150,
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.pad_token_id,
        )
    
    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    if "### PYTHON CODE:" in generated:
        code = generated.split("### PYTHON CODE:")[1].strip()
        if "###" in code:
            code = code.split("###")[0].strip()
        return code
    
    return generated

# App
st.title("💻 Pseudocode to Code Converter")

tokenizer, model, device = load_model()

if tokenizer and model:
    pseudo_input = st.text_area("Enter pseudocode:", height=150)
    
    if st.button("Generate Code"):
        if pseudo_input.strip():
            with st.spinner("Generating..."):
                code = generate_code(pseudo_input, tokenizer, model, device)
                st.code(code)
        else:
            st.warning("Please enter pseudocode!")
else:
    st.error("Could not load model. Please check model files.")

