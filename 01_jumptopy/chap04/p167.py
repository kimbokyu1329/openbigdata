import sys
# Run - edit configuration  에서 argv 인자를 설정해 줄 수 있음
args = sys.argv[1:]

for i in args :
    print(i.upper(), end=' ')