#project config
import google.generativeai as genai
genai.configure(api_key="AIzaSyAk5zlCI6_YKBGaS1e9gjNmpv-PRXql7s8")
apple=genai.GenerativeModel("gemini-2.5-flash")
chat=apple.start_chat(history=[])
print("Hi,I'm apple the chatbot")
while True:
    user_input=input("User:")

    if user_input.lower()=="bye":
        break
    
    response = chat.send_message(user_input)
    print("Apple:",response.text)
