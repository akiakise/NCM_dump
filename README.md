# NCM格式文件转换 (Python version)

## 简介

本项目 fork 自大佬的移植 python 版本项目[nondanee/ncmdump](https://github.com/nondanee/ncmdump) 在此非常感谢

也非常感谢原 C++ 版本代码大佬的 [anonymous5l/ncmdump ](https://github.com/anonymous5l/ncmdump)项目，感谢源代码作者的 Walkman帮了大忙（大雾）

如原作者描述 python 版本运行相对较慢 但是优势在于安装简单（原C++版本需要自行编译taglib相对操作较多）

另：原python版本使用的是pycrypto库相对较老且在部分一体包中的实现相对较差 已替换使用相对较新兼容性较好的pycryptodomex（pycryptodome的共存版本）

仅供学习交流 请勿传播扩散

## 依赖

- python 3.6 （3.*系列）

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## 使用

运行GUI即可打开可视化界面
```
python(3) GUI_TRANS.py
```
包含两种处理：`单个ncm文件处理`和`指定文件夹内所有ncm文件批量处理`

两种输入方式：

- `输入`文件（夹）路径
- `按钮选择`单个文件或文件夹

点击`转换`按钮即可进行转换
