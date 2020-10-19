import argparse
parser = argparse.ArgumentParser('Film ratings')
parser.add_argument('film')
parser.add_argument('stars')
args = parser.parse_args()
with open('args.txt', 'w') as fp: 

print parser.parse_args()
