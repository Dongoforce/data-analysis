def finder(names, alf):
    names.sort()
    result = []
    ind = 0

    for i in names:
        ind += 1
        summa = 0
        for j in i:
            if j in alf:
                summa += alf.index(j) + 1
        result.append(summa * ind)
    return sum(result)

def main():
    try:
        name_file = open('names.txt', 'r')
    except:
        print("File not found")
        return -1

    names = name_file.readline().split(',')

    if len(name_file.read()) > 0:
        print("Wrong structure of file")
        return -1
    name_file.close()

    try:
        alf_file = open('alfavit', 'r')
    except:
        print("File alfavit not found")
        return -1

    alf = alf_file.readline().split(' ')
    alf_file.close()

    print(finder(names, alf))

if __name__ == '__main__':
    main()