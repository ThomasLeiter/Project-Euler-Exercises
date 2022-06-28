using System;

class Problem_01{

    /*
    If we list all the natural numbers below 10 that are 
    multiples of 3 or 5, we get 3, 5, 6 and 9. 
    The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    */

    static int SumOfMultiples(int N, int[] divisors){
        int Sum = 0;
        for (int i = 1; i < N; ++i){
            foreach (int divisor in divisors){
                if (i % divisor == 0){
                    Sum += i;
                    break;
                }
            }
        }
        return Sum;
    }

    public static void Solve(){
        int N = 1000;
        int[] divisors = {3,5};
        var Sum = SumOfMultiples(N, divisors);
        Console.WriteLine($"The Sum of Multiples of {divisors} is {Sum}.");
    }

}


