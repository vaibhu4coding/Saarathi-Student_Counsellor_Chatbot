import openai
import gradio
openai.api_key = "GPT_API_KEY"

messages = [{"role": "system", 
             "content": "You are a student counselor that plays a vital role in helping students navigate the challenges they face during their academic journey"
             }]

def Saarathi(Student_Query):
    messages.append({"role": "user", "content": Student_Query})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    guidance = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": guidance})
    return guidance

SaarathiGUI = gradio.Interface(fn=Saarathi, 
                               inputs = gradio.Textbox(label="Student"), 
                               outputs = gradio.Textbox(label="Counselor"), 
                               title = "Saarathi:Guiding you towards success")

SaarathiGUI.launch()