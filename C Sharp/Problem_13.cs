using System;

class Problem_13{

    /*
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    (see file)
    */

    static string Reverse(string str){
        char[] charArray = str.ToCharArray();
        Array.Reverse( charArray );
        return new string( charArray );    
    }

    static string SchoolBookAddition(string lhs, string rhs){
        if (rhs.Length > lhs.Length){
            return SchoolBookAddition(rhs, lhs);
        }
        lhs = Reverse(lhs);
        rhs = Reverse(rhs);
        string result = "";
        int carry = 0;
        int i = 0;
        for (; i < rhs.Length; ++i){
            int digit = rhs[i] - '0' + lhs[i] - '0' + carry;
            carry = digit / 10;
            digit %= 10;
            result += digit;
        }
        for (; i < lhs.Length; ++i){
            int digit = lhs[i] - '0' + carry;
            carry = digit / 10;
            digit %= 10;
            result += digit;
        }
        if (carry > 0){
            result += carry;
        }
        return Reverse(result);
    }

    static string SumOfNumbers(string filename){
        string sum = "";
        foreach (string number in System.IO.File.ReadLines(filename)){
            sum = SchoolBookAddition(sum,number);
        }
        return sum;
    }

    public static void Solve(){
        string filename = "Problem_13_numbers.txt";
        string sum = SumOfNumbers(filename);
        Console.WriteLine($"The sum of all numbers is {sum}.");
        Console.WriteLine($"The first 10 digits are therefore {sum.Substring(0,10)}.");        
    }

}