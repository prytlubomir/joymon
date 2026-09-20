import sys
import time

import XInput as xi

import gui


def trigger_listener(index, handler, *args, delay=0, select=None, **kwargs):
    print('listener started')
    while True:
        time.sleep(delay)
        values = xi.get_trigger_values(xi.get_state(index))
        if select is not None:
            result = values[select]
        else:
            result = values
        handler(result, *args, **kwargs)
        print('run', result)
    print('listener ended')


def slowprint(*args, d=0.05) -> None:
    time.sleep(d)
    print(*args)


def tui() -> None:
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

    trigger_listener(index, slowprint, d=0.1, select=0)
    

def main():
    if '--gui' in sys.argv:
        gui.start()
    elif '--cli' in sys.argv:
        tui()
    else:
        gui.start()


if __name__ == "__main__":
    main()
