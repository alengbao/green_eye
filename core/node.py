import inspect
import types
import typing
from typing import Tuple


class Node:
    cnt = 0

    def __init__(self):
        self.inputs = ()
        self.outputs = ()
        self.connected_to = []
        self.next = []
        self.code = ''
        self.name = 'default'

        self.call_func = None
        self.env = {}
        self.local_scope = {}
        self.cleanup_func = None
        self.problem = False
        self.problem_desc = ''
        self.proc_result = None

    def draw(self, x=None, y=None):
        pass

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

            if tuple in signature.return_annotation.mro():
                out = []
                i = 0
                for arg in list(signature.return_annotation.__args__):
                    is_string = isinstance(arg, typing.ForwardRef) and isinstance(arg.__forward_arg__, str)
                    out.append(arg.__forward_arg__ if is_string else 'result ' + str(i))
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

    def processor(self):
        connected_to = self.connected_to
        outputs = self.outputs
        if self.proc_result:
            return self.proc_result

        gen_inputs = {}
        for connection in connected_to:
            try:
                inputs = connection['output']['node'].processor()
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

        return self.proc_result

    def add_connected(self, node, put):
        self.connected_to.append({
            'output': {
                'node': node,
                'name': node.outputs[0]
            },
            'input': {
                'name': put
            }
        })