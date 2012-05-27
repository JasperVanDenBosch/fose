import sys, argparse
import pkg_resources
import fose.tests


def main():
    description='Core package of Framework for Open Science Evaluation.'
    parser = argparse.ArgumentParser(description)
    parser.add_argument('--test', action='store_true',help='Run unit tests.')
    args = parser.parse_args()
    if args.test:
        fose.tests.runall()

version = pkg_resources.get_distribution("fose").version
