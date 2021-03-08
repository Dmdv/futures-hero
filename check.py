import time
from termcolor import colored

def entry_condition():
    import heikin_ashi
    print("DIRECTION")
    heikin_ashi.get_hour(6)
    heikin_ashi.get_hour(1)
    print()
    print("STRENGTH OF CANDLE")

    if heikin_ashi.strength_of("6HOUR") == "STRONG": print(colored("CURRENT 6 HOUR   :   STRONG", "green"))
    else: print(colored("CURRENT 6 HOUR  :   STRONG", "red"))
    if heikin_ashi.strength_of("1HOUR") == "STRONG": print(colored("CURRENT 1 HOUR   :   STRONG", "green"))
    else: print(colored("CURRENT 1 HOUR  :   STRONG", "red"))

    from binance_futures import get_volume
    previous_volume = get_volume("PREVIOUS", "1HOUR")
    current_volume  = get_volume("CURRENT", "1HOUR")
    if (previous_volume / 5) < current_volume:
        print(colored("VOLUME ENTRY     :   YES", "green"))
    else: print(colored("VOLUME ENTRY     :   NO", "red"))
    if heikin_ashi.pattern_broken("1HOUR") == "BROKEN": print(colored("1 HOUR PATTERN   :   BROKEN", "red"))

def check():
    print("What do you want to check? ")
    print("1. entry condition")
    print("2. minute")
    print("3. position")
    print("4. realizedPNL")
    input_num = input("\nEnter a number   :   ")

    if (input_num == '1'):
        start = time.time()
        entry_condition()
        print(f"Time Taken: {time.time() - start} seconds")

    elif (input_num == '2'):
        import heikin_ashi
        loop = input("Do you want to loop? [Y/n]") or 'n'
        if loop == 'Y':
            while True:
                heikin_ashi.get_current_minute(1)
                print()
                time.sleep(3)
        else:
            start = time.time()
            heikin_ashi.get_current_minute(1)
            print(f"Time Taken: {time.time() - start} seconds")

    elif (input_num == '3'):
        start = time.time()
        from get_position import get_position_info
        print("\nThe <get_position.py> return value is : " + get_position_info())
        print(f"Time Taken: {time.time() - start} seconds")

    else: import get_realizedPNL
    print()
try: check()
except KeyboardInterrupt: print("\n\nAborted.\n")
