# 智障树自动挂机
## 特色 Feature
- **玄学防封** 使用自动化测试技术，挂课时启动真实浏览器，减低被检测的概率
- **完全后台** 可以完全挂在在后台运行，不影响你玩，运行也不需要前台焦点
- **自动快播** 自动1.5倍速播放 你的时间非常值钱
- **人工智障答题** 自动瞎JB答视频中间的各种题目（又不是不能过.jpg）
- **自动跳课** 一集一集根本停不下来
## 配置 Configuration
### 1.安装python并配置
建议直接安装Anaconda

https://www.anaconda.com/
安装时勾选配置环境变量，或者自己配置环境变量
### 1.安装requirement.txt中的库
```python
pip install -r requirement.txt
```
### 2.配置selenium环境
这一步可能会遇到很多问题，建议多百度解决
搜索关键字 ```selenium python 环境搭建```

我这里使用的是chrome的浏览器，如果你没有chrome浏览器，下载一个。

如果你是firefox党，你也可以试着自己修改代码并安装firefox的驱动。

下载配套的chromedirver，下面的网站可以下载到，如果网站无法访问也可以从百度上找**浏览器和驱动版本号对应**就行
https://sites.google.com/a/chromium.org/chromedriver/home

然后把驱动放到chrome软件目录下，这个目录应该在
C:\Program Files (x86)\Google\Chrome\Application

### 3.打开AmentiaTree.py修改内容

username 你的账号

passwd 你的密码

url 要挂的课的url（课已经选了）

### 4.一切就绪 执行脚本 


## 使用建议
开启后不要管脚本了，不要在脚本接管的浏览器中做任何操作
建议把网页的声音禁掉

