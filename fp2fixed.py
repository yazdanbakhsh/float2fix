#!/usr/bin/python

# Amir Yazdanbakhsh
import sys
import math

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
pass

def usage():
	print bcolors.FAIL + "Usage: python fp2fixed.py [fixed point value] [number of integer bits] [number of fraction bits]" + bcolors.ENDC
	exit(1)
pass


def main():
	if(len(sys.argv) < 3):
		usage()

	fpval = float(sys.argv[1])
	nint  = int(sys.argv[2])
	nfrac = int(sys.argv[3])

	res = float(round(fpval * math.pow(2.0, nfrac))) / float(math.pow(2.0, nfrac))

	if(res > math.pow(2.0, nint)):
		res = math.pow(2.0, nint) - 1 + (math.pow(2.0, nfrac) - 1.0) / (math.pow(2.0, nfrac))

	print bcolors.OKGREEN + "FloatingPoint = %f" % (fpval) + bcolors.ENDC
	print bcolors.OKGREEN + "FixedPoint(Qm.f)[%d:%d] = %f" % (nint,nfrac,res) + bcolors.ENDC
	print bcolors.FAIL + "Abs Difference: %.2f" % ((abs(fpval - res) / float(fpval))) + bcolors.ENDC
pass
if __name__ == "__main__":
	main()