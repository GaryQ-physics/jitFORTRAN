# https://stackoverflow.com/questions/37067414/python-import-multiple-times

def foo():
    print("before importing module")
    import testmodule
    reload(testmodule)
    testmodule.dummy()
    print("after importing module")
    #del testmodule

if __name__ == '__main__':
    foo()
    foo()

# in python 3.4, need    from importlib import reload     see:
# https://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module
