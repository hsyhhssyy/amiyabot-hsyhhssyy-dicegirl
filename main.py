import re
import time
import datetime
import json
import copy
import random
import os
import importlib
import inspect
import pathlib

from amiyabot import PluginInstance
from amiyabot.util import temp_sys_path, extract_zip
from core.util import read_yaml
from core import log, Message, Chain
from core.database.user import User, UserInfo
from core.database.bot import OperatorConfig
from core.resource.arknightsGameData import ArknightsGameData, ArknightsGameDataResource, Operator

curr_dir = os.path.dirname(__file__)

class QuickActionPluginInstance(PluginInstance):
    def install(self):
        pass

bot = QuickActionPluginInstance(
    name='兔兔骰娘',
    version='1.0',
    plugin_id='amiyabot-hsyhhssyy-dicegirl',
    plugin_type='official',
    description='让兔兔可以做一个骰娘',
    document=f'{curr_dir}/README.md'
)

async def roll(text_command):
    reg = '(roll|\.rh|\.r)[\s]*([\d]+?)[D|d]([\d]+)(([+|-])([\d]+)){0,1}'
    
    match = re.search(reg,text_command)

    # log.info(f'{match} {data.text_initial}')

    # log.info(f'{match.group(1)} {match.group(2)} {match.group(3)} {match.group(4)} {match.group(5)}')

    x = int(match.group(2))
    y = int(match.group(3))

    symbol = match.group(5)
    if match.group(4):
        z = int(match.group(4))
    else:
        z = 0
    
    # log.info(f'{x} {y} {z}')

    text = '详细骰子情况为：'
    total = 0

    while x > 0: 
        rand = random.randint(1, y)
        total = total + rand
        text += f'{rand} '
        x = x - 1
    
    total = total+z

    return total,text

@bot.on_message(keywords=['sroll','.rh'],level=11)
async def _(data: Message):

    total, text = await roll(data.text_initial)

    if not total :
        return Chain(data).text('如果想让我秘密roll点的话，请说sroll XDY(+/-Z)')

    await data.instance.send_message(Chain().text(f'您的秘密掷骰结果为：{total}。'+text+'。'),
                       user_id=data.user_id)

    return Chain(data).text(f'您的秘密掷骰结果已经私聊发送给您了。')

@bot.on_message(keywords=['roll','.r'],level=10)
async def _(data: Message):

    total, text = await roll(data.text_initial)

    if not total :
        return Chain(data).text('如果想让我roll点的话，请说roll XDY(+/-Z)')

    return Chain(data).text(f'您的掷骰结果为：{total}。'+text+'。')