import wolframalpha
import PySimpleGUI as sg
import wikipedia
import pyttsx3
# The key has been depcrepted.
api_id = "48YVQ9-4R6TWQ3V2V"

client = wolframalpha.Client(api_id)

sg.theme('DarkAmber')
layout = [  [sg.Text('Enter your question'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('ChunHao Assistant', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    question = values[0]
    engine = pyttsx3.init()
    try:
        wiki_res = wikipedia.summary(question, sentences=1)
        engine.say(f"answer from wikipeidia, {wiki_res}")
        sg.PopupNonBlocking(wiki_res)
    except:
        try:
            res = client.query(question)
            wol_res = next(res.results).text
            engine.say(f"answer from wolfram, {wol_res}")
            sg.PopupNonBlocking(wol_res)
        except:
            error_handling = "There is no answer from wolfram and wiki"
            engine.say(error_handling)
            sg.PopupNonBlocking(error_handling)
    engine.runAndWait()

window.close()