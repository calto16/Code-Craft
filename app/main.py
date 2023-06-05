import sys
import os
import zlib
import hashlib
def gitInit():
    os.mkdir(".git")
    os.mkdir(".git/objects")
    os.mkdir(".git/refs")
    with open(".git/HEAD", "w") as f:
        f.write("ref: refs/heads/master\n")
def gitCatFile(input):
    # make the git objects path from the input
    path = ".git/objects/" + input[0:2] + "/" + input[2:]
    # read contents -> decompress -> parse the data
    str = open(path, "rb").read()
    raw = zlib.decompress(str)
    data = open(path, "rb").read()
    raw = zlib.decompress(data)
    y = raw.find(b"\x00")
    print(raw[y + 1 :].decode(), end="")
def gitHashObject(path):
    data = open(path, "r").read().encode()  # read data from file
    sz = len(data)
    fmt = "blob".encode()
    header = fmt + b" " + str(sz).encode() + b"\x00"  # make header
    raw = header + data
    hash = hashlib.sha1(raw).hexdigest()  # get hash of all data
    print(hash)
    # persist the data to the objects dir
    dir = os.path.join(".git/objects", hash[0:2])
    if not os.path.exists(dir):
        os.makedirs(dir)
    write_path = os.path.join(dir, hash[2:])
    with open(write_path, "wb") as f:
        f.write(zlib.compress(raw))
def main():
    command = sys.argv[1]
    if command == "init":
        gitInit()
        # print("--completed writing the contents for init")
    elif command == "cat-file":
        gitCatFile(sys.argv[3])
    elif command == "hash-object":
        gitHashObject(sys.argv[3])
    else:
        raise RuntimeError("unimplemented command: {command}")
if __name__ == "__main__":
    main()