import win32gui

from classes import CursorInfo

def get_cursor() -> CursorInfo:
    cursor_info = win32gui.GetCursorInfo()
    cursor_type = cursor_info[1]
    cursor_pos_x, cursor_pos_y = cursor_info[2]
    return CursorInfo(cursor_pos_x, cursor_pos_y, cursor_type)