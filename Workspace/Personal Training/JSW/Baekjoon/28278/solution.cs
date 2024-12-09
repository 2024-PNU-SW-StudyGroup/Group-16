using System;
using System.Text;
using System.Collections.Generic;
using System.IO;


public class Program
{
    public static void Main()
    {
        MyStack<string?> stack = new ();
        StringBuilder sb = new StringBuilder();
        using (var sr = new StreamReader(Console.OpenStandardInput())) 
        {
            int N = int.Parse(sr.ReadLine());

            for (int i = 0; i < N; i++)
            {
                var line = sr.ReadLine().Split(' ');
                switch (line[0])
                {
                    case "1":
                        stack.Push(line[1]);
                        break;
                    case "2":
                        sb.AppendLine(stack.Pop() ?? "-1");
                        break;
                    case "3":
                        sb.AppendLine(stack.Count.ToString());
                        break;
                    case "4":
                        sb.AppendLine(stack.IsEmpty() ? "1" : "0");
                        break;
                    case "5":
                        sb.AppendLine(stack.Peek() ?? "-1");
                        break;
                }
            }
        }
        

        Console.Write(sb);
    }
}

public class Node<T>
{
    public T Value { get; set; }
    public Node<T>? Next { get; set; }
    public Node(T value, Node<T>? next = null)
    {
        Value = value;
        Next = next;
    }
}

public class MyStack<T>
{
    private Node<T>? Top { get; set; }
    public int Count { get; private set; }

    public MyStack()
    {
        Top = new Node<T>(default, null);
        Count = 0;
    }

    public void Push(T value)
    {
        Top = new Node<T>(value, Top);
        Count++;
    }

    public bool IsEmpty()
    {
        return Count == 0;
    }

    public T? Pop()
    {
        if (IsEmpty()) return default;
        T value = Top!.Value;
        Top = Top.Next;
        Count--;
        return value;
    }

    public T? Peek()
    {
        return IsEmpty() ? default : Top!.Value;
    }
}
