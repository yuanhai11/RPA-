import shutil
import os
import win32gui
import win32api
from win32.lib import win32con
from Crypto.Cipher import AES
import time
import logging
import threading
import win32con
from ctypes import windll

MAP_KEYS = windll.user32.MapVirtualKeyA
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

from logger_manager import LoggerManager
LoggerManager.init_logging("logs/project_update.log", need_mail=False, need_console=True)
logger = logging.getLogger('loggerManager')
logger.setLevel(logging.DEBUG)

class MyHandler(FileSystemEventHandler):
    '''
    远程备份bank
    删除远程原文件，拷贝本地文件到远程文件
    实现文件更新机制
    '''
    def __init__(self,all_modified_file_set):
        self.all_modified_file_set = all_modified_file_set

    def on_modified(self, event):
        # 改变的文件路径
        # 目前是uibot文件
        # 还需要考虑图片问题
        logger.info('触发了modified！！{}'.format(event.src_path))
        if ".task" in event.src_path:
            file_name = event.src_path.rsplit('0申报流程')[-1].replace("\\", "", 1)
            if 'already' in self.all_modified_file_set:
                logger.info('本地已经完成了更新！！！')
            else:
                self.all_modified_file_set.append(file_name)
                self.all_modified_file_set = list(set(self.all_modified_file_set))

            if 'uibot37b2aa35a6616e.task' in self.all_modified_file_set:
                lock.acquire()
                logger.info('开始上锁、项目更新！！！')
                self.close_api()
                # time.sleep(2.3)
                try:
                    self.bank()
                    # time.sleep(3)
                    shutil.rmtree(local_file_path)
                    shutil.copytree(watched_file_path, local_file_path)
                    # time.sleep(2)
                except Exception as e:
                    logger.error('程序出现错误,尽快解决！！！',e)
                finally:
                    self.open_uibot()
                    self.all_modified_file_set.clear()
                    self.all_modified_file_set.append('already')
                    lock.release()
                    threading.Timer(5,self.setInterval).start()

    def on_created(self, event):
        logger.info('触发了 created！！--{}'.format(event.src_path))

    def on_deleted(self, event):
        logger.info('触发了 deleted！！--{}'.format(event.src_path))

    def on_moved(self, event):
        logger.info('触发了 moved！！--{}'.format(event.src_path))

    def bank(self):
        bank_path = os.path.join(path,'Desktop','bank')
        if os.path.exists(bank_path):
            bank_path = os.path.join(bank_path,'0申报流程--{}'.format(int(time.time())))
        else:
            os.makedirs(bank_path)
            bank_path = os.path.join(bank_path,'0申报流程--{}'.format(int(time.time())))
        shutil.copytree(local_file_path, bank_path)
        logger.info('备份成功！！')

    def handle_window(self,hwnd, extra,):
        if win32gui.IsWindowVisible(hwnd):
            if 'UiBot' in win32gui.GetWindowText(hwnd):
                win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

    def close_api(self):
        win32gui.EnumWindows(self.handle_window, None)  # 枚举列出所有窗口
        time.sleep(5)
    def open_uibot(self):
        time.sleep(1)
        win32api.ShellExecute(0, 'open', r'C:\Program Files (x86)\UiBotCreator\Creator', '', '', 1)

        time.sleep(8)
        win32api.SetCursorPos([1000, 420])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(2)

        win32api.keybd_event(win32con.VK_F5, MAP_KEYS(116, 0), 0, 0)  # 按下 F5
        win32api.keybd_event(win32con.VK_F5, MAP_KEYS(116, 0), win32con.WM_KEYUP, 0)
        logger.info('重启UIBOT项目，按F5启动！！！')
    def setInterval(self):
        self.all_modified_file_set.clear()
        logger.info('5s后启动定时器，进行监控！！！')
if __name__ == "__main__":

    logger.info('开始监控！！')
    lock = threading.Lock()
    path = os.environ.get('USERPROFILE')
    watched_file_path = r"\\192.168.2.70\rpa-share\deploy-test\0申报流程"
    logger.info('监控的路径：{}'.format(watched_file_path))
    local_file_path = os.path.join(path,'Desktop','0申报流程')
    if not os.path.exists(local_file_path):
        os.makedirs(local_file_path)

    all_modified_file_set = []
    event_handler = MyHandler(all_modified_file_set)
    observer = Observer()
    observer.schedule(event_handler, watched_file_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()