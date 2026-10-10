import sys

def cat(file_obj, chunk_size: int = 8192):
    """
    Stream the contents of *file_obj* to stdout using a fixed-size buffer.

    Args:
        file_obj: A binary‑readable file‑like object (e.g. an open file or
                  sys.stdin.buffer).
        chunk_size: Number of bytes to read per iteration. 8 KB is a good
                    default for most workloads.
    """
    while True:
        data = file_obj.read(chunk_size)
        if not data:          # EOF reached
            break
        sys.stdout.buffer.write(data)

if __name__ == "__main__":
    # If file names are given, process each sequentially.
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        # No arguments → read from standard input.
        cat(sys.stdin.buffer)
