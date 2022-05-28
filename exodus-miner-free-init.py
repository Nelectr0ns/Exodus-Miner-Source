import sys
sys.frozen = True

def run(name):
    code = __loader__.get_code(name)
    module_main = __import__('__main__')
    module_main.__dict__['__file__'] = code.co_filename
    exec(code, module_main.__dict__)

