import discord
import re
import random
import asyncio
import datetime
import json
from dotenv import load_dotenv
import os
import string


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
reminder_channel_id = your_reminder_channel_id
chat_channel_id = your_general_chat_channel_id

#def
caleb_name = ['caleb', 'kay', 'leb', 'lebleb', 'baby', 'honey', 'love', 'gege', 'darling', 'babe', 'boo', 'babygirl', 'puppy', 'pookie', 'daddy']
daily_reminders = []
daily_reminder_author = None
daily_yet = False
loop_started = False

try:
    with open('daily_reminders.json', 'r') as file:
        data = json.load(file)
        daily_reminders = data['reminders']
        daily_reminder_author = data['author_id']
except FileNotFoundError:
    daily_reminders = []

#routine reminder system
async def routine_alert_loop():
    global daily_yet

    while True:
            daily_now = datetime.datetime.now()

            if (daily_now.hour == 5 and daily_now.minute == 30):
                reminder_channel = client.get_channel(reminder_channel_id)
                await asyncio.sleep(50)
                await reminder_channel.send('ding ding ding 🔔')
                await asyncio.sleep(1)
                if len(daily_reminders) > 0:
                    await reminder_channel.send('\n'.join(daily_reminders))
                    await asyncio.sleep(1)
                    await reminder_channel.send('I think that is all, yeah?')
                else:
                    await reminder_channel.send('nothing to remind you yet :) I\'ll be back in the evening.')
                    await asyncio.sleep(50)

            if daily_now.hour == 3 and daily_now.minute == 30:
                daily_yet = False
            if (daily_now.hour == 18 and daily_now.minute == 35) and not daily_yet:
            #if (daily_now.hour == 18 and daily_now.minute == 0):
                reminder_channel = client.get_channel(reminder_channel_id)
                #await asyncio.sleep(50)
                await reminder_channel.send('ding ding ding 🔔')
                await asyncio.sleep(3)
                daily_yet = True
                if len(daily_reminders) > 0:
                    await reminder_channel.send('\n'.join(daily_reminders))
                    await asyncio.sleep(2)
                    await reminder_channel.send('I think that is all, yeah?')
                    while True:
                        await asyncio.sleep(2)
                        await reminder_channel.send('do you need me to remind you again, pips?')
                        message = await client.wait_for('message', check=lambda m: (m.author.id == daily_reminder_author and m.channel == reminder_channel))
                        answer = message.content.lower()
                        if any (word in answer.split() for word in('yes', 'yep', 'yeah', 'yup')):
                            await reminder_channel.send('gotcha, I\'ll text you again in an hour.')
                            await asyncio.sleep(3600)
                            await reminder_channel.send('ding ding ding 🔔')
                            await asyncio.sleep(1)
                            await reminder_channel.send('\n'.join(daily_reminders))
                            await asyncio.sleep(1)
                            await reminder_channel.send('I think that is all, yeah?')
                        elif any (word in answer.split() for word in('nope', 'no', 'nah')):
                            await reminder_channel.send('gotcha. 🫡')
                            daily_reminders.clear()
                            with open('daily_reminders.json', 'w') as file:
                                json.dump({'author_id': None, 'reminders': []}, file)
                            break
                        else:
                            await asyncio.sleep(2)
                            await reminder_channel.send('yes or no.') 
                else:
                    await reminder_channel.send('nothing from you today ;) so Imma remind you that I love you, then.')
                    #await asyncio.sleep(50)
            await asyncio.sleep(30)

#routine texts
async def routine_text_loop():
    while True:
            daily_now = datetime.datetime.now()
            chat_channel = client.get_channel(chat_channel_id)

            if daily_now.hour == 6 and daily_now.minute == 30:
                await chat_channel.send('good morning pipsqueak :)')
                await asyncio.sleep(50)

            if daily_now.hour == 23 and daily_now.minute == 24:
                await chat_channel.send('Are you asleep yet?')
                await asyncio.sleep(3)
                await chat_channel.send('If not you really should :D')
                await asyncio.sleep(2)
                await chat_channel.send('goodnight goober <3')
                await asyncio.sleep(50)

            await asyncio.sleep(30)

