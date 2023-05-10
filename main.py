import atexit
import threading
import webview
import cursor
from constants import CURSOR
from constants import WINDOW
from utils import get_cursor


initial_cursor = get_cursor()
window = webview.create_window(
    title="Ipad Cursor",
    url="res/index.html",
    width=WINDOW.WIDTH,
    height=WINDOW.HEIGHT,
    x=initial_cursor.x - (WINDOW.WIDTH // 2) - CURSOR.OFFSET_X,
    y=initial_cursor.y - (WINDOW.HEIGHT // 2) - CURSOR.OFFSET_Y,
    transparent=True,
    frameless=True,
    on_top=True
)

last_cursor = None
def update_loop():
    global last_cursor
    
    while True:
        cursor = get_cursor()
        
        target_x = cursor.x - (WINDOW.WIDTH // 2) - CURSOR.OFFSET_X
        target_y = cursor.y - (WINDOW.HEIGHT // 2) - CURSOR.OFFSET_Y
        
        window.move(target_x, target_y)
        
        if last_cursor != cursor.type:
            cursor_str = CURSOR.CURSORS[cursor.type] if cursor.type in CURSOR.CURSORS else "other"
            window.load_url(f"{window.original_url}#{cursor_str}")
            last_cursor = cursor.type
            
if __name__ == "__main__":
    cursor.install()
    atexit.register(cursor.uninstall)
    webview.start(
        http_server=True,
        func=lambda: threading.Thread(target=update_loop).start()
    )