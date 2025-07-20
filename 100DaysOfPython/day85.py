import argparse

parser = argparse.ArgumentParser()

parser.add_argument('url',help='URL to download')
parser.add_argument('output',help='Name of file')

args = parser.parse_args()

print(args)
