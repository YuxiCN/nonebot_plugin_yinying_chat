import random
import string
import time
import aiohttp
from nonebot.adapters.onebot.v11.event import MessageEvent,PrivateMessageEvent,GroupMessageEvent

# 定义聊天会话类
class ChatSession:
    def __init__(self, app_id, token, model, event):
        self.app_id = app_id
        self.token = token
        self.model = model
        self.content = []
        self.count = 0
        self.chatId = f"{self.app_id}-{self.create_session_id(event)}-{self.generate_random_string()}"

    # 根据消息类型创建会话ID
    @staticmethod
    def create_session_id(event):
        if isinstance(event, PrivateMessageEvent):
            session_id = f"Private_{event.user_id}"
        elif isinstance(event, GroupMessageEvent):
            session_id = str(event.user_id)  # 使用群成员的QQ号作为会话ID
        else:
            session_id = f"Other_{event.user_id}"
        return session_id

    # 生成随机字符串
    @staticmethod
    def generate_random_string(length=8):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    # 请求自定义API，获取回复
    async def get_response(self, content: str, event: MessageEvent):
        custom_api_data = {
            "appId": self.app_id,
            "chatId": self.chatId,  # 使用 self.chatId 替代 session[session_id].chatId
            "model": self.model,
            "message": content,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                    "https://api-yinying-ng.wingmark.cn/v1/chatWithCyberFurry",
                    headers={"Authorization": f"Bearer {self.token}"},
                    json=custom_api_data,
            ) as response:
                response_data = await response.json()
                print(response_data)  # 打印出返回的数据
                if "choices" in response_data and len(response_data["choices"]) > 0:
                    result = response_data["choices"][0]["message"]["content"]
                    self.content.append({"role": "user", "content": content})
                    self.content.append({"role": "assistant", "content": result})
                    self.count += 1


                    return result
                else:
                    print(f"API request failed with code {response_data['code']}: {response_data['message']}")
                    return None