from environs import Env


env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN") 
ADMINS = env.list("ADMINS") 
IP = env.str("ip") 
CHANNELS = ["-1001507962338"]


# import os

# BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
# ADMINS = list(os.environ.get("ADMINS"))
# IP = str(os.environ.get("ip"))
# CHANNELS = list(os.environ.get("CHANNELS"))