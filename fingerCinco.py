from encoder import encoder
from decoder import decoder
import sys

def main():
	encoder(sys.argv[1])
	decoder(sys.argv[1])
main()