def main():
    hits_file = open('hits.txt', 'r')
    hits = []
    counter = []

    while True:
        try:
            a = hits_file.readline().split('\t')[1]
        except:
            break
        if a in hits:
            counter[hits.index(a)] += 1
        else:
            hits.append(a)
            counter.append(1)
    hits_file.close()

    for i in range(5):
        temp_ip = hits[counter.index(max(counter))]
        temp_count = max(counter)
        hits.remove(temp_ip)
        counter.remove(temp_count)
        print(temp_ip, "---->", temp_count)



if __name__ == '__main__':
    main()