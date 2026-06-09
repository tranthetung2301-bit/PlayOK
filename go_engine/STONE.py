#Tạo class để tạo tên cho các giá trị của quân cờ
from enum import Enum 
class Stone(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2