import os
import random
import heapq

'''
f.read() ->  read the whole file
f.readline() -> read a single line. If you call this fcn again, it will read the next line
f.readlines() -> return all lines in the file as a list. == .split('\n')

f.write(str) -> write a single string
f.writelines(list) -> write strings in the list
    txt = ['hello', 'world']
        >>> helloworld
    txt = ['hello\n', 'world']
        >>> hello
            world
'''


def createUnsortedLargeData(test_filename, total_size):
    path = f"./testFiles/{test_filename}"
    filename = path + f"/{test_filename}.txt"
    # check if such file does not exist yet
    file_exist = os.path.isfile(filename)
    if file_exist:
        file_size = os.path.getsize(filename)
        if file_size != 0:
            print("such test file already exists")
            return
    else:
        if not os.path.isdir(path):
            os.mkdir(path)
    with open(filename, 'w') as f:
        for x in range(total_size):
            f.write(str(random.randint(0, 10000)) + '\n')
        print("new test file created")


def createSortedChunks(test_filename, chunk_size, whlie=None):
    filename = f"./testFiles/{test_filename}/{test_filename}.txt"
    with open(filename, 'r') as f:
        i = 1
        while True:
            temp_name = f"./testFiles/{test_filename}/chunk{str(i) + '_' + test_filename}.txt"
            temp_list = []
            for _ in range(chunk_size):
                item = f.readline()
                if item == '':
                    break
                heapq.heappush(temp_list, int(item))
            if len(temp_list) == 0:
                break
            with open(temp_name, 'w') as chunk:
                while temp_list:
                    temp = str(heapq.heappop(temp_list)) + '\n'
                    chunk.write(temp)
            i += 1
        print(f"total {i-1} chunks are created")


def main():
    total_size = 10000
    test_filename = 'testLarge'
    chunk_size = 1000
    createUnsortedLargeData(test_filename, total_size)
    createSortedChunks(test_filename, chunk_size)


if __name__ == "__main__":
    main()
