# Imports
try:
    import discord, time, random, sys, asyncio, colorama, warnings, pystyle, os, re
    from colorama import Fore, Back, Style
    from discord.ext import commands
    from pystyle import Colors, Colorate, Center
except ImportError as e:
    print("Error: " + str(e))
    exit()

# Variables
clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear") # Don't touch this
token = "" # Token here
counting_channel = "" # Counting channel ID 
humanized = False # Use True if you want a randomized delay of False if you want it to be instant
delay = [0.5, 5] # Don't touch this
typing_delay = [0.6, 1.2] # Don't touch this
selfbot = True # Self explanatory
last_number = "" # Don't touch this
shutdown = "" # Emergency shutdown word anybody can use to stop the selfbot (Make this something people wont say accidentally!)

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
    print(f"\n{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Logging in...")
    if humanized == True:
        print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}]{Fore.RESET} Logged in as {Fore.MAGENTA}{bot.user}{Fore.RESET} - {Fore.GREEN}(Humanized delay){Fore.GREEN}{Fore.RESET}\n")
        os.system(f"title Counter - Logged in as {bot.user} - Humanized delay - Ready")
    elif humanized == False:
        print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}]{Fore.RESET} Logged in as {Fore.MAGENTA}{bot.user}{Fore.RESET} - {Fore.RED}(Botted delay){Fore.RED}{Fore.RESET}\n")
        os.system(f"title Counter - Logged in as {bot.user} - Botted delay - Ready")
    else:
        print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.RESET} Failed to login.")
        time.sleep(3)
        exit()

# Getting & sending the numbers
@bot.event
async def on_message(message):
    if message.content == shutdown:
        print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Emergency Shutdown Activated")
        os._exit(1)
    else:
        pass
    num_strip = re.sub("[^0-9]", "", message.content) # Remove any data from the message that aren't numbers
    global last_number
    try:
        if bot.user.id != message.author.id and message.channel.id == int(counting_channel):
            channel = bot.get_channel(int(counting_channel))
            try:
                if last_number == "":
                    last_number = int(num_strip)
                else:
                    pass
            except:
                pass
            else:
                if humanized:
                    sleep = random.uniform(delay[0], delay[1])
                    typesleep = random.uniform(typing_delay[0], typing_delay[1])
                    time.sleep(sleep)
                else:
                    sleep = 0
                    pass  
                if int(num_strip) < last_number:
                    print(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Lower number detected! Skipping...")
                elif int(num_strip) > (last_number + 1):
                    print(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Higher number detected! Skipping...")
                else:
                    if humanized:
                        async with channel.typing():
                            time.sleep(typesleep)
                            last_number += 2
                            num = int(num_strip)
                            bigger_num = num + 1
                        await channel.send(bigger_num)
                        print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Sending: {Fore.MAGENTA}" + str(bigger_num) + f". {Fore.RESET}Next number is {Fore.YELLOW}{str(last_number)}{Fore.RESET}. (Delay: {Fore.LIGHTCYAN_EX}{str(sleep+typesleep)}{Fore.RESET} seconds)")
                    else:
                        last_number += 2
                        num = int(num_strip)
                        bigger_num = num + 1
                        await channel.send(bigger_num)
                        print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Sending: {Fore.MAGENTA}" + str(bigger_num) + f". {Fore.RESET}Next number is {Fore.YELLOW}{str(last_number)}{Fore.RESET}. ")
    except ValueError as e:
        print(f"{Fore.YELLOW}[{Fore.RESET}-{Fore.YELLOW}]{Fore.RESET} Invalid number: " + str(num_strip))
    except Exception as e:
        print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.RESET} Error: " + str(e))

# Start
try:
    clear()
    asyncio.run(bot.run(token))
except KeyboardInterrupt:
    print(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Exiting...")
    time.sleep(1)
    exit()
except Exception as e:
    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.RESET} Error: " + str(e))
