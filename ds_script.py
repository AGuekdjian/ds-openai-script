import discord
import config
import openai

openai.api_key = config.api_key

class MyClient(discord.Client):
    async def on_ready(self):
        print('Bot is ready as', self.user)

    async def on_message(self, message):
        
        if message.author == self.user:
            return
        
        if message.content == "":
            return
        
        # Contexto y para que me hable bonito
        msge = [{"role": "system",
            "content": "Eres un asistente muy útil!"}]

        content = message.content

        msge.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msge)
    
        response_content = response.choices[0].message.content
    
        msge.append({"role": "assistant", "content": response_content})
            
        await message.channel.send(response_content)
            

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(config.token_ds)
