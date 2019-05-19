# PythonbusyThreadingMIMEServer  Best for Server in background
Python Threading MIME Server Example

class MIMEServerThread(threading.Thread):
    
    def __init__(self):
        self.busy = False        
        threading.Thread.__init__(self)

    def run(self):

Code to check busy False before next Thread
