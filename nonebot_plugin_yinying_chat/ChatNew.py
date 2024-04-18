import nonebot
import aiohttp
import random
import string

from nonebot import on_command, CommandSession, get_plugin_config
from nonebot.adapters import Bot
from nonebot.adapters.cqhttp.event import MessageEvent, PrivateMessageEvent, GroupMessageEvent
from .chat import get_answer

# 获取插件配置
config = get_plugin_config("Hx_YinYing")
yinying_api_key = config.yinying_api_key
yinying_model_name = config.yinying_model_name
yinying_app_id = config.yinying_app_id

# 带上下文的聊天
chat_record = on_command("chat", block=False, priority=1)

# 开始聊天
@chat_record.handle()
async def chat(session: CommandSession):
    # 若未开启私聊模式则检测到私聊就结束
    if isinstance(session.event, PrivateMessageEvent) and not config.enable_private_chat:
        await session.finish("对不起，私聊暂不支持此功能。")

    # 检测是否填写 API key
    if yinying_api_key == "":
        await session.finish("请先配置银影APIKEY")

    # 提取提问内容
    content = session.current_arg_text.strip()
    if not content:
        await session.finish("内容不能为空哦~")

    # 获取回答
    try:
        answer = await get_answer(content, session.event)
    except Exception as e:
        await session.finish(str(e))

    # 输出回答
    await session.finish(answer)

# 根据消息类型创建会话ID
def create_session_id(event):
    if isinstance(event, PrivateMessageEvent):
        session_id = f"Private_{event.user_id}"
    elif isinstance(event, GroupMessageEvent):
        session_id = str(event.user_id)  # 使用群成员的QQ号作为会话ID
    else:
        session_id = f"Other_{event.user_id}"
    return session_id

