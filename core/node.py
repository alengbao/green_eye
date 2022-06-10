import inspect
import types
import typing
from typing import Tuple

from PyQt5.QtWidgets import QMessageBox


class Node:
    cnt = 1
    dic = {}

    def __init__(self, code='', node_id=None):
        if node_id is None:
            self.id = Node.cnt
            Node.cnt += 1
        else:
            self.id = node_id
            if Node.cnt <= node_id:
                Node.cnt = node_id+1
        Node.dic[self.id] = self

        self.inputs = ()
        self.outputs = ()
        self.connected_to = []
        self.nexts = {}
        self.code = code
        self.name = 'default'

        self.call_func = None
        self.env = {}
        self.local_scope = {}
        self.cleanup_func = None
        self.problem = False
        self.problem_desc = ''
        self.proc_result = None
        self.reload()

    def reload(self):
        self.new_code(self.code)

    def new_code(self, code):
        # self.cleanup()
        self.code = code
        self.problem = False

        self.call_func = None
        self.cleanup_func = None
        try:
            self.env = {'S': self.local_scope}
            exec(code, self.env)

            self.call_func = self.env['call']
            if not isinstance(self.call_func, types.FunctionType):
                raise Exception('Call value is not callable!')

            if 'cleanup' in self.env:
                self.cleanup_func = self.env['cleanup']
        except Exception as ex:
            self.problem = True
        else:
            self.name = self.call_func.__name__

            signature = inspect.signature(self.call_func)
            inputs = tuple(map(lambda x: x.name, signature.parameters.values()))

            if signature.return_annotation is not inspect.Signature.empty:
                out = []
                i = 0
                for arg in list(signature.return_annotation):
                    is_string = isinstance(arg, typing.ForwardRef) and isinstance(arg.__forward_arg__, str)
                    out.append(arg.__forward_arg__ if is_string else 'result' + str(i))
                    i += 1
                outputs = tuple(out)
            else:
                outputs = ('result',)

            self.insert_inouts({'inputs': inputs,
                                'outputs': outputs})

    def insert_inouts(self, data):
        self.inputs = data['inputs']
        self.outputs = data['outputs']

    def cleanup(self):
        try:
            self.cleanup_func()
        except Exception as ex:
            if not self.problem:
                self.problem_desc = "Cleanup error: " + str(ex)
            self.problem = True

    def processor(self, rerun=False):
        connected_to = self.connected_to
        outputs = self.outputs
        if self.proc_result is not None and not rerun:
            return self.proc_result

        gen_inputs = {}
        for connection in connected_to:
            try:
                n = Node.dic[connection['output']['id']]
                inputs = n.processor()
                data = inputs[connection['output']['name']]
            except:
                self.problem = True
                self.problem_desc = 'Can\'t read input'
                continue
            gen_inputs[connection['input']['name']] = data

        get_outputs = {}
        try:
            result = self.call_func(**gen_inputs)
        except Exception as ex:
            if not self.problem:
                self.problem_desc = "Runtime error: " + str(ex)
            self.problem = True
        else:
            if isinstance(result, Tuple) and len(outputs) > 1:
                for output in outputs:
                    item = result[outputs.index(output)]
                    get_outputs[output] = item  # tuple output
            else:
                get_outputs[outputs[0]] = result  # one output
            # build output
            self.proc_result = get_outputs
            self.problem = False

        if self.problem_desc and self.problem:
            print(self.problem_desc)
            self.pop_error()
        if rerun:
            for key in self.nexts.keys():
                Node.dic[key].processor(True)

        return self.proc_result

    def add_connected(self, n, input_name, output_name):
        self.connected_to.append({
            'output': {
                'id': n.id,
                'name': output_name
            },
            'input': {
                'name': input_name
            }
        })
        n.nexts[self.id] = True

    def pop_error(self):
        box = QMessageBox()
        box.setIcon(1)
        box.setWindowTitle("错误")
        box.setText(self.problem_desc)
        # 添加按钮，可用中文
        yes = box.addButton('确定', QMessageBox.YesRole)
        no = box.addButton('取消', QMessageBox.NoRole)
        # 设置消息框中内容前面的图标
        box.setIcon(1)
        box.exec_()
        if box.clickedButton() == yes:
            print('确定')
        else:
            print('取消')
