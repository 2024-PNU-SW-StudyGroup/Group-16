MyStack<int> stack = new MyStack<int>();
using (StreamReader sr = new StreamReader(Console.OpenStandardInput()))
{
    int K = int.Parse(sr.ReadLine());
    for (int i = 0; i < K; i++)
    {
        int temp = int.Parse(sr.ReadLine());
        if (temp == 0)
        {
            stack.Pop();
            continue;
        }

        stack.Push(temp);
    }
}

int result = 0;
while (!stack.IsEmpty())
{
    result += stack.Pop();
}

Console.WriteLine(result);


public class Node<T>
{
    public T? Value;
    public Node<T>? Next;

    public Node(T? value, Node<T>? next = null)
    {
        Value = value;
        Next = next;
    }
}

public class MyStack<T>
{
    private Node<T>? _top;

    public int Count { get; private set; }

    public MyStack()
    {
        _top = new Node<T>(default(T), null);
        Count = 0;
    }

    public void Push(T value)
    {
        var temp = new Node<T>(value, _top);
        _top = temp;
        Count++;
    }

    public T? Pop()
    {
        if (IsEmpty())
            return default(T);
        var temp = _top.Value;
        _top = _top.Next;
        Count--;
        return temp;
    }

    public T? Peek()
    {
        if (IsEmpty())
            return default(T);
        return _top.Value;
    }

    public bool IsEmpty() => Count == 0;

}