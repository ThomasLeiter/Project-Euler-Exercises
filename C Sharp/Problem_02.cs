using System;

class Problem_02{

    class Fibonacci{
        private int a = 1;
        private int b = 1;

        public int next(){
            int t = a;
            a = b;
            b += t;
            return a;            
        }
    }

    static int SumOfEvenFibonacciNumbers(int N){
        int sum = 0;
        var fibonacci = new Fibonacci();
        int next;
        while (true) {
            next = fibonacci.next();
            if (next >= N){
                break;
            } else if (next % 2 == 0){
                sum += next;
            }
        } 
        return sum;
    }

    public static void Solve(){
        var sum = SumOfEvenFibonacciNumbers(4000000);
        Console.WriteLine($"The sum of even fibonacci numbers is {sum}.");
    }

}