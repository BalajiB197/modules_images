import os
import pytest
from modules import *

path = './images/'
import os.path
import types
import sys

module_name = "modules"
module_file = 'modules.py'
module_path = '.'

module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

with open(module_rel_file_path, 'r') as code_file:
    source_code = code_file.read()

# create a module object
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

sys.modules[module_name] = mod

code = compile(source_code, filename=module_abs_file_path, mode='exec')

exec(code, mod.__dict__)

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_j2p():
    status = j2p(path)
    assert status == True, 'function call successfully'

def test_p2j():
    status = p2j(path)
    assert status == True, 'function call successfully'

def test_res_w():
    status = res_w(path, new_width=500) # width=500
    assert status == True, 'function call successfully'

def test_res_h():
    status = res_h(path, new_height=500) #height=500
    assert status == True, 'function call successfully'

def test_res_p():
    status = res_p(path, new_percent=0.80) # 80 percent
    assert status == True, 'function call successfully'

def test_crp_px():
    status = crp_px(path, new_length=224) # center_crop=224
    assert status == True, 'function call successfully'

def test_j2p_1():
    status = mod.j2p(path)
    assert status == True, 'function call successfully'

def test_p2j_2():
    status = mod.p2j(path)
    assert status == True, 'function call successfully'

def test_res_w_2():
    status = mod.res_w(path, new_width=500) # width=500
    assert status == True, 'function call successfully'

def test_res_h_2():
    status = mod.res_h(path, new_height=500) #height=500
    assert status == True, 'function call successfully'

def test_res_p_2():
    status = mod.res_p(path, new_percent=0.80) # 80 percent
    assert status == True, 'function call successfully'

def test_crp_px_2():
    status = mod.crp_px(path, new_length=224) # center_crop=224
    assert status == True, 'function call successfully'

def test_res_h_3():
    status = mod.res_h(path, new_height=400) #height=400
    assert status == True, 'function call successfully'

def test_res_p_3():
    status = mod.res_p(path, new_percent=0.70) # 70 percent
    assert status == True, 'function call successfully'

def test_crp_px_3():
    status = mod.crp_px(path, new_length=250) # center_crop=250
    assert status == True, 'function call successfully'

def test_res_w_3():
    status = res_w(path, new_width=200) # width=200
    assert status == True, 'function call successfully'

def test_res_h_4():
    status = res_h(path, new_height=200) #height=200
    assert status == True, 'function call successfully'

def test_res_p_5():
    status = res_p(path, new_percent=0.60) # 60 percent
    assert status == True, 'function call successfully'

def test_crp_px_5():
    status = crp_px(path, new_length=160) # center_crop=160
    assert status == True, 'function call successfully'