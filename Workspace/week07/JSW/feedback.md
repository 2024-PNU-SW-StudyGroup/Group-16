# python에서 EOF 처리
## sol1. input()을 사용하는 경우
input()을 사용하여 입력을 처리하는 경우 EOF 시 EOFError를 raise하므로, try-except로 검출해낼 수 있다.
```python
while True:
    try:
        # body
    except EOFError:
        break
```
## sol2. sys.stdin.readline()을 사용하는 경우
sys.stdin.readline()은 EOF일 때 ''을 반환한다.
```python
while (line := sys.stdin.readline()) != '':
```