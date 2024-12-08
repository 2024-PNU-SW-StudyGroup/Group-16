long fact(long n)
{
    if (n == 0) return 1;
    return n * fact(n - 1);
}

int N = int.Parse(Console.ReadLine ());
Console.WriteLine(fact(N));