from threading import Thread

from tkinter import VERTICAL, Tk
from tkinter.ttk import Label, Progressbar, Style

import main


def input_handler(values, lt, ltv, rt, rtv):
    lt_value = round(values[0]*100)
    rt_value = round(values[1]*100)

    ltv['text'] = f"{lt_value}%"
    rtv['text'] = f"{rt_value}%"

    lt['value'] = lt_value
    rt['value'] = rt_value
    

def setup_gui():
    root = Tk()
    root.title("Joymon")
    root.wm_resizable(False, False)
    root.configure(background="black")
        
    
    BRAKE_TROUGH_COLOR = 'black'
    BRAKE_BAR_COLOR = 'green'
    
    brakeBarStyle = Style()
    brakeBarStyle.theme_use('clam')
    brakeBarStyle.configure("brake.Horizontal.TProgressbar", troughcolor=BRAKE_TROUGH_COLOR, 
                    bordercolor=BRAKE_BAR_COLOR, background=BRAKE_BAR_COLOR, lightcolor=BRAKE_BAR_COLOR, 
                    darkcolor=BRAKE_BAR_COLOR, padding=0)
    
    THROTTLE_TROUGH_COLOR = 'black'
    THROTTLE_BAR_COLOR = 'red'
    
    throttleBarStyle = Style()
    throttleBarStyle.theme_use('clam')
    throttleBarStyle.configure("throttle.Horizontal.TProgressbar", troughcolor=THROTTLE_TROUGH_COLOR, 
                    bordercolor=THROTTLE_BAR_COLOR, background=THROTTLE_BAR_COLOR, lightcolor=THROTTLE_BAR_COLOR, 
                    darkcolor=THROTTLE_BAR_COLOR, troughrelief="flat")
    
    
    lt = Progressbar(root, style="brake.Horizontal.TProgressbar", orient=VERTICAL, length=200, mode='determinate', value=50)
    rt = Progressbar(root, style="throttle.Horizontal.TProgressbar", orient=VERTICAL, length=200, mode='determinate', value=70)
    
    ltl = Label(root, foreground="white", background="black", text="Left trigger: ")
    rtl = Label(root, foreground="white", background="black", text="Right trigger: ")
    
    ltv = Label(root, foreground="white", background="black", text="0%")
    rtv = Label(root, foreground="white", background="black", text="0%")
    
    
    labels_row = 0
    values_row = 1
    bars_row = 2
    
    ltl.grid(row=labels_row, column=0, padx=5, pady=5)
    rtl.grid(row=labels_row, column=1, padx=5, pady=5)
    
    ltv.grid(row=values_row, column=0, padx=5, pady=2)
    rtv.grid(row=values_row, column=1, padx=5, pady=2)
    
    lt.grid(row=bars_row, column=0, padx=5, pady=5)
    rt.grid(row=bars_row, column=1, padx=5, pady=5)
    
    # Button(root, text='Start', command=bar).grid(pady=10)
    # root.mainloop()
    
    return root, lt, ltv, rt, rtv


def start():
    root, *widgets = setup_gui()

    thr_listen = Thread(
        target=main.trigger_listener, 
        args=[0, input_handler, *widgets], 
        kwargs={'delay': 0.01},
        daemon=True
    )
    thr_listen.start()
    
    root.mainloop()

    thr_listen.join(timeout=0)


if __name__ == "__main__":
    start()
