
import XInput as xi
import sys
import time



    
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
