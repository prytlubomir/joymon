
from tkinter import Tk, VERTICAL
from tkinter.ttk import Progressbar, Label, Style
import XInput as xi
import sys
import time



def gui():
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
    root.mainloop()


# def bar():
#     for value in (20, 40, 50, 60, 80, 100):
#         progress['value'] = value
#         root.update_idletasks()
#         time.sleep(1)


def slowprint(*args, d=0.05) -> None:
    time.sleep(d)
    print(*args)


def main() -> None:
    slowprint("Hello from joymon!")

    detected: list[int] = []
    selected: int | None = None

    while selected is None:
        slowprint("\nconnected controllers:\n")
        for i, s in enumerate(xi.get_connected()):
            if s:
                detected.append(i)
                slowprint(f'    {i}: {s}')
                
        slowprint('\nenter "q" to exit')
        command = input("pick a controller: ")
        
        if command == "q":
            sys.exit()
        if not command.isnumeric():
            slowprint(f'\n -- ERROR: invalid command "{command}"')
            continue
            
        index = int(command)
        
        if index in detected:
            selected = index
        else:
            slowprint(f"\n -- ERROR: controller {index} not found. Please try again.")
    
    while True:
        slowprint(xi.get_trigger_values(xi.get_state(index))[0], d=0.1)
    


if __name__ == "__main__":
    main()
