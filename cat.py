'''
This program prints stdin to the screen.
'''
import sys
import shutil

def cat(file):
    # Stream data in bounded chunks to keep memory usage O(1).
    shutil.copyfileobj(file, sys.stdout.buffer, length=1024 * 1024)
    sys.stdout.buffer.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
