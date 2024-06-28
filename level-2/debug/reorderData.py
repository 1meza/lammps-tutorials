def sortData (data: str) -> str:
    sorted_data = sorted(data, key=lambda x: x[2])
    return sorted_data

def readDataFromFile (filename: str) -> str:
    data = []
    start_reading = False
    with open(filename, 'r') as file:
        for line in file:
            if 'Atoms # full' in line:
                start_reading = True
                continue
            if start_reading and line.strip():
                data.append(list(map(float, line.split())))
    return data

def writeDataToFile (filename: str, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(' '.join(map(str, line)) + '\n')



def main():
    data = readDataFromFile('old-mix.data')
    sorted_data = sortData(data)
    writeDataToFile('old-sorted.data', sorted_data)

if __name__ == '__main__':
    main()
