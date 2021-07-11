using System;

namespace CSharp1
{
    class Program
    {
        static void Main(string[] args)
        {

            //Console.WriteLine("Hello World!");
            //int[] nums = new int[] { -4, -1, 0, 3, 10 };
            //int[] renm;
            //renm = SortedSquares(nums);
            //Console.Write("[" + renm[0]);
            //for (int i=1;i<renm.Length;i++)
            //{
            //    Console.Write("," + renm[i]);
            //}
            //Console.Write("]");
            //Console.WriteLine();
            //Console.Write("[" + nums[0]);
            //for (int i = 1; i < nums.Length; i++)
            //{
            //    Console.Write("," + nums[i]);
            //}
            //Console.Write("]");
            //Console.WriteLine();

            //Rotate(nums,2);
            //Console.Write(2%2);
            //Console.Write(2%3);
            //Console.Write(2%4);
            //Console.Write(3%2);

        }

        public static int[] SortedSquares(int[] A)
        {
            int n = A.Length;
            int[] result = new int[n];
            for (int i = 0, j = n-1, pos = n - 1 ; i <= j;)
            {
                if (A[i] * A[i] > A[j] * A[j])
                {
                    result[pos] = A[i] * A[i];
                    i++;

                }
                else
                {
                    result[pos] = A[j] * A[j];
                    j--;
                }

                pos--;

            }
            return result;
        }
        //public static void Rotate(int[] nums, int k)
        //{
        //    int[] result = new int[nums.Length];
        //    int n = nums.Length;
        //    for (int i=0;i< n; i++)
        //    {
        //        result[(i + k) % n] = nums[i];
        //    }
        //    Console.Write("[" + result[0]);
        //    for (int i = 1; i < result.Length; i++)
        //    {
        //        Console.Write("," + result[i]);
        //    }
        //    Console.Write("]");
        //}

        public static void Rotate(int[] nums, int k)
        {
            int temp;
            int n = nums.Length;
            for (int i = 0, j = n - 1; i <= j;)
            {
                temp = nums[i];
                nums[(i + k) % n] = nums[i];
                nums[i] = temp;
            }
            Console.Write("[" + nums[0]);
            for (int i = 1; i < nums.Length; i++)
            {
                Console.Write("," + nums[i]);
            }
            Console.Write("]");
        }
    }
}
