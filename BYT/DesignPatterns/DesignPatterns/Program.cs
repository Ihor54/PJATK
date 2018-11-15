using System;
using ChainOfResponsibility.Operations;

namespace ChainOfResponsibility
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine();
            while (input != "exit")
            {
                var op5 = new PowerOperation();
                var op4 = new DivideOperation(op5);
                var op3 = new MultiplyOperation(op4);
                var op2 = new SubstractOperation(op3);
                var op1 = new AddOperation(op2);
                Command command;
                try
                {
                     command = new Command(input);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                    throw;
                }

                var result = op1.Calculate(command);
                Console.Write(result == null
                    ? $"Operation {command.Operation} is not supported"
                    : $"{command} = {result} \n");

                input = Console.ReadLine();
            }
           
        }
    }
}
