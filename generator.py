import csv
import random
import datetime
import timeit
import argparse


class Argparser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.init_parser()

    def init_parser(self):
        parser = self.parser
        parser.add_argument("-i", "--integers", help="how many integer value do you want to generate")
        parser.add_argument("-ri", "--range-integer", help="describe range of integer")
        parser.add_argument("-vc", "--varchars", help="how many varchar value do you want to generate")
        parser.add_argument("-t", "--texts", help="how many text value do you want to generate")
        parser.add_argument("-dt", "--dates", help="how many datetime value do you want to generate")
        parser.add_argument("-d", "--doubles", help="how many double value do you want to generate")
        parser.add_argument("-r", "--rows", help="describe number of rows")
        parser.add_argument("-o", "--output", help="describe file name")
        self.parser = parser


class Generator:
    def __init__(self, args):
        self.rows = int(args.rows) if args.rows else 1000
        self.filename = args.output if args.output else "out.csv"
        self.integers = int(args.integers) if args.integers else 5
        self.varchars = int(args.varchars) if args.varchars else 5
        self.texts = int(args.texts) if args.texts else 5
        self.doubles = int(args.doubles) if args.doubles else 5
        self.dates = int(args.dates) if args.dates else 1
        self.text_pool = ['Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity \
in the Amazon Web Services (AWS) cloud. Using Amazon EC2 eliminates your need to invest \
in hardware up front so you can develop and deploy applications faster. You can use Amazon EC2 \
to launch as many or as few virtual servers as you need configure security and networking and manage storage. \
Amazon EC2 enables you to scale up or down to handle changes in requirements or spikes in popularity reducing \
your need to forecast traffic.',
                          'First you need to get set up to use Amazon EC2. After you are set up you are ready \
to complete the Getting Started tutorial for Amazon EC2. Whenever you need more information about an Amazon EC2 feature\
you can read the technical documentation.',
                          'You can provision Amazon EC2 resources such as instances and volumes \
directly using Amazon EC2. You can also provision Amazon EC2 resources using other services in AWS. \
For more information see the following documentation:',
                          'If you prefer to build applications using language-specific APIs\
 instead of submitting a request over HTTP or HTTPS AWS provides libraries sample code tutorials and other resources \
 for software developers. These libraries provide basic functions that automate tasks such as cryptographically \
 signing your request set trying requests and handling error responses making it is easier for you to get started.\
  For more information see AWS SDKs and Tools.']
        self.word_pool = self.text_pool[0].split()

    def generate(self):
        f = open(self.filename, 'w', encoding='utf-8', newline='')
        wr = csv.writer(f)
        for i in range(0, self.rows):
            idx = [i + 1]
            val_ints = []
            val_varchars = []
            val_texts = []
            val_doubles = []
            val_dates = []

            for j in range(0, self.integers):
                val_ints.append(random.randrange(0, 10000))
            for j in range(0, self.varchars):
                val_varchars.append(random.choice(self.word_pool))
            for j in range(0, self.texts):
                val_texts.append(random.choice(self.text_pool))
            for j in range(0, self.dates):
                val_dates.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            for j in range(0, self.doubles):
                val_doubles.append(random.random())
            wr.writerow(idx + val_ints + val_varchars + val_texts + val_dates + val_doubles)
        f.close()


if __name__ == "__main__":
    parser = Argparser()
    args = parser.parser.parse_args()
    print("Generating file...")
    start = timeit.default_timer()
    generator = Generator(args)
    generator.generate()
    stop = timeit.default_timer()
    print(generator.filename + " is created. ")
    print("It took " + str(stop - start) + " seconds to generate data.")

