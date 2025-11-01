# Pseudocode-To-Python

A GPT-2 fine-tuned model that converts pseudocode to code. This project includes a Streamlit web application for easy interaction.

## 🚀 Quick Start

### Running the Streamlit App Locally

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Streamlit app:**
   ```bash
   streamlit run streamlit_app.py
   ```
   
   Or use the alternative entry point:
   ```bash
   streamlit run streamlit.py
   ```

3. **Access the app:**
   - The app will open automatically in your browser
   - Or navigate to `http://localhost:8501`

### Deploying to Streamlit Cloud

1. Push your code to GitHub (already done ✅)
2. Go to [streamlit.io](https://streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository: `mtaha-23/pseudocodetopython`
6. Set the main file path: `streamlit_app.py`
7. Click "Deploy"

**Important:** For Streamlit Cloud, make sure:
- All model files are committed to the repository (model files are in `.gitignore` by default - you may need to upload large model files to a cloud storage and load them, or use Git LFS)
- The `requirements.txt` file is present
- Model files should be accessible (consider using HuggingFace Hub or similar for large files)

## 📁 Project Structure

- `streamlit_app.py` - Main Streamlit application with full UI
- `streamlit.py` - Simplified Streamlit app alternative
- `a3_t2_Final.ipynb` - Training notebook
- Model files: `config.json`, `tokenizer_config.json`, `model.safetensors`, etc.

## 💡 Usage Example

Enter pseudocode like:
```
create integer variable x
read input from user
print x
```

The model will generate the corresponding code.

## 📝 Notes

- The model was fine-tuned on the SPOC dataset
- Model: GPT-2 Medium (355M parameters)
- Training was done on Google Colab
