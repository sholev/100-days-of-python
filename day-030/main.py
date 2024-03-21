try:
    try:
        # file = open("none.txt")
        print({"": ""}["none"])
    except FileNotFoundError as e:
        print(e)
    except KeyError as e:
        print(f"No key {e} found.")
    else:
        print("No exception")
    finally:
        print("Do regardless")
        raise Exception("Base exception")
except Exception as e:
    print(e)
