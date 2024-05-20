#!/usr/bin/python3
import marshal
import types

def list_module_names(pyc_file):
    with open(pyc_file, 'rb') as f:
        f.seek(16)  # Skip the header
        code = marshal.load(f)
        return [name for name in dir(types.ModuleType('__main__', code)) if not name.startswith('__')]

if __name__ == "__main__":
    names = list_module_names('/tmp/hidden_4.pyc')
    for name in sorted(names):
        print(name)

