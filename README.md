# Learning
## About python development
1. Think about what functions we need.
    e.g. Voice Assitant requires
        1. Ask question
        2. Answer question
        3. Voice out
2. Search if there are useful API in Python libraries.
    e.g. 
        1. Ask question -> GUI Library
        2. Answer question -> Wiki API or wolframalpha API
        3. Voice out -> pyttsx3
3. Read the doc and think about how to use the library.

# Libraries I used in voice assistant

## wolframalpha API
We can get the answer to a question by simply calling this API with input of a question.
- API doc: https://pypi.org/project/wolframalpha/
- Please take the key from https://developer.wolframalpha.com/access

## wikipedia API
We can get the answer to a question by simply calling this API with input of a question.
- API doc: https://pypi.org/project/wikipedia/

## PySimpleGUI API
We can let the users input the questions by this GUI.
- API doc: https://www.pysimplegui.org/en/latest/

## Text to speech Voice API, pyttsx3
We can make text into voice, speaking by PC.
- API doc: https://pypi.org/project/pyttsx3/
- Error to fix: https://stackoverflow.com/a/77338405