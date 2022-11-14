import time
from pageobjmodel.loginpage import Homepage
h = Homepage('driver')
h.chrome1()
time.sleep(3)
h.visit()
time.sleep(3)
h.username()
time.sleep(2)
h.password()
time.sleep(3)
h.submit()
time.sleep(2)
h.closed()
