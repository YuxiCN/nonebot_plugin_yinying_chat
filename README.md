<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-yinying-chat
</div>


# 介绍

- 本插件适配银影API，可以在nonebot中调用的银影API，可根据调用配置自定义模型进行回复。
# 使用方法

- chat 使用该命令进行聊天
- @机器人 chat 使用该指令进行聊天也可以
- clear 清除当前用户的聊天记录

# 配置

yinying_api_key: Optional[str] = "" # 在这里输入银影APIKEY

yinying_model_name: Optional[str] = "" #在这里输入模型名称

yinying_app_id: Optional[str] = ""    #在这里输入AppID

enable_private_chat: bool = True    #是否开启私聊
	
yinying_chat_public: bool = False  # 群聊是否开启公共会话#


##  安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-yinying-chat

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-yinying-chat
</details>
<details>
  



