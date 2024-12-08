Stack<int> stack = new Stack<int>();
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
while (stack.Count != 0)
{
    result += stack.Pop();
}
Console.WriteLine(result);