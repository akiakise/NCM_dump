# coding: utf-8
import tkinter
import tkinter.filedialog

import dump


class GUI(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("NCM文件转换")
        # 创建一个输入框,并设置尺寸
        self.path_label = tkinter.Label(self.root, text="文件(夹)路径：")
        self.path_input = tkinter.Entry(self.root, width=30)
        self.path_file_button = tkinter.Button(self.root, width=10, command=self.file_selector, text="选择文件")
        self.path_files_button = tkinter.Button(self.root, width=10, command=self.dir_selector, text="选择文件夹")

        # 回显列表
        self.display_info = tkinter.Listbox(self.root, width=60)
        # 转换按钮
        self.result_button = tkinter.Button(self.root, width=15, command=self.ncm_transfer, text="转换")

    # 完成布局
    def init(self):
        self.path_label.grid(row=0, column=0)
        self.path_input.grid(row=0, column=1)
        self.path_file_button.grid(row=0, column=2)
        self.path_files_button.grid(row=0, column=3)
        self.display_info.grid(row=1, columnspan=4)
        self.result_button.grid(row=2, columnspan=4)

    # ncm文件转换
    def ncm_transfer(self):
        self.display_info.delete(0, 'end')
        self.path = self.path_input.get()
        msg = self.dump(self.path)
        self.display_info.insert(0, msg)
        return self.path

    # 单个文件选择
    def file_selector(self):
        self.path_input.delete(0, 'end')
        filename = tkinter.filedialog.askopenfilename()
        if filename != '':
            self.path_input.insert(0, filename)
        else:
            self.path_input.insert(0, "您没有选择任何文件")

    # 文件夹选择
    def dir_selector(self):
        self.path_input.delete(0, 'end')
        dirname = tkinter.filedialog.askdirectory()
        if dirname != '':
            self.path_input.insert(0, dirname)
        else:
            self.path_input.insert(0, dirname)

    # 获取文件并调用dump
    def dump(self, path):
        import os
        # 路径标志位
        dir_flag = False
        # 文件列表
        files = []
        # 文件夹
        if os.path.isdir(''.join(path)):
            files = [file_name for file_name in os.listdir(''.join(path)) if os.path.splitext(file_name)[-1] == '.ncm']
            dir_flag = True
        # 空路径/空文件夹
        elif not path:
            self.display_info.insert(0, '路径为空！输入文件路径！')
        # 单个文件
        elif os.path.isfile(''.join(path)):
            files = [path]
        # 路径错误
        else:
            self.display_info.insert(0, '路径有误！检查无误后继续！')

        for file_name in files:
            try:
                if dir_flag:
                    dump.dumpfile(path + '/' + file_name)
                else:
                    dump.dumpfile(file_name)
                # 成功信息
                self.display_info.insert('end', os.path.split(file_name)[-1] + '已成功转换！')
                self.display_info.update()
            except Exception as e:
                self.display_info.insert('end', e)
                pass


def main():
    # 初始化对象
    gui = GUI()
    # 进行布局
    gui.init()
    # 主程序执行
    tkinter.mainloop()


if __name__ == "__main__":
    main()
