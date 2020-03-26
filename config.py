
import os

BASE_DIRS = os.path.dirname(__file__)  # 当前文件的绝对路径

options = {
    'port': 9000,

}

settings = {
    'static_path': os.path.join(BASE_DIRS, 'static'),
    'template_path': os.path.join(BASE_DIRS, 'templates'),
    'debug': True,
}
