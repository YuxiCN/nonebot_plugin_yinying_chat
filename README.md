<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-yinying-chat
</div>


# 介绍

  本插件适配银影API，可以在nonebot中调用的银影API，可根据调用配置自定义模型进行回复。

> [!WARNING]
> 本插件使用时需要提供对应API和AppId，如果没有对应的，需要联系银影开发者秩乱申请API，才可以使用

> [!WARNING]
> 银影[官网链接](https://chat.wingmark.cn/)，银影官方QQ群：175334224，秩乱的联系方式（QQ）：1660466270

> [!WARNING]
> 使用本插件和银影API时，需遵守相关法律法规及在使用本插件和银影API时，请务必遵守相关法律法规及[API使用规范](https://wingmark.feishu.cn/docx/Zk5RdCKSRoBnH8xI3jfcTXBEnXe)

> [!WARNING]
> 如因未遵守相关法律法规和API使用规范，造成的一切后果均由插件使用者承担，开发者不承担任何责任

# 使用方法

- chat 使用该命令进行聊天
- @机器人 chat 使用该指令进行聊天也可以
- clear 清除当前用户的聊天记录

# 配置文件
在nonebot全局变量文件（一般为.env.prod）内加入如下变量

YINYING_API_KEY=

YINYING_MODEL_NAME=

YINYING_APP_ID=

ENABLE_PRIVATE_CHAT=

YINYING_CHAT_PUBLIC=


配置文件示例：

```dotenv
YINYING_API_KEY=你的APIKEY
YINYING_MODEL_NAME=模型名称
YINYING_APP_ID=你的AppId
ENABLE_PRIVATE_CHAT=True
YINYING_CHAT_PUBLIC=False
```


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
  



