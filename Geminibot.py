import google.generativeai as genai

genai.configure(api_key="AIzaSyBfqyO36oDFHxbPMyCZbP1uUgy-l-R4_4Q")  

model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

chat = model.start_chat()

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    try:
        response = chat.send_message(user_input)
        print("ChatBot:", response.text)
    except Exception as e:
        print("ChatBot: An error occurred:", e)