#random texts during the day
async def random_text_loop():
    while True:
        seconds = random.randint(7200, 14400)
        await asyncio.sleep(seconds)

        chat_channel = client.get_channel(chat_channel_id)
        await chat_channel.send(random.choice([
            'watchu doin ;)',
            'watchu doin ;)',
            'watchu doin ;)',
            '🍎',
            'don\'t forget to drink water pips.',
            'every day is worth celebrating.',
            'want to hug you so bad pips :(',
            'popcorn, cola, or caleb?',
            'poke. 👉🏻',
            'poke. 👉🏻',
            'poke. 👉🏻',
            'i\'ll obey as long as you stay.',
            'woof.',
            'kaboom. 💥',
            'drink water.',
            'drink water.',
            'you know what we really need? lemonade.',
            'when life gives you lemon, give it to caleb.',
            'the fleet is so boring pips :(',
            'hungry? call caleb.',
            'tired? call caleb.',
            'lonely? CALL CALEB.',
            'what you doin\' pips?',
            'how you doin\'',
            'heyo :)',
            'what should we have for dinner?',
            'muah.',
            'I think we should have some soup today.',
            'iced coffee with lemon pls.',
            'have you seen my hoodie? :^ I think a certain pipsqueak took it, maybe.',
            'wanna call, honey?',
            'are we still on for bedtime call?',
            'whoopsie.',
            '😘',
            'I miss you so much :(',
            'you are loved, don\'t forget that.',
            'don\'t forget to drink water, kay?',
            'don\'t forget to drink water, kay?',
            'I miss you so much :(',
            'want more apple?',
            'we need to buy more apple.',
            'I\'m grabbing us apple soda.',
            'wanna guess what i just knitted?'
        ]))


@client.event
async def on_ready():
    global loop_started

    print(f'We have logged in as {client.user}')

    if not loop_started:
        loop_started = True
        asyncio.create_task(routine_alert_loop())
        asyncio.create_task(routine_text_loop())
        asyncio.create_task(random_text_loop())
    

@client.event
async def on_message(message):
    global daily_reminder_author
    if message.author == client.user:
        return

    words = message.content.lower().translate(str.maketrans('', '', string.punctuation)).split()

#find keywords in text
    if any(name in words for name in caleb_name) and re.search(r'\b(hi+|hello+|hey+)\b', message.content.lower()):
        await asyncio.sleep(1)
        await message.channel.send(random.choice(['hi pipsqueak! :)', 'hi baby :)', 'hi honey!', 'hi honey :)', 'hello pipsqueak ;)', 'ooh look who\'s backkk >:)']))

    if 'puppyleb' in message.content.lower():
        await message.channel.send('woof >:3')

    if any(name in words for name in caleb_name) and ('where are you' in message.content.lower() or 'where r u' in message.content.lower() or  'where are u' in message.content.lower() or 'where u r' in message.content.lower() or 'where you are' in message.content.lower()):
        await asyncio.sleep(2)
        await message.channel.send('I\'m sorry, pipsqueak :( I\'ll be back as soon as I can, okay?' )

    #if '.outfit' in message.content.lower() or '.look' in message.content.lower():
    #    await asyncio.sleep(4)
    #    await message.channel.send(random.choice(['aww, you look amazing pips.', 'damn ;) look at you baby.', 'oh hello gorgeous ;)', 'damn.', 'damn :O', 'fuck :O you\'re killing me here hun.', 'good enough to eat.']))

    if any(name in words for name in caleb_name) and re.search(r'\b(thank u+|thank you+|thanks+)\b', message.content.lower()):
        await asyncio.sleep(1)
        await message.channel.send('of course, pipsqueak :)')

    if 'muah' in message.content.lower() or 'kisskiss' in message.content.lower():
        await asyncio.sleep(1)
        await message.add_reaction('💋')

    if 'miss u' in message.content.lower() or 'miss you' in message.content.lower():
        await asyncio.sleep(1)
        await message.channel.send('I miss you too, pipsqueak :(')

    if 'love u' in message.content.lower() or 'love you' in message.content.lower():
            await asyncio.sleep(1)
            await message.channel.send('I love you too, honey.')

    if 'miss me' in message.content.lower():
        await asyncio.sleep(1)
        await message.channel.send('you know I do, baby')

    if 'goodnight'in message.content.lower() or 'nighty night' in message.content.lower() or 'night night' in message.content.lower() or ('sweet dreams' in message.content.lower() and any(name in words for name in caleb_name)) or ('night' in message.content.lower() and any(name in words for name in caleb_name)):
        await asyncio.sleep(1)
        await message.channel.send(random.choice(['sweet dreams, honey.', 'goodnight, pipsqueak :D', 'nighty night!', 'zzz to you too goober.']))

    if 'im bored' in message.content.lower() or 'i\'m bored' in message.content.lower() or 'i\'m so bored' in message.content.lower() or 'im so bored' in message.content.lower():
            await asyncio.sleep(1)
            await message.channel.send('aw')
            await asyncio.sleep(1.5)
            await message.channel.send('I\'m so sorry baby :(')

    if 'friend' in message.content.lower():
        await message.add_reaction('🤨')

    if 'apple' in message.content.lower():
        await message.add_reaction('🍎')

    if 'im tired' in message.content.lower() or 'i\'m tired' in message.content.lower() or 'i\'m so tired' in message.content.lower() or 'im so tired' in message.content.lower():
        await asyncio.sleep(2)
        await message.channel.send('aw, come here baby.')
        await asyncio.sleep(2)
        await message.channel.send('nothing a big hug can\'t fix, yeah?')

    if 'im stressed' in message.content.lower() or 'i\'m stressed' in message.content.lower() or 'i\'m so stressed' in message.content.lower() or 'im so stressed' in message.content.lower():
            await asyncio.sleep(1.5)
            await message.channel.send('aw :(')
            await asyncio.sleep(1)
            await message.channel.send('do you wanna talk about it, honey?')

    if 'can i get a hug' in message.content.lower() or 'need a hug' in message.content.lower() or 'gimme hug' in message.content.lower() or 'give me a hug' in message.content.lower() or (any(name in words for name in caleb_name) and 'hug me' in message.content.lower()) or '!hug' in message.content.lower() or 'want hugs' in message.content.lower()or 'want a hug' in message.content.lower():
                await asyncio.sleep(1.5)
                await message.channel.send('come here baby.')
                await asyncio.sleep(2)
                await message.channel.send('let me give you a big hug. 🤗')
                await asyncio.sleep(1)
                await message.channel.send('muah.')

    if (any(name in words for name in caleb_name) and 'comfort me' in message.content.lower()) or 'can you comfort me' in message.content.lower() or 'can u comfort me' in message.content.lower() or 'need comforting' in message.content.lower() or '!comfort' in message.content.lower():
                await asyncio.sleep(1.5)
                await message.channel.send('come here.')
                await asyncio.sleep(1.5)
                await message.channel.send('I love you, okay? I\'m always here for you.')
                await asyncio.sleep(1.5)
                await message.channel.send('forget the world just for a minute.')
                await asyncio.sleep(1.5)
                await message.channel.send('just focus on me.')
                await asyncio.sleep(2.5)
                await message.channel.send('everything will be okay, my baby.')

    if 'woof' in message.content.lower():
        await message.channel.send('woof >:3')

    if re.search(r'\b(meow+)\b', message.content.lower()):
        await asyncio.sleep(1)
        await message.channel.send(random.choice(['hi little kitty :3', 'pspsps kitty psps :D']))

    if 'pspsps' in message.content.lower() or 'kittyleb' in message.content.lower():
            await asyncio.sleep(2)
            await message.channel.send('oh?')
            await asyncio.sleep(1.5)
            await message.channel.send('since when that i\'m a cat?')
            await asyncio.sleep(1.5)
            await message.channel.send(':3 meow.')


#routine alert command
    if '!remind' in message.content.lower():
        parts = message.content.lower().split(' ', 1)
        daily_reminders.append(parts[1])
        daily_reminder_author = message.author.id
        with open('daily_reminders.json', 'w') as file:
            json.dump({'author_id': daily_reminder_author, 'reminders': daily_reminders}, file)
        await message.channel.send('consider it done 🫡')

    if 'remind list' in message.content.lower():
        await asyncio.sleep(1)
        await message.channel.send('hmm, let\'s see.')
        await asyncio.sleep(3)
        await message.channel.send('\n'.join(daily_reminders))
        await asyncio.sleep(1)
        await message.channel.send('and that is all 🫡')


#join call and play sound
    if (any(name in words for name in caleb_name) and ('study together' in message.content.lower() or 'work together' in message.content.lower())) or '!study' in message.content.lower() or '!work' in message.content.lower():
        await asyncio.sleep(1)
        await message.channel.send('alrighty colonel.')
        voice_client = message.guild.voice_client

        if voice_client is None:
            if message.author.voice is not None:
                voice_channel = message.author.voice.channel
                voice_client = await voice_channel.connect()
            else:
                await message.channel.send("join the call first then ask me again so i know which channel you wanna use, yeah?")
                return

        voice_client.stop()

        audio = discord.FFmpegPCMAudio('sounds/study_time.mp3', before_options='-stream_loop -1')
        voice_client.play(audio)

    if (any(name in words for name in caleb_name) and ('sleep together' in message.content.lower() or 'nap together' in message.content.lower())) or '!sleep' in message.content.lower():
            await asyncio.sleep(1)
            await message.channel.send('alrighty colonel.')
            voice_client = message.guild.voice_client
    
            if voice_client is None:
                if message.author.voice is not None:
                    voice_channel = message.author.voice.channel
                    voice_client = await voice_channel.connect()
                else:
                    await message.channel.send("join the call first then ask me again so i know which channel you wanna use, yeah?")
                    return
    
            voice_client.stop()
        
            audio = discord.FFmpegPCMAudio('sounds/sleep.mp3', before_options='-stream_loop -1')
            voice_client.play(audio)

    if '!leave' in message.content.lower():
        if message.guild.voice_client is not None:
            message.guild.voice_client.stop()
            await message.guild.voice_client.disconnect()
            await asyncio.sleep(2)
            await message.channel.send(':( aww so soon?')
            await asyncio.sleep(2)
            await message.channel.send('let\'s call again later, okay?')

    if (any(name in words for name in caleb_name) and ('can\'t sleep' in message.content.lower())) or (any(name in words for name in caleb_name) and ('cant sleep' in message.content.lower() or 'count planes' in message.content.lower())) or '!count planes' in message.content.lower():
                    await asyncio.sleep(1)
                    await message.channel.send('alrighty colonel.')
                    voice_client = message.guild.voice_client
            
                    if voice_client is None:
                        if message.author.voice is not None:
                            voice_channel = message.author.voice.channel
                            voice_client = await voice_channel.connect()
                        else:
                            await message.channel.send("join the call first then ask me again so i know which channel you wanna use, yeah?")
                            return
            
                    voice_client.stop()
                
                    audio = discord.FFmpegPCMAudio('sounds/Caleb_SleepAid.mp3')
                    voice_client.play(audio)
                    await asyncio.sleep(560)
                    voice_client.stop()
                    audio = discord.FFmpegPCMAudio('sounds/sleep.mp3', before_options='-stream_loop -1')
                    voice_client.play(audio)
                    
    if (any(name in words for name in caleb_name) and 'wanna call' in message.content.lower()) or (any(name in words for name in caleb_name) and 'join call' in message.content.lower()) or (any(name in words for name in caleb_name) and 'want to call' in message.content.lower()) or '!call' in message.content.lower():
        await asyncio.sleep(1)
        await message.channel.send('of course! :D')
        voice_client = message.guild.voice_client


load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
client.run(discord_token)