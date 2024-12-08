using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

Dictionary<char, char> wordPairs = new Dictionary<char, char>() {
    {'(', ')'},
    {'[', ']'},
    {'{', '}'}
};
Stack<char> stack = new Stack<char>();
bool isVPS(string str)  
{
    stack.Clear();
    foreach (char c in str)
    {
        if (wordPairs.ContainsKey(c)) stack.Push(c);
        if (wordPairs.ContainsValue(c))
        {
            if (stack.Count == 0) return false;
            var last = stack.Pop();
            if (wordPairs[last] != c) return false;
        }
    }

    return stack.Count == 0 ? true : false;
}

StringBuilder sb = new StringBuilder();
using (StreamReader sr = new StreamReader(Console.OpenStandardInput()))
{
    string line;
    while ((line = sr.ReadLine()) != ".")
    {
        sb.AppendLine(isVPS(line) ? "yes" : "no");
    }
}
Console.Write(sb);