# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import signal
import time
import readchar
import sys
import os
from nodes import LinkedList, Node


def handler(signum, frame):
    msg = "   Ctrl-c was pressed. Do you really want to exit? y/n "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y':
        print("")
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True)  # clear the printed line
        print("    ", end="\r", flush=True)


# signal.signal(signal.SIGINT, handler)

count = 0


def save_method():
    savefile = open('file.txt', 'r+')
    for i in savefile:
        savefile.write(i)
        savefile.flush()  # flushes buffer, saving RAM
    savefile.close()


class CMD:
    def __init__(self, key=None, value=None, parts=None, l_list=None):
        self.key = key
        self.value = value
        self.parts = parts
        self.next = None
        self.l_list = l_list
        self.prev = None

    def cmd_set(self):

        node_exist = self.l_list.search(self.key)
        if node_exist is False:
            if self.l_list.head is None:
                self.l_list.push((self.key, self.value))
            else:
                self.prev, self.next = self.l_list.position(self.key)
                self.l_list.push((self.key, self.value), prev=self.prev, next=self.next)

        else:
            self.l_list.update(node_exist, (self.key, self.value))
        self.l_list.print_list()
        print("finished")

    def cmd_get(self):
        obj = self.l_list.search(self.key)
        if obj is False:
            print("nothing found")
        else:
            print(obj.data[1])

    def cmd_del(self):
        node_exist = self.l_list.search(self.key)
        if node_exist is False:
            if self.l_list.head is None:
                self.l_list.push((self.key, self.value))
            else:
                self.prev, self.next = self.l_list.position(self.key)
                self.l_list.push((self.key, self.value), prev=self.prev, next=self.next)

        else:
            self.l_list.update(node_exist, (self.key, self.value))
        self.l_list.print_list()

    def cmd_dump(self):
        root_dir = os.path.dirname(os.path.abspath(__file__))
        f = open(f"{root_dir}/demofile3.txt", "w")
        for i in self.l_list.print_list():
            f.write(f"{i[0]} {i[1]}")
        f.close()

    @staticmethod
    def cmd_list():
        print(list(linked_list.keys()))


cmd_mapper = {
    "get": 2,
    "set": 3,
    "del": 2,
    "list": 1,
}
linked_list = {"default": LinkedList()}
current_db = "default"
while True:
    for line in sys.stdin:

        parts = line.split(' ')
        cmd = parts[0].replace('\n', '')
        cmd_len = cmd_mapper.get(cmd)
        if cmd == 'use':
            print(linked_list.get('default'))
            db = parts[1].replace('\n', '')
            if linked_list.get(db) is None:
                linked_list[db] = LinkedList()
                print(linked_list.get(db))
            current_db = db
        elif cmd_len is not None and len(parts) == cmd_len and cmd_len == 3:
            command = getattr(CMD(parts[1].replace('\n', ''), parts[2].replace('\n', ''), l_list=linked_list.get(current_db)), f'cmd_{cmd}')()
        elif cmd_len is not None and len(parts) == cmd_len and cmd_len == 2:
            command = getattr(CMD(key=parts[1].replace('\n', ''), l_list=linked_list.get(current_db)), f'cmd_{cmd}')()
        elif cmd_len is not None and len(parts) == cmd_len and cmd_len == 1:
            command = getattr(CMD(), f'cmd_{cmd}')()
        else:
            print("command not found")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
