import google.generativeai as genai

genai.configure(api_key="AIzaSyCg_2OOxs6GSIm1cjDkNmgZbkdIzJC4NNg")

model = genai.GenerativeModel('gemini-pro')


gpa = 4.0
prompt = f"I have a GPA of {gpa}. What are the potential job opportunities for someone with this GPA?"
response = model.generate_content(prompt)

print(response.text)

 
