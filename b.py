# Imports
try:
    import discord, time, random, sys, asyncio, colorama, warnings, pystyle
    from colorama import Fore, Back, Style
    from discord.ext import commands
    from pystyle import Colors, Colorate, Center
except ImportError as e:
    print(e)
    exit()

# Variables
token = "MTAwMjgwNDA0NTY0OTU1OTcwNQ.GTGSZ4.Iua1ww9KVDQUhWIdgZENfANgkn_-MQAFOarBco" # Token here
counting_channel = "986915223556485170" # Counting channel ID
humanized = False # Use True if you want a randomized delay of False if you want it to be instant
delay = [0.5, 5] # Don't touch this
selfbot = True # Self explanatory
last_number = "" # Don't touch this

# Disable warnings
warnings.filterwarnings("ignore")

# Logo
logo = """
░█████╗░░█████╗░██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░  ██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░╚═╝██║░░██║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝  ██████╦╝██║░░██║░░░██║░░░
██║░░██╗██║░░██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗  ██╔══██╗██║░░██║░░░██║░░░
╚█████╔╝╚█████╔╝╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║  ██████╦╝╚█████╔╝░░░██║░░░
░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░░╚════╝░░░░╚═╝░░░"""
def printLogo():
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, logo, 1)))

# Some settings
if sys.version_info[0] < 3:
    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.RESET} Python 3 or a more recent version is required.")
    exit()

bot = commands.Bot(command_prefix='>', self_bot=selfbot)
bot.remove_command("help")

# Ready event
@bot.event
async def on_ready():
    printLogo()
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name="numbers!"))
    print(f"\n{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Logging in...")
    if humanized:
        print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}]{Fore.RESET} Logged in as {Fore.MAGENTA}{bot.user}{Fore.RESET} - {Fore.GREEN}(Humanized){Fore.GREEN}{Fore.RESET}\n")
    else:
        print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}]{Fore.RESET} Logged in as {Fore.MAGENTA}{bot.user}{Fore.RESET} - {Fore.RED}(Botted){Fore.RED}{Fore.RESET}\n")

# Getting & sending the numbers
@bot.event
async def on_message(message):
    global last_number
    try:
        if bot.user.id != message.author.id and message.channel.id == int(counting_channel):
            channel = bot.get_channel(int(counting_channel))
            try:
                if last_number == "":
                    last_number = int(message.content)
                else:
                    pass
            except:
                pass
            else:
                if humanized:
                    sleep = random.uniform(delay[0], delay[1])
                    time.sleep(sleep)
                else:
                    sleep = 0
                    pass  
                if int(message.content) < last_number:
                    print(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Lower number detected! Skipping...")
                elif int(message.content) > (last_number + 1):
                    print(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Higher number detected! Skipping...")
                else:
                    last_number += 2
                    num = int(message.content)
                    bigger_num = num + 1
                    
                    await channel.send(bigger_num)
                    print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Sending: {Fore.MAGENTA}" + str(bigger_num) + f". {Fore.RESET}Next number is {Fore.YELLOW}{str(last_number)}{Fore.RESET}. (Delay: {Fore.LIGHTCYAN_EX}{str(sleep)}{Fore.RESET} seconds)")
    except ValueError as e:
        print(f"{Fore.YELLOW}[{Fore.RESET}-{Fore.YELLOW}]{Fore.RESET} Invalid number: " + message.content)
    except Exception as e:
        print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.RESET} Error: " + str(e))

# Start
try:
    asyncio.run(bot.run(token))
except KeyboardInterrupt:
    print(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Exiting...")
    time.sleep(1)
    exit()
except Exception as e:
    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.RESET} Error: " + str(e))