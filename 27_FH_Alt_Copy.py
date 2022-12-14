def  copyOddNumberedLines(file_in, file_out):
    print("\nCopying alternate lines from \'{}\' to \'{}\'...".format(file_in, file_out))
    try:
        fh_in = open(file_in, 'r')
        fh_out = open(file_out, 'w')
        lines = fh_in.readlines()
        for i in range(0, len(lines), 2):
            fh_out.write(lines[i])
        print('Done!\n')
    except FileNotFoundError:
        print('Error: \'{}\' not found.\n'.format(file_in))

if __name__ == "__main__":

    copyOddNumberedLines('file1.txt', 'file2.txt')