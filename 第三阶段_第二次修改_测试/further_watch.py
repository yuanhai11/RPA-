import time
import os
import shutil
import threading
import logging
import win32api
import win32gui
import win32con
from Crypto.Cipher import AES
from ctypes import windll
from watchdog.observers import Observer

MAP_KEYS = windll.user32.MapVirtualKeyA
from watchdog.utils.dirsnapshot import DirectorySnapshot, DirectorySnapshotDiff
from watchdog.events import FileSystemEventHandler,FileSystemEvent

from logger_manager import LoggerManager
LoggerManager.init_logging("logs/project_update.log", need_mail=False, need_console=True)
logger = logging.getLogger('loggerManager')
logger.setLevel(logging.DEBUG)

class FileEventHandler(FileSystemEventHandler):

    def __init__(self, aim_path):
        FileSystemEventHandler.__init__(self)
        self.aim_path = aim_path
        self.timer = None
        self.snapshot = DirectorySnapshot(self.aim_path)
        self.file_list = []
    def on_any_event(self, event):
        if self.timer:
            self.timer.cancel()

        self.timer = threading.Timer(0.2, self.checkSnapshot)
        self.timer.start()

    def checkSnapshot(self):
        snapshot = DirectorySnapshot(self.aim_path)
        diff = DirectorySnapshotDiff(self.snapshot, snapshot)
        self.snapshot = snapshot
        self.timer = None
        self.file_list = diff.files_modified + diff.files_created + diff.files_deleted + diff.files_moved
        self.file_list = [i.split('0申报流程')[-1].replace(os.path.sep, "", 1) for i in self.file_list]
        self.file_list = list(filter(lambda x:'task' in x ,self.file_list))

        FileEventHandler.create(self,diff.files_created)
        FileEventHandler.delete(self,diff.files_deleted)
        FileEventHandler.modify(self,diff.files_modified)
        FileEventHandler.move(self,diff.files_moved)


    # 文件改变
    def modify(self,modified):
        logger.info("files_modified:{}".format(modified))
        for i in modified:
            time.sleep(2)
            file_name = i.split('0申报流程')[-1].replace(os.path.sep, "", 1)
            if file_name.endswith('.task'):# task文件和flow文件对应的，只需要备份一次
                self.copy_File()
                delete_local_file = os.path.join(local_file_path,file_name)
                os.remove(delete_local_file)
                shutil.copyfile(i,delete_local_file)
                logger.info('更新文件！')
            elif file_name.endswith('.flow'):
                delete_local_file = os.path.join(local_file_path, file_name)
                os.remove(delete_local_file)
                shutil.copyfile(i, delete_local_file)
                logger.info('更新文件！')
            file_old_name = (i.split('0申报流程')[-1].replace('\\', "", 1).replace('\\',''))
            self.file_list.remove(file_old_name)
        if len(self.file_list)==0:
            self.close_api()
            self.open_uibot()

    # 添加新文件
    def create(self,create):
        logger.info("files_create:{}".format(create))
        for i in create:
            time.sleep(2)
            file_name = i.split('0申报流程')[-1].replace(os.path.sep, "", 1)
            if file_name.endswith('.task'):  # task文件和png文件对应的，只需要备份一次
                self.copy_File()
                new_local_file = os.path.join(local_file_path, file_name)
                shutil.copyfile(i, new_local_file)
                logger.info('添加task文件！')
            elif file_name.endswith('.png'):
                local_file_png = os.path.join(local_file_path, file_name)
                shutil.copyfile(i, local_file_png)
                logger.info('添加png图片！')
            file_old_name = (i.split('0申报流程')[-1].replace('\\', "", 1).replace('\\',''))
            self.file_list.remove(file_old_name)
        if len(self.file_list)==0:
            self.close_api()
            self.open_uibot()
    # 删除文件
    def delete(self,delete):
        logger.info("files_deleted:{}".format(delete))
    # 文件改名
    def move(self,move):
        logger.info("files_moved:{}".format(move))
        for i in move:
            time.sleep(1.5)
            name = i[0].split('0申报流程')[-1].replace(os.path.sep, "", 1)
            old_file_name = os.path.join(local_file_path,name)
            os.remove(old_file_name)

            name =  i[1].split('0申报流程')[-1].replace(os.path.sep, "", 1)
            new_file_name = os.path.join(local_file_path,name)
            shutil.copyfile(i[1],new_file_name)
    # 备份
    def copy_File(self):
        bank_path = os.path.join(path, 'Desktop', 'bank')
        if os.path.exists(bank_path):
            bank_path = os.path.join(bank_path, '0申报流程--{}'.format(int(time.time())))
        else:
            os.makedirs(bank_path)
            bank_path = os.path.join(bank_path, '0申报流程--{}'.format(int(time.time())))
        shutil.copytree(local_file_path, bank_path)
        # if ".task" in event.src_path:
        #     file_name = event.src_path.rsplit('0申报流程')[-1].replace("\\", "", 1)
        #     if 'already' in self.all_modified_file_set:
        #         logger.info('本地已经完成了更新！！！')
        #     else:
        #         self.all_modified_file_set.append(file_name)
        #         self.all_modified_file_set = list(set(self.all_modified_file_set))
        #
        #     if 'uibot37b2aa35a6616e.task' in self.all_modified_file_set:
        #         lock.acquire()
        #         logger.info('开始上锁、项目更新！！！')
        #         self.close_api()
        #         # time.sleep(2.3)
        #         try:
        #             self.bank()
        #             # time.sleep(3)
        #             shutil.rmtree(local_file_path)
        #             shutil.copytree(watched_file_path, local_file_path)
        #             # time.sleep(2)
        #         except Exception as e:
        #             logger.error('程序出现错误,尽快解决！！！',e)
        #         finally:
        #             self.open_uibot()
        #             self.all_modified_file_set.clear()
        #             self.all_modified_file_set.append('already')
        #             lock.release()
        #             threading.Timer(5,self.setInterval).start()
        # def bank(self):
        #     bank_path = os.path.join(path, 'Desktop', 'bank')
        #     if os.path.exists(bank_path):
        #         bank_path = os.path.join(bank_path, '0申报流程--{}'.format(int(time.time())))
        #     else:
        #         os.makedirs(bank_path)
        #         bank_path = os.path.join(bank_path, '0申报流程--{}'.format(int(time.time())))
        #     shutil.copytree(local_file_path, bank_path)
        #     logger.info('备份成功！！')
        #
        # def handle_window(self, hwnd, extra, ):
        #     if win32gui.IsWindowVisible(hwnd):
        #         if 'UiBot' in win32gui.GetWindowText(hwnd):
        #             win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        #
        # def close_api(self):
        #     win32gui.EnumWindows(self.handle_window, None)  # 枚举列出所有窗口
        #     time.sleep(5)
        #
        # def open_uibot(self):
        #     time.sleep(1)
        #     win32api.ShellExecute(0, 'open', r'C:\Program Files (x86)\UiBotCreator\Creator', '', '', 1)
        #     # windows_type = "Chrome_WidgetWin_1"
        #     # windows_name = "UiBot Creator"
        #     #
        #     # h_wnd = win32gui.FindWindow(windows_type, windows_name)
        #     # win32gui.ShowWindow(h_wnd, win32con.SW_RESTORE)
        #     # time.sleep(.5)
        #     # win32gui.SetActiveWindow(h_wnd)
        #     # time.sleep(.5)
        #     # win32gui.SetForegroundWindow(h_wnd)
        #     # time.sleep(.5)
        #
        #     time.sleep(8)
        #     win32api.SetCursorPos([1000, 420])
        #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        #     time.sleep(2)
        #
        #     win32api.keybd_event(win32con.VK_F5, MAP_KEYS(116, 0), 0, 0)  # 按下 F5
        #     win32api.keybd_event(win32con.VK_F5, MAP_KEYS(116, 0), win32con.WM_KEYUP, 0)
        #     logger.info('重启UIBOT项目，按F5启动！！！')
        # 接下来就是你想干的啥就干点啥，或者该干点啥就干点啥

    def handle_window(self, hwnd, extra, ):
        if win32gui.IsWindowVisible(hwnd):
            if 'UiBot' in win32gui.GetWindowText(hwnd):
                win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    def close_api(self):
        win32gui.EnumWindows(self.handle_window, None)  # 枚举列出所有窗口
        logger.info('关闭UIBOT程序！！！')
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

if __name__ == "__main__":
    logger.info('开始监控！！！')
    lock = threading.Lock()
    path = os.environ.get('USERPROFILE')
    local_file_path = os.path.join(path,'Desktop','0申报流程')

    aim_path = r"\\192.168.2.70\rpa-share\deploy-test\0申报流程"
    event_handler = FileEventHandler(aim_path)

    obsever = Observer()
    obsever.schedule(event_handler,aim_path,False)
    obsever.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        obsever.stop()
    obsever.join()