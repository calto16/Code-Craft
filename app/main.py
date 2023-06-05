import sys
import os
import zlib
def main():
    print("Now in the main() function")
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
    y = raw.find(b"\x00")
    print(raw[y + 1 :].decode(), end="")
def main():
    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/master\n")
        print("--completed writing the contents for init")
        gitInit()
        # print("--completed writing the contents for init")
    elif command == "cat-file":
        gitCatFile(sys.argv[3])
    else:
        raise RuntimeError("unimplemented command: {command}")
if __name__ == "__main__":
    main()