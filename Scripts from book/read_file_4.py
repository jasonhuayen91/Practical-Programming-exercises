import sys
import urllib

def process_file(reader):
    '''Read and print the contents of reader.'''
    
    for line in reader:
        line = line.strip()
        print line
        
    if __name__ == "__main__":
        webpage = urllib.urlopen(sys.argv[1])
        process_file(webpage)
        webpage.close()