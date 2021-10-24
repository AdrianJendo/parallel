import sys

# Use
#   alias factorTree='cd ~ && cd rootdir-scripts && cd factorTree && f(){pipenv run python3 factorTree.py "$1"; unset -f f; cd ~;}; f'
# to run from terminal


def parallelOperation():
    args = sys.argv
    if len(args) < 3:
        print("Need at least 2 operators")
    else:
        numArgs = args[1:]
        sum = 0
        for arg in numArgs:
            temp = float(arg)
            sum += 1 / temp

        print(1 / sum)

    return args


parallelOperation()
