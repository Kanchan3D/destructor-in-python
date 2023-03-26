class destructor_demo:
    def __init__(self):
        print("welcome")
    def __del__(self):
        print("destructor running")
ob1=destructor_demo()
