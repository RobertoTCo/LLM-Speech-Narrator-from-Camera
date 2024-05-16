import os
import torch
import time
import simpleaudio
from CV2Text_llava_class import CV2Text
from TTS.api import TTS

def main():
    chat_records = []
    count=0
    while count<5:
        full_path_to_image = r"C:\Users\rober\Documents\Python Scripts\LLM Speech Narrator from Camera\frames\frame.jpg"
        audio_sample = "audio samples/David_assets_wonderful_posture.wav"
        audio_export_name = "output.wav"
        processing_device = check_device_cpu_or_gpu()

        prompt = "Describe this image. Do not repeat the previous context by the assistant! Add something new!"
        #llava_response, llava_context = apply_llava_narrator(full_path, prompt=prompt, chat_records=chat_records, print_response = True)
        llava_response = apply_llava_narrator(full_path_to_image, prompt=prompt, chat_records=chat_records, print_response = True)
        #play_audio_with_xtts_v2(llava_response['content'], audio_sample, processing_device, audio_export_name)        

        #chat_records = chat_records + [{"role": "assistant", "content": llava_response}]
        chat_records = [{"role": "assistant", "content": llava_response}]
        
        #time.sleep(5)
        count+=1
        print("loop ",count)

def check_device_cpu_or_gpu():
    if torch.cuda.is_available():
        processing_device = "cuda"
        print("You are using {} GPU".format(torch.cuda.get_device_name()))
    else:
        processing_device = "cpu"
        print("Warning! You are using CPU to clone the AI voice")
    return processing_device

def apply_llava_narrator(full_path, prompt: str = '', chat_records: list = None, print_response: bool = False):
    LlaVa_narrator = CV2Text()
    LlaVa_narrator.assign_path_to_imgs(full_path)
    print("👀 David is watching...")
    #llava_text, llava_context = LlaVa_narrator.analyze_image_generate(prompt=prompt, chat_records=chat_records)
    llava_response = LlaVa_narrator.analyze_image_chat(prompt = prompt, chat_records=chat_records)

    if print_response:
        print("🎙️ David says:\n")
        print(llava_response) 
    return llava_response

def play_audio_with_xtts_v2(text, audio_sample,  processing_device: str="cpu", audio_export_name: str = "output.wav"):
    folder_output = "output_sound"
    speech_model = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(processing_device)
    os.makedirs(folder_output, exist_ok=True) # exist_ok already handles if path exists
    speech_model.tts_to_file(text=text, speaker_wav=audio_sample, language="en", file_path= folder_output+"/"+audio_export_name)
    play_audio(audio_export_name)

def play_audio(audio_file):
    wave_obj = simpleaudio.WaveObject.from_wave_file(audio_file)
    play_obj = wave_obj.play()
    play_obj.wait_done()

if __name__ == "__main__":
    main()
