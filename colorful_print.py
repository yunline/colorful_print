USE_COLOR=1#是否启用彩色（防止在某些无法转义彩色的控制台显示异常）
DISPLAY_MODE={#被注释掉的显示模式似乎在vscode中无法使用
    "default":0,
    "bold":1,
    "underlined":4,
    #"blink":5,
    "inverse_color":7,
    #"!bold":22,
    #"!underlined":24,
    #"!blink":25,
    #"!inverse_color":27
    }

COLOR={#这里记录的是前景色，背景色则要加10
    "black":30,
    "red":31,
    "green":32,
    "yellow":33,
    "blue":34,
    "carmine":35,
    "cyan":36,
    "white":37
}

def set_color(dm="",fg="",bg=""):
    #dm: display mode
    #fg: foreground
    #bg: background
    #不填参数就是重置为默认值
    if dm:dm=str(DISPLAY_MODE[dm])
    else:dm="0"
    if fg:fg=";"+str(COLOR[fg])
    if bg:bg=";"+str(COLOR[bg]+10)

    print("\033[%s%s%sm"%(dm,fg,bg),end="")

def c_print(*args,dm="",fg="",bg="",**kwargs):
    if USE_COLOR:set_color(dm,fg,bg)
    print(*args,**kwargs)
    if USE_COLOR:set_color()

def c_input(arg,dm="",fg="",bg=""):
    if USE_COLOR:set_color(dm,fg,bg)
    print(arg,end="")
    if USE_COLOR:set_color()
    out=input()

'''
#使用例
print("\n")
print("hello_world")
for i in DISPLAY_MODE:
    for j in COLOR: 
        c_print("hello_world",dm=i,fg=j)
set_color()

c_input("\n我是红色的吗？\n>>>",fg="red")
'''