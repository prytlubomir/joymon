
import XInput as xi
import time


def main():
    print("Hello from joymon!")

    print("connected controllers:")
    for i, s in enumerate(xi.get_connected()):
        print(f'{i}: {s}')
    
    index = int(input("pick a controller: "))
    
    while True:
        time.sleep(0.1)
        print(xi.get_trigger_values(xi.get_state(index))[0])
    


if __name__ == "__main__":
    main()
