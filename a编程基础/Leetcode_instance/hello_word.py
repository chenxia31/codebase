import sys 
sys.path.append('/Users/xuchenlong/Downloads/Chenlongxu的代码仓库/0 模板代码仓库_portable/')
from utils import timer

@timer 
def hello_word():
    print('Hello Word!')

hello_word()