import json

from django.conf import settings
from openai import OpenAI


class ChatGPTClient:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def run_prompt(self, prompt, model="gpt-40", max_tokens=150, temperature=0.7):
        res = self.client.completions.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            n=1,
            stream=False,
        )
        return res.choices[0].message.content

    def get_song_summary(self, lyrics):
        prompt = (
            f"Please provide a one-line summary of the song "
            f"with the following lyrics-\n{lyrics}"
        )
        return self.run_prompt(prompt)

    def get_countries(self, lyrics):
        prompt = (
            f"Extract the names of countries mentioned in the "
            f"following song lyrics.\nReturn the result strictly "
            f"in a list format like this: ['India', 'USA'].\n\n"
            f"Lyrics-\n{lyrics}"
        )
        res = self.run_prompt(prompt)
        return json.loads(res)
