from gtts import gTTS
import ollama
import sys
import json



#######################
#######################
# Uses LLM to analyze given url as a string.
# Returns response as a string.
def run_llm(url: str, input_model: str) -> str:
    print('Analyzing article...')

    prompt = f'Summarize this article and make it straight to the point. {url}'

    response = ollama.chat(model=input_model, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    return response['message']['content']



#######################
#######################
# Uses gTTS to create mp3 from the text.
# It also saves it so it can be used as an endpoint.
def create_audio(text: str):
    print('Creating speech...')
    tts = gTTS(text=text, lang='en')
    filename = "wrap_n_yap_output.mp3"
    tts.save(f"wrap_n_yap\\{filename}")



#######################
#######################
# Uses the LLM to analyze the URL.
# Creates and saves audio file of the summarization.
# Returns the summarized text as JSON.
def main(url: str, input_model: str):
    response = run_llm(url, input_model)
    response = response.strip()
    create_audio(response)
    return json.dumps({"text":response})



#######################
#######################
#######################
if __name__ == "__main__":
    input_model = "qwen2:1.5b"
    url = sys.argv[1]
    main(url, input_model)
    