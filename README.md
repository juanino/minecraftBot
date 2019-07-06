# minecraftBot
A bot to control ec2 instances
Based off of some work done here: https://github.com/juanino/shopbot

This bot is used to allow my kids and friends to control a single instance in ec2 
from their discord server.  To keep the costs down their minecraft server shuts down
via a cron nightly.

## Usage in discord

Try !hello first, to confirm the bot is up.
```!hello```
The bot should return with:

```Hello [your user] I am the Minecraft Server Bot```

You can also issue a help command:
```!help
minecraft-controllerBOTToday at 8:55 AM
Help commands: 
                    !hello - test to make sure the bot is listening
                    !start - start the minecraft server
                    !stop - stop the minecraft server
                    !status - fetch status of running```
