import os, sys
try:
    __import__("update2").main()
except Exception as e:
    exit(str(e))
