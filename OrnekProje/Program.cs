using System;

class Program
{
    static void Main()
    {
        Func<int, int, int> topla = (a, b) => a + b;
        Console.WriteLine(topla(3, 4));
    }
}
