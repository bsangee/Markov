import csv

class parser:
        def __init__(self):
                self.timestamp= []
                self.read_bytes=[]
                self.write_bytes=[]
                self.stripe_count=[]

        def parse_file(self):
                with open('hacc.csv', 'r') as f:
                        for line in f.readlines():
                                time,read, write, stripe = line.strip().split(',')
                                self.timestamp.append(time)
                                self.read_bytes.append(read)
                                self.write_bytes.append(write)
                                self.stripe_count.append(stripe)

