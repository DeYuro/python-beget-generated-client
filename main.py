from client.client import Test
import getopt
import sys


def test_client():
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "l:p:")
    test = Test(opts[0][1], opts[1][1])
    test.run()


if __name__ == '__main__':
    test_client()
