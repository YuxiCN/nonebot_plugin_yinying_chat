from pydantic import Extra, BaseModel
from typing import Optional
import nonebot


#定义配置文件
class Config(BaseModel, extra=Extra.ignore):
    yinying_api_key: Optional[str] = "" # 在这里输入银影APIKEY
    yinying_model_name: Optional[str] = "" #在这里输入模型名称
    yinying_app_id: Optional[str] = ""    #在这里输入AppID
    enable_private_chat: bool = True    #是否开启私聊
    yinying_chat_public: bool = False  # 群聊是否开启公共会话


class ConfigError(Exception):
    pass

global_config = nonebot.get_driver().config