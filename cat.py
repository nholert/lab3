'''
This program prints stdin to the screen.
'''
import sys

def cat(file):
    chunk_size = 64 * 1024  # 64 KB
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        sys.stdout.buffer.write(chunk)

def flush():
    sys.stdout.buffer.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
                flush()
    else:
        cat(sys.stdin.buffer)
        flush()
