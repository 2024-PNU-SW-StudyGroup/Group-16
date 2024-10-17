# 학습 내용 정리
- 
# 회고
## 1. 특정 조건을 리스트 안에서 체크해야하는 경우
### any
```python
def any(iterable):
	for element in iterable:
    	if element:
        	return True
    return False
```
### all
```python
def all(iterable):
	for element in iterable:
    	if not element:
        	return False
    return True
```
## 2. object들의 비교 연산
처음에 `1 == True`의 결과를 False라고 생각했었다. python에서는 모든 데이터가 object이고, 다른 언어에서 `object == object` 연산은 object의 메모리 주소를 비교하는 연산이기 때문에 True일 수가 없다고 생각했었다.

Python docs의 [truth testing procedure](https://docs.python.org/3/library/stdtypes.html#truth)를 확인해보면 "모든 오브젝트는 특정 조건을 제외하고 True로 평가된다"라고 적혀있다.
특정 조건은 다음과 같다.
> unless its class defines either a __bool__() method that returns False or a __len__() method that returns zero

False로 간주되는 built-in object는 다음과 같다.
- constants defined to be false: None and False
- zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
- empty sequences and collections: '', (), [], {}, set(), range(0)

이때까지 python에서 boolean을 사용할 때 항상 조심했었는데, 앞으로는 좀 더 믿고 쓸 수 있겠다.
```python
n = 1
if n%2:
    pass
else:
    pass
```