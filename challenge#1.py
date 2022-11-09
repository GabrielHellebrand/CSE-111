from datetime import datetime
now = datetime.now().minute

print(now % 2 == 0)