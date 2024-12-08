Date: 2024.12.04
Tags: #Python, #Generator, #product 

# Problem
itertools의 product를 사용하면서 문제가 발생하였다.
```python
dir_map = product(range(3), repeat=2)
for dy, dx in dir_map:
    pass
```
재귀 함수 내부에 있는 for문이 9번만 돌고 꺼져버렸다.

# Cause
`product`는 generator이므로 생성한 결과를 다 소진하게 되면 비어버린다.
`len(dir_map)`가 9이므로, for문이 정확하게 9번 돌고 멈춰버리게 된다.

# Solution
만약 product의 결과값을 재사용하고 싶다면, `list(product())`처럼 generator에서 list로 만들어줘야한다.