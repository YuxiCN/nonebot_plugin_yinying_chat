import aiohttp
import random
import string
import nonebot

from nonebot import on_command, on_message, get_plugin_config
from nonebot.adapters import Bot
from nonebot.adapters.onebot.v11 import PrivateMessageEvent, GroupMessageEvent
from .ChatNew import get_answer
from nonebot.plugin import Plugin, PluginConfig, PluginManager, on_command, CommandSession, MessageSession, CommandHandler
from .chat import (
    chat_text,
    get_session_id,
    send_to_at,
    finish_with_at,
    get_request,
)
# 定义插件元数据
plugin_metadata = PluginMetadata(
    name="Yuanluo", 
    description="这是一个通过调用银影API来和银影聊天的插件",  
    type="application",
    usage="快来和银影聊天吧~", 
    homepage="https://github.com/YuxiCN/nonebot_plugin_yinying_chat",
    supported_adapters={"~onebot.v11"}
    
)

msg_at = on_message(rule=to_me(), priority=0, block=True)
msg_console = on_command("chat", block=True)

@msg_ml.handle()
@msg_console.handle()
async def _(matcher: Matcher, event: MessageEvent, bot: Bot):
    await get_answer(matcher, event, bot)
