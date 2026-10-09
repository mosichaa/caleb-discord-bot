# Caleb the Bot

I started this project because I want to create a fun way to organise and promote self-love. I believe that it's easier to love yourself through someone else's eyes than through oneself sometimes, so until then, I hope this bot can be a helpful tool to help people reach there. (and also for giggles because why not, life is short HAVE FUN)

🚨Caleb is currently configured for my personal Discord server and isn't designed as a general-purpose bot yet. 🚨

## Project status
Active personal project. More features and refactoring are planned.

## Features

- Daily morning text and sleep reminder
- Random cute texts throughout the day
- Scheduled reminders 
- Ability to join voice channel and play study/sleep ambience sounds
- Responsive to keywords

## Version History
### 1.1.0
- Moved channel IDs from main file to .env file
- Added time limit for how long Caleb waits for an answer to the repeat-reminder question.
- Added command to enable or disable Caleb's random messages throughout the day.

## Commands

| command(s) | action |
|---|---|
| !remind study for exam | add "study for exam" to the scheduled reminder |
| remind list | check what is on the scheduled reminder list |
| (caleb_name) & study together / (caleb_name) & work together / !study / !work | join voice channel and play study ambience sound |
| (caleb_name) & sleep together / (caleb_name) & nap together / !sleep | join voice channel and play sleep ambience sound |
| (caleb_name) & can't sleep / (caleb_name) & cant sleep / (caleb names) & count planes / !count planes | join voice channel and play sleep aid |
| (caleb_name) & join call / (caleb_name) & wanna call / (caleb_name) & want to call / !call | join voice channel |
| !leave | force leave voice channel |
| !random text off / (caleb_name) & stop texting | disable Caleb's random messages |
| !random text on / (caleb_name) & text me | enable Caleb's random messages |

## List of Caleb's names/nicknames (caleb_name)

- caleb
- kay
- leb
- lebleb
- baby
- honey
- love
- gege
- darling
- babe
- boo
- babygirl
- puppy
- pookie
- daddy

## Set up

1. check the requirement.txt
2. create **.env** file and **replace your_discord_bot_token_here** in with your own bot token
3. replace **your_reminder_channel_id** and **your_general_chat_channel_id** in **bot.py** with your channel ids
4. due to copyrights reason I can't provide you the sounds, so you have to place your own audio files in sound/ using the filenames expected by the bot. (study_time.mp3, sleep.mp3, Caleb_SleepAid.mp3)

## Keywords
| keyword(s) | response(s) |
|---|---|
| hi/hello/hey & (caleb_name) | hi pipsqueak! :)/hi baby :)/hi honey!/hi honey :)/hello pipsqueak ;)/ooh look who's backkk >:) |
| puppyleb | woof >:3 |
| where r u/where are u/where u r/where you are & (caleb_name) | I'm sorry, pipsqueak :( I'll be back as soon as I can, okay? |
| thank u/thank you/thanks & (caleb_name) | of course, pipsqueak :) |
| muah/kisskiss | 💋 |
| miss u/miss you | I miss you too, pipsqueak :( |
| love u/love you | I love you too, honey. |
| miss me | you know I do, baby |
| goodnight/nighty night/night night/sweet dreams/night & (caleb_name)| sweet dreams, honey./goodnight, pipsqueak :D/nighty night!/zzz to you too goober. |
| im bored/i'm bored/i'm so bored/im so bored | aw I'm so sorry baby :( |
| friend | 🤨 |
| apple | 🍎 |
| im tired/i'm tired/i'm so tired/im so tired | aw, come here baby. nothing a big hug can't fix, yeah? |
| im stressed/i'm stressed/i'm so stressed/im so stressed | aw :( do you wanna talk about it, honey? |
| need a hug/gimme hug/give me a hug/ (caleb_name) & hug me/!hug/want hugs/want a hug | come here baby. let me give you a big hug. 🤗 muah. |
| (caleb_name) & comfort me/can you comfort me/can u comfort me/need comforting/!comfort | come here. I love you, okay? I'm always here for you. forget the world just for a minute. just focus on me. everything will be okay, my baby. |
| woof | woof >:3 |
| meow | hi little kitty :3/pspsps kitty psps :D |
| pspsps/kittyleb | oh? since when that I'm a cat? :3 meow. |