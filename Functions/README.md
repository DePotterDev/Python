## Collection of everything about Python, tutorials, documentation, tests, ect. 

- enumerate

- with construct (functions: open.py, with.py)
    An important context manager able of opening and closing programs.
    Problems with managing resources in Python
    - **external resources**, such as files, locks and network connections. It is possible to keep using those resources forever, without ever closing them creating a memory leak.
    - database keeps creating new connections without releasing or reusing them.
    - writing text to files is a buffered operation. Calling .write() will create a temporary buffer. Youĺl need the .close() at the end.
    - the app can run into errors or exceptions, causing the control flow to bypass the code responible for releasing the resource.

    In Python, you can use two general approaches to deal with resource management. You can wrap your code in:
    - A try … finally construct
    - A with construct


