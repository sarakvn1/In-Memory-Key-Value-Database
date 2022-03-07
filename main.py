import sys

from mappers import cmd_mapper
from nodes import LinkedList
from tools import clean_inputs, split_input

linked_list = {"default": LinkedList()}
current_db = "default"
x = True


class CMD:
    def __init__(self, first_input=None, second_input=None, l_list=None):
        self.firs_input = first_input
        self.second_input = second_input
        self.next = None
        self.l_list = l_list
        self.prev = None

    def cmd_set(self):
        node_exist = self.l_list.search(self.firs_input)
        if node_exist is False:
            if self.l_list.head is None:
                self.l_list.push((self.firs_input, self.second_input))
            else:
                self.prev, self.next = self.l_list.position(self.firs_input)
                self.l_list.push((self.firs_input, self.second_input), prev=self.prev, next=self.next)

        else:
            self.l_list.update(node_exist, (self.firs_input, self.second_input))
        # self.l_list.print_list()
        print("ok")

    def cmd_get(self):
        obj = self.l_list.search(self.firs_input)
        if obj is False:
            print("record not found")
        else:
            print(obj.data[1])

    def cmd_del(self):
        node_exist = self.l_list.search(self.firs_input)
        if node_exist is False:
            print("record not found")
        else:
            self.l_list.delete(self.firs_input)
            print("success")

        self.l_list.print_list()

    def cmd_dump(self):
        f = open(self.second_input, "w")
        for i in self.l_list.print_list():
            f.write(f"{i[0]} {i[1]}\n")
        f.close()
        print("ok")

    @staticmethod
    def cmd_list():
        print(list(linked_list.keys()))

    def cmd_load(self):
        f = open(self.firs_input, "r")
        for i in f:
            part = i.split(' ')
            self.firs_input = part[0].replace('\n', '')
            self.second_input = part[1].replace('\n', '')
            self.cmd_set()
        self.l_list.print_list()

    def cmd_keys(self):
        result = self.l_list.search_with_regex(self.firs_input)
        for i in result:
            print(i.data[0])


while x is True:
    for line in sys.stdin:
        if line != '':
            line = clean_inputs(line)
            cmd, input_1, input_2, length = split_input(line)
            cmd_len = cmd_mapper.get(cmd)

            if cmd == 'load':
                db = input_1
                if linked_list.get(db) is None:
                    linked_list[db] = LinkedList()
                    print(linked_list.get(db))
                current_db = db

            elif cmd == 'dump':
                db = input_1
                if linked_list.get(db) is None:
                    print("db not found")
                else:
                    current_db = db

            elif cmd == 'exit':
                x = False
                print("bye")
                break

            if cmd == 'use':
                db = input_1
                if linked_list.get(db) is None:
                    linked_list[db] = LinkedList()
                current_db = db
            elif cmd_len is not None and length == cmd_len and cmd_len == 3:
                command = getattr(
                    CMD(input_1, input_2, l_list=linked_list.get(current_db)),
                    f'cmd_{cmd}')()
            elif cmd_len is not None and length == cmd_len and cmd_len == 2:
                command = getattr(CMD(first_input=input_1, l_list=linked_list.get(current_db)), f'cmd_{cmd}')()
            elif cmd_len is not None and length == cmd_len and cmd_len == 1:
                command = getattr(CMD(), f'cmd_{cmd}')()
            else:
                print("command not found")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
