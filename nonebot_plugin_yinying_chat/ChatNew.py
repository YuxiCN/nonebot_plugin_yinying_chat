# -- coding: utf-8 --
import nonebot
import aiohttp
import random
import string

from nonebot import on_command, CommandSession, get_plugin_config
from nonebot.adapters import Bot
from nonebot.adapters.cqhttp.event import MessageEvent, PrivateMessageEvent, GroupMessageEvent

# ��ȡ�������
config = get_plugin_config("Yuanluo")
yinying_api_key = config.yinying_api_key
yinying_model_name = config.yinying_model_name
yinying_app_id = config.yinying_app_id

# �������ĵ�����
chat_record = on_command("chat", block=False, priority=1)

# ��ʼ����
@chat_record.handle()
async def chat(session: CommandSession):
    # ��δ����˽��ģʽ���⵽˽�ľͽ���
    if isinstance(session.event, PrivateMessageEvent) and not config.enable_private_chat:
        await session.finish("��ʱ��֧���������Ŷ~")

    # ����Ƿ���д API key
    if yinying_api_key == "":
        await session.finish("����������ӰAPIKEY")

    # ��ȡ��������
    content = session.current_arg_text.strip()
    if not content:
        await session.finish("���ݲ���Ϊ��Ŷ~")

    # ��ȡ�ش�
    try:
        answer = await get_answer(content, session.event)
    except Exception as e:
        await session.finish(str(e))

    # ����ش�
    await session.finish(answer)

# ������Ϣ���ʹ����ỰID
def create_session_id(event):
    if isinstance(event, PrivateMessageEvent):
        session_id = f"Private_{event.user_id}"
    elif isinstance(event, GroupMessageEvent):
        session_id = str(event.user_id)  # ʹ��Ⱥ��Ա��QQ����Ϊ�ỰID
    else:
        session_id = f"Other_{event.user_id}"
    return session_id

