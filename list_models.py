import google.generativeai as genai

# Replace this with your Gemini API key
genai.configure(api_key="AIzaSyDAsi-jQ2Zz4QXHO-smzsgbfVgIm9RGDuw")

# List all available models
models = genai.list_models()
for model in models:
    print(model.name)
