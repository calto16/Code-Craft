import sys
import os
import zlib

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    
    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/master\n")
        print("Initialized git directory")
    elif command == "cat-file":
        if sys.argv[2] != "-p":
            raise RuntimeError(f"Expected cat-file -p")
        blob_sha = sys.argv[3]
        try:
            blob_content = open(
                f".git/objects/{blob_sha[:2]}/{blob_sha[2:]}", "rb"
            ).read()
        except:
            raise RuntimeError(f"Not a valid object name {blob_sha}")
        data = zlib.decompress(blob_content)
        if data.startswith(b"blob"):
            data = data[data.find(b"\x00") + 1 :]
            print(data.decode("utf-8"), end="")
        else:
            raise RuntimeError(f"Unknown command #{command}")

if __name__ == "__main__":
    main()
