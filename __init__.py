import nonebot
import aiohttp
import random
import string

from nonebot import on_command, on_message
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Message, MessageSegment, Bot
from nonebot.adapters.onebot.v11.event import Event, MessageEvent, PrivateMessageEvent,GroupMessageEvent
from .config import Config, ConfigError
from .ChatSession import ChatSession



# 配置导入
plugin_config = Config.parse_obj(nonebot.get_driver().config.dict())

# 导入设置内的API，模型名称，AppID
yinying_api_key = plugin_config.yinying_api_key
yinying_model_name = plugin_config.yinying_model_name
yinying_app_id = plugin_config.yinying_app_id
session = {}

# 带上下文的聊天
chat_record = on_command("chat", block=False, priority=1)

# 停止聊天
stop_chat = on_command("stop", block=True, priority=1)

# 清除历史记录
clear_request = on_command("clear", block=True, priority=1)

# 开始聊天
@chat_record.handle()
async def _(event: MessageEvent, msg: Message = CommandArg()):
    # 若未开启私聊模式则检测到私聊就结束
    if isinstance(event, PrivateMessageEvent) and not plugin_config.enable_private_chat:
        chat_record.finish("对不起，私聊暂不支持此功能。")

    # 检测是否填写 API key
    if yinying_api_key == "":
        await chat_record.finish(MessageSegment.text("请先配置银影APIKEY"), at_sender=True)

    # 提取提问内容
    content = msg.extract_plain_text()
    if content == "" or content is None:
        await chat_record.finish(MessageSegment.text("内容不能为空哦~"), at_sender=True)

    # 创建会话ID
    session_id = create_session_id(event)

    # 如果会话ID不存在，则创建一个新的ChatSession实例
    if session_id not in session:
        session[session_id] = ChatSession("yuanluobot", yinying_api_key, yinying_model_name,event)

    # 开始请求
    try:
        res = await session[session_id].get_response(content, event)

    except Exception as error:
        await chat_record.finish(str(error), at_sender=True)
    await chat_record.finish(MessageSegment.text(res), at_sender=True)

# 清除历史记录
@clear_request.handle()
async def _(event: MessageEvent):
    del session[create_session_id(event)]
    await clear_request.finish(MessageSegment.text("成功清除历史记录~"), at_sender=True)

# 根据消息类型创建会话ID
def create_session_id(event):
    if isinstance(event, PrivateMessageEvent):
        session_id = f"Private_{event.user_id}"
    elif isinstance(event, GroupMessageEvent):
        session_id = str(event.user_id)  # 使用群成员的QQ号作为会话ID
    else:
        session_id = f"Other_{event.user_id}"
    return session_id

# 生成随机字符串
def generate_random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# 请求自定义API
async def get_response(content: str, event: MessageEvent):
    # 自定义API相关参数
    custom_api_app_id = yinying_app_id  # 替换为实际的appId
    custom_api_token = yinying_api_key  # 替换为实际的API Token
    custom_api_model = yinying_model_name # 替换为实际的模型名称

    # 创建会话ID
    session_id = create_session_id(event)

    # 如果会话ID不存在，则创建一个新的ChatSession实例
    if session_id not in session:
        session[session_id] = ChatSession(custom_api_app_id, custom_api_token, custom_api_model,event)

    # 构造请求数据
    custom_api_data = {
        "appId": custom_api_app_id,
        "chatId": session[session_id].chatId,
        "model": custom_api_model,
        "message": content,
    }

    # 打印调试信息
    print(f"Event: {event}")
    print(f"Content: {content}")
    print(f"Custom API Data: {custom_api_data}")

    # 发送请求
    async with aiohttp.ClientSession() as http_session:
        async with http_session.post(
                "https://api-yinying-ng.wingmark.cn/v1/chatWithCyberFurry",
                headers={"Authorization": f"Bearer {custom_api_token}"},
                json=custom_api_data,
        ) as response:
            response_data = await response.json()
            print(f"Response Data: {response_data}")
            return response_data["choices"][0]["message"]["content"]