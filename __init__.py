import openai
import os

class OpenAINode:
    FUNCTION = "execute"
    CATEGORY = "OpenAI"
    RETURN_TYPES = ("STRING",)
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "system_prompt": ("STRING", {
                    "multiline": True,
                    "default": "Enter system prompt here..."
                }),
                "user_string": ("STRING", {
                    "multiline": True,
                    "default": "Enter user input here..."
                }),
                "seed": ("INT", {
                    "default": -1
                })
            }
        }

    def __init__(self):
        #load key from environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def execute(self, system_prompt, user_string,seed=-1):
        try:
            
            print("DOING CHAT WITH",user_string)
            
            chat_completion = openai.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_string,
                    },
                ],
                model="gpt-3.5-turbo",
            )
            
            output=chat_completion.choices[0].message.content
            
            return (output.strip(),)
        except Exception as e:
            return (f"Error: {str(e)}",)

NODE_CLASS_MAPPINGS = {
    "OpenAINode": OpenAINode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OpenAINode": "OpenAI Query Node"
}
