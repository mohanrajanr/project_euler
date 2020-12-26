import os
import argparse

current_pwd = ''


def main():
    parser = argparse.ArgumentParser(prog="Problem Spec Creator",
                                     description="Create Files & Folders for Problems")
    parser.add_argument('problem_number', type=int, help='Enter the Problem Name')
    print(parser.parse_args())

if __name__ == '__main__':
    main()