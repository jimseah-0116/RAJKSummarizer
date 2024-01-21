import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
curr_dir = os.getcwd()

client = OpenAI(api_key=os.getenv("APIKEY"))


# GPT-3 API call
def get_completion(prompt, model="gpt-3.5-turbo"): 
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model,
                                              messages=messages,
                                              temperature=0)
    return response.choices[0].message.content


# Use GPT API
# change max_tokens

def chatGPT(prompt, model="gpt-3.5-turbo", max_tokens=500, stop=None):
    response = client.chat.completions.create(
        model=model,
        messages = [{"role": "user", "content": prompt}],  # Provide the required 'messages' argument,
        max_tokens=max_tokens,
        stop=stop
        )
    return response.choices[0].message.content.strip()


def TeleGPT(df):
    # join all text messages together
    joined_text = []
    for i in range(len(df)):
        if df.iloc[i]["text"] is not None:
            joined_text.append(df.iloc[i]["text"])
    joined_text = " ".join(joined_text)
  
    # Extract relevant text
    q = "Here are the text messages from a telegram channel, summarise the contents in less than 350 words.\n"
    prompt = q + "".join(joined_text)
    print("Prompt Created!")
    print("Computing...")
    return chatGPT(prompt)
