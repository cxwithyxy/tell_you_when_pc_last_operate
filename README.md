# tell_you_when_pc_last_operate
通过web接口, 告知你电脑最后一次操作是什么时候



## 使用

#### 安装

1. 去[发布页](https://github.com/cxwithyxy/tell_you_when_pc_last_operate/releases)下载程序，程序已经被打包成7z压缩包

2. 用解压工具（winrar、7z、bandizip等）解压到任意目录


#### 启动服务

1. 把目录下 **setting.ini.demo** 文件重命名 **setting.ini**
2. 打开 **setting.ini** 文件可以修改端口等配置信息
3. 双击运行 **tell_you_when_pc_last_operate.exe** 即可

#### 连接web接口

默认设置的接口是 http://127.0.0.1:6727 ，因此可以直接通过浏览器访问，并见到文本形式的 json 数据

数据如下：

```
{
	"last_operate_time": 1565837927.3160355,
	"last_operate_name": "mouse left up",
	"interval_time": 0.0010006427764892578
}
```

**last_operate_time** 指最后一次操作时间（单位：秒）

**last_operate_name** 指最后一次操作的类型

**interval_time** 指访问接口时，与最后一次操作时间的间隔时间（单位：秒）



## 开发

#### 安装依赖

```bat
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

#### 运行

```bat
python index.py
```

#### 打包

```bat
pyinstaller index.spec
```