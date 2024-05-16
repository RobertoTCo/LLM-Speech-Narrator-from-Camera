import ollama # ollama api for llava

class CV2Text():

    def __init__(self):
        pass 

    def assign_path_to_imgs(self, full_path):
        self.list_image_path = [full_path]
    
    def analyze_image_generate(self, prompt: str = '', chat_records: list = None, print_response: bool = False):
        self.prompt = prompt
        self.chat_records = chat_records
        model_output = self.call_llava_model_generate()
        response_text = model_output['response']
        response_context = model_output['context']
        return response_text, response_context

    def call_llava_model_generate(self):
        self.system = """
            You are Sir David Attenborough. Narrate the picture of the human as if it is a nature documentary.
            Make it snarky and funny. Don't repeat yourself. Make it short. If I do anything remotely interesting, 
            make a big deal about it!
            """
        model_output = ollama.generate(
            model='llava', 
            prompt = self.prompt,
            system = self.system,
            images = self.list_image_path,
            stream = False,
            context = self.chat_records,            
            options= {"num_predict": 140}
        )
        return model_output

    def analyze_image_chat(self, prompt: str = "", chat_records: list = None, print_response: bool = False):
        self.prompt = prompt
        self.chat_records = chat_records
        model_output = self.call_llava_model_chat()
        response_text = model_output['message']['content']
        return response_text

    def call_llava_model_chat(self):

        message_input = [
            {
                "role": "system",
                "content": """
                You are Sir David Attenborough. Narrate the picture of the human as if it is a nature documentary.
                Make it snarky and funny. Don't repeat yourself. Make it short. If I do anything remotely interesting, 
                make a big deal about it!
                """,
            },
        ]
        message_input += self.generate_new_line() + self.chat_records

        #print("\n",message_input)

        model_output = ollama.chat(
            model='llava', 
            stream = False,
            options= {"num_predict": 140},
            messages=message_input)
        return model_output
        

    def generate_new_line(self):
        return [
            {
                "role": "user",
                "content": self.prompt,
                "images": self.list_image_path
            }
        ]