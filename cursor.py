import winreg

cursor_theme = "Ipad Dynamic"

def install():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Cursors", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(key, "Scheme", 0, winreg.REG_SZ, cursor_theme)

    winreg.SetValueEx(key, "Arrow", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "AppStarting", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "Crosshair", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "Hand", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "Help", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "IBeam", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "No", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "NWPen", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "SizeAll", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "SizeNESW", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "SizeNS", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "SizeNWSE", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "SizeWE", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "UpArrow", 0, winreg.REG_SZ, cursor_theme)
    winreg.SetValueEx(key, "Wait", 0, winreg.REG_SZ, cursor_theme)

    winreg.CloseKey(key)

def uninstall():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Cursors", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(key, "Scheme", 0, winreg.REG_SZ, "Windows Default (system scheme)")

    winreg.SetValueEx(key, "Arrow", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "AppStarting", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "Crosshair", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "Hand", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "Help", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "IBeam", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "No", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "NWPen", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "SizeAll", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "SizeNESW", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "SizeNS", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "SizeNWSE", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "SizeWE", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "UpArrow", 0, winreg.REG_SZ, None)
    winreg.SetValueEx(key, "Wait", 0, winreg.REG_SZ, None)

    winreg.CloseKey(key)