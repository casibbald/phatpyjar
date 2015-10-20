import argparse
import sys


def initialise(name):
    print "Hello {0}".format(name)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subparser_name', help='commands')
runner_parser = subparsers.add_parser('list', help='test')
runner_parser.add_argument('-t', '--test', required=True)
runner_parser.add_argument('-v', '--verbose', required=False)


def runner():
    try:
        if parser.parse_args().verbose:
            print "Initialising Jython jvm {0}".format(sys.version)
            print
        if parser.parse_args().subparser_name == 'list':
            initialise(parser.parse_args().test)
    except:
        pass
        #Deliberately suppressing exception information at this point.

if __name__ == '__main__':
    runner()
else:
    runner()

