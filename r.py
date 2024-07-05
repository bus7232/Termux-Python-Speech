import os
import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot instance
chatbot = ChatBot("Chatpot")

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Initialize the TTS engine
engine = pyttsx3.init()

# Function to convert text to speech with speed and pitch control
def speak(text, speed=1.0, pitch=1.0):
    engine.setProperty('rate', int(engine.getProperty('rate') * speed))
    engine.setProperty('pitch', pitch)
    engine.say(text)
    engine.runAndWait()

# Your conversations list remains the same
conversations = [
['ระวังโดนรุมนะ!', ['ไม่กลัวหรอก']],
['ไปรวมกันเร็ว!', ['มาแล้วๆ']],
['พร้อมลุยยัง?', ['เกิดมาเพื่อสิ่งนี้']],
['บวกเลยดิ!', ['รอไรอะ']],
['จะเอาป้อมนี้!', ['จัดไปอย่าให้เสีย']],
['ถอยก่อน!', ['โอเคๆ']],
['รวมกันก่อน!', ['กำลังไป']],
['ได้เปรียบแล้ว!', ['อย่าประมาท']],
['ดีใจด้วย!', ['ขอบคุณนะ']],
['สู้ๆ นะ!', ['ไม่ยอมแพ้หรอก']]
]

# Train the chatbot with the input-output pairs
for input_text, output_texts in conversations:
    for output_text in output_texts:
        trainer.train([input_text, output_text])

# Main loop to interact with the chatbot
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        # Get response from the chatbot
        response = chatbot.get_response(query)
        print(f"Chatpot: {response}")

        # Convert response to speech with adjustable speed and pitch
        speak(str(response), speed=1.2, pitch=1.1)