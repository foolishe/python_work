from unit11 import *
import doctest

TEST_FILE = 'Tombola_test.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'


def main(argv):

    verbose = '-v' in argv
    real_subclasses = Tombola.__subclasses__()
    virtual_subclasses = list(Tombola._abc_registry)
    # have issue here,i don't know how to get the registry subclass

    for cls in real_subclasses + virtual_subclasses:
        test(cls,verbose)


def test(cls, verbose=False):
    print(1)
    res = doctest.testfile(
        TEST_FILE,
        globs = {'ConcreteTombola': cls},
        verbose = verbose,
        optionflags = doctest.REPORT_ONLY_FIRST_FAILURE)
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__,res,tag))

if __name__ == '__main__':
        import sys
        main(sys.argv)
