# PySys —— 基于 Python 的简单系统框架

PySys 是一款非常简单和集成的系统框架，它和操作系统相近，但是不能叫做操作系统，因为它并没有直接通过驱动操控电脑的硬件，而是和虚拟机类似地运行在基础的系统之上。它的用处就是让你能够简单、集成地使用到 Python 的各个模块，让你能够在使用中体会这些模块的简易和强大，与其说 PySys 是一个系统，更不如说它是一个工具集。当然，PySys 作为一款系统，它也有类似于系统的特点，它可以直接操控基础系统中的目录和文件，它也可以生成虚拟硬盘来专门存储 PySys 的数据，还能够联网、管理用户和权限等等。由于 PySys 只是系统的框架，它并没有 GUI 图形界面，只能通过 PSTerm (PySys Terminal) 操控整个 PySys 系统，后续可能会开发相应的图形界面 PSUI，可能不会在一年之内完成。

PySys 原本是 @bobby233 在 2019 年开始开发的项目，大约在 2020 年将其作为仓库上传至 GitHub，又因为各种时间和个人原因暂时关闭了 GitHub 仓库，再之后将其留作备用（见 [PySys-old](https://github.com/bobby233/PySys-old)）。在将近一年后，@bobby233 重新在 GitHub 上传了同名仓库，重写了大部分代码，优化了几乎所有的算法和功能实现方法，提升了程序整体的性能。

## 快速上手

想要运行 PySys 十分简单，首先你需要安装 Python3 环境（由于 PySys 是 Python3.9.5 编写的，推荐安装  Python3.9 系列）。请前往 [Python 下载页面](https://www.python.org/downloads/) 选择版本下载安装，不要前往不安全的网站下载，最好在下载完后检验校验码。注意安装时需要把 Python 加入 PATH 来方便地从命令行调用 Python。

在安装完 Python3 后，只需要几句命令即可进入 PySys 的世界：

```cmd
git clone https://github.com/bobby233/PySys.git
cd PySys
python PySys.py
```

*注意：UNIX (Linux & macOS) 用户需要把 `python` 替换成 `python3`，否则程序将以默认的 Python2 运行。*

## TODO

1. [ ] 完成 README 中其他部分的编写
2. [ ] 完成 PSTerm 的编写，不让系统只有应急模式
3. [ ] 完成 .psy (PySys Python format, ψ) 格式的编写，创造属于 PySys 自己的执行文件格式
4. [ ] 完成 .psvd (PySys Virtual Disk) 虚拟硬盘格式的编写，让多个 .psy 或其它格式文件合成一个仅供 PySys 读取的虚拟硬盘
5. [ ] 完成 PSC (PySys Cipher) 的规范和编写，本步骤需要多方协助