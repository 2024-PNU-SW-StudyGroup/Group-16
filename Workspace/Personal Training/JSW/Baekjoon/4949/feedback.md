# solution.cs
- Dictionary를 초기화 하는 방법:
    ```cs
    new Dictionary<,> () {
        {,},
        {,},
        {,}
    }
    ```
# solutoin.py
- Python에서 빠른 입출력:
    ```py
    import sys

    sys.stdin.read().splitlines()
    sys.stdin.readline().strip('\n')
    ```
# Main.java
- Hashtable보다는 HashMap 사용을 권장. (Hashtable은 레거시 클래스)
- Dictionary는 인터페이스. Dictionary<,> = new HashMap<,> (); 로 정의하면 Dictionary 인터페이스 메서드만 사용할 수 있음.
- HashTable을 초기화 하는 방법:
    ```java
    new HashMap<,>() {
        put(,);
        put(,);
    }
    ```
- Java에서 빠른 입출력:
    ```java
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    br.readLine();
    ```
