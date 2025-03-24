import os
from llamaapi import LlamaAPI
from openai import OpenAI

#load enviorment variable
client = OpenAI(api_key = os.environ.get('Open_Ai_Key'))

def make_flashcards(topic, num_cards):
        prompt = f"Create {num_cards} flashcards related to the topic: {topic}. Each flashcard should have a question and an answer."

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500, # Controls how long the responses are
            temperature=0.3 # Controls how random the responses are
        )
        return response.choices[0].message.content.strip()

        
        
    
    #prompt = f"create {num_cards} in relation to the following topic : {topic} \n The flash cards should have a qustion and an answer."

    #response = client.chat.completions.create(
       # model="llama3.1-70b",
        #messages = prompt,
        #max_tokens=500,
        #temperature=0.3
    
    
#)

    #flashcards = response['choices'][0]['text'].strip().split('\n\n')
# Get the users inputs 
input_text = input("What topic do you want to study? ")
inpput_num_cards = int(input("How many flashcards do you want to make? "))
#Makes the flashcards
print(make_flashcards(input_text,inpput_num_cards))
    

