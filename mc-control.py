#!/usr/bin/python3
import discord
import pprint
import botconfig as cfg
import sys
import aws_helpers

TOKEN = cfg.token
instance_id = cfg.instance_id
master_channel = cfg.master_channel

client = discord.Client()
pp = pprint.PrettyPrinter(indent=4)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    else:
        print("message from " + str(message.author))
        print("message was: " + str(message.author) +  "->" + str(message.content))
        print("channel was: " + str(message.channel))

    if str(message.channel) != master_channel:
        print("ignoring wrong channel")
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message) + 'I am the Minecraft Server Bot'
        await client.send_message(message.channel, msg)
        print("got a hello command")
    elif message.content.startswith('!crash'):
        #exit()
        sys.exit("Crash command sent")
    elif message.content.startswith('!start'):
        #msg = 'Start command running'
        #await client.send_message(message.channel, msg)
        response = aws_helpers.startInstance()
        msg = 'The minecraft server is starting.'
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!stop'):
        #msg = 'Stop command running'
        #await client.send_message(message.channel, msg)
        response = aws_helpers.stopInstance()
        msg = 'The minecraft server is stopping. '
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!status'):
        #msg = 'Status command running'
        #await client.send_message(message.channel, msg)
        response = aws_helpers.describeInstances()
        status = aws_helpers.describeStatus(response)
        print(status)
        msg = 'The minecraft server is: ' + status
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!help'):
        msg = """ Help commands: 
                    !hello - test to make sure the bot is listening
                    !start - start the minecraft server
                    !stop - stop the minecraft server
                    !status - fetch status of running 
        """
        await client.send_message(message.channel,msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    msg = "Minecraft bot has fired up and is operational"
    await client.send_message(client.get_channel(cfg.bot_channel_id), msg)

client.run(TOKEN)

