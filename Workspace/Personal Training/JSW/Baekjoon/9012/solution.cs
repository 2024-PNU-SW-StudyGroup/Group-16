using System.Text;

StringBuilder sb = new StringBuilder();
using (StreamReader sr = new StreamReader(Console.OpenStandardInput()))
{
    int T = int.Parse(sr.ReadLine());
    for (int i = 0; i < T; i++)
    {
        Stack<char> stack = new Stack<char>();
        bool isVPS = true;
        foreach (var c in sr.ReadLine())
        {
            if (c == '(') stack.Push('(');
            else
            {
                if (stack.Count == 0)
                {
                    isVPS = false;
                    break;
                }
                stack.Pop();
            }
        }
        if (stack.Count != 0) isVPS = false;
        sb.AppendLine(isVPS ? "YES" : "NO");
    }
}

Console.Write(sb);