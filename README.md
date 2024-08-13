# Wrap-n-Yap

![IMG_2116](https://github.com/user-attachments/assets/118985e5-9735-4415-937d-d3d705df1489)

Wrap-n-yap wraps up articles for you, then serves it with a side of sound - an audio summary that'll keep you in the know!


## RUNNING Wrap-n-Yap
- Make sure to have [Ollama](https://ollama.com/) installed.
- Ollama run Llama 3.1
- Pip install ollama and gTTS.
- When the script is completed, wrap_n_yap_output.mp3 file will be created in the same directory.

## HOW IT WORKS
- `wrap_n_yap.py` makes an inference to the LLM using the URL.
- The summarization is then fed into gTTS for audio creation.

## HOW I USE IT
- I use it in my portfolio website as part of the react and flask backend. [Website](http://38.125.229.163:3000/wrap-n-yap)

## KNOWN BUGS
- The LLM used is qwen2 1.5b which works well for summarization, but still takes too long to compute.
- Run time takes 3 to 4 minutes on average due to hardware limitations.
- I've tested the script on my Macbook M2 and it runs in approximately 20 seconds. 

## Requirements
-   [Python](https://www.python.org) \>= 2.7, 3.4
-   [Ollama](https://pypi.org/project/ollama/) \>= 0.31
-   [gTTS](https://pypi.org/project/gTTS/) \>= 2.5.2

### P.S.

Please drop me a note with any feedback you have.

**Joel**
