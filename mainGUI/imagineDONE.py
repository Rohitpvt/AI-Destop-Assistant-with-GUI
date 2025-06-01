import asyncio
import requests
import webbrowser
import time
import pyttsx3
global command2
import aiohttp
import threading

replace_list=['garry','gary','imagine','generate','image',' an ', ' of ']


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(updategif, text):
    updategif("speaking")
    engine.say(text)
    engine.runAndWait()


models_list = {'Default': 'v1-5-pruned-emaonly.safetensors [d7049739]',
               'Anime': 'EimisAnimeDiffusion_V1.ckpt [4f828a15]',
               'Animated': 'revAnimated_v122.safetensors [3f4fefd9]',
               'Cartoon': 'toonyou_beta6.safetensors [980f6b15]',
               'Cyberpunk': 'shoninsBeautiful_v10.safetensors [25d8c546]',
               'Photography': 'ICantBelieveItsNotPhotography_seco.safetensors [4e7a3dfd]',
               'Logo': 'dreamshaper_8.safetensors [9d40847d]',
               'Realistic': 'absolutereality_v181.safetensors [3d9d4d2b]',
               'Nature': 'epicrealism_naturalSinRC1VAE.safetensors [90a4c676]',
               'Anything': 'anythingV5_PrtRE.safetensors [893e49b9]'}





def imagine(terminalPrint, command, modelin, updategif, current_task):
    global command2
    command2 = command
    for i in replace_list:
       command2 = command2.replace(i,'')

    terminalPrint(f"Your Prompt: {command2}")
    speak(updategif, f"Your Prompt:{command2}")
    url = 'https://api.prodia.com/generate'
    headers = {
        'Accept': '*/*',
        'Origin': 'https://app.prodia.com',
        'Referer': 'https://app.prodia.com/',
    }
    #

    terminalPrint("")
    terminalPrint("Models List: \n")
    for i in models_list.keys():
        terminalPrint(i)

    terminalPrint("")

    modelin(current_task)
    #model_input = onenter()

    #goes to main file for asking input and when enter pressed
    #create a new function when enter pressed to come in this file and do further process


    # while True:
    #     #terminalPrint("Type any ONE model name from the list: ")
    #
    #     #terminalPrint("Type any ONE model name from the list: ")
    #     model_input = input("Type any ONE model name from the list: ").capitalize()
    #     #model_input = inputText("Type any ONE model name from the list: ")
    #     #terminalPrint("Type any ONE model name from the list: ")
    #     #model_input = get_model(text=None,enterpress)
    #     if model_input in models_list.keys():
    #         modelname = models_list[model_input]
    #         break
    #     else:
    #         terminalPrint("Choose from the list and try again!")
    #         speak("Choose from the list and try again!")
    #         modelin()

def generate(ui, model_input):
    global command2
    modelname = models_list[model_input]
    url = 'https://api.prodia.com/generate'
    headers = {
        'Accept': '*/*',
        'Origin': 'https://app.prodia.com',
        'Referer': 'https://app.prodia.com/',
    }
    data = {
        "new": "true",
        "prompt": command2,
        "model": modelname,
        "negative_prompt": "verybadimagenegative_v1.3, ng_deepnegative_v1_75t, (ugly face:0.8),cross-eyed,sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy, DeepNegative, facing away, tilted head, {Multiple people}, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worstquality, low quality, normal quality, jpegartifacts, signature, watermark, username, blurry, bad feet, cropped, poorly drawn hands, poorly drawn face, mutation, deformed, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, extra fingers, fewer digits, extra limbs, extra arms,extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed,mutated hands, polar lowres, bad body, bad proportions, gross proportions, text, error, missing fingers, missing arms, missing legs, extra digit, extra arms, extra leg, extra foot, repeating hair, [[[[[bad-artist-anime, sketch by bad-artist]]]]], [[[mutation, lowres, bad hands, [text, signature, watermark, username], blurry, monochrome, grayscale, realistic, simple background, limited palette]]], close-up, (cleavage, navel, cleavage cutout), (forehead jewel:1.2), (forehead mark:1.5), (bad and mutated hands:1.3), (worst quality:2.0), (low quality:2.0), (blurry:2.0), multiple limbs, bad anatomy, (interlocked fingers:1.2),(interlocked leg:1.2), Ugly Fingers, (extra digit and hands and fingers and legs and arms:1.4), crown braid, (deformed fingers:1.2), (long fingers:1.2)",
        "steps": "25",
        "cfg": "9",
        "seed": "-1",
        "sampler": "DPM++ 2M Karras",
        "aspect_ratio": "square"
    }
    json_data = requests.get(url=url, params=data, headers=headers).json()
    job_id = json_data['job']
    job_url = f'https://api.prodia.com/job/{job_id}'
    ui.terminalPrint(f"\nImage Prompt: {command2}")
    ui.terminalPrint(f"Image Generation Model: {model_input}")
    ui.terminalPrint("\nGenerating your image, Please wait..")
    ui.updateGifs("loading")


    def check_status():
        while True:
            resp = requests.get(job_url).json()
            if resp['status'] == 'succeeded':
                dl_link = f'https://images.prodia.xyz/{job_id}.png?download=0'
                ui.current_task = None
                return webbrowser.open_new_tab(dl_link)

    thread = threading.Thread(target=check_status)
    thread.start()
