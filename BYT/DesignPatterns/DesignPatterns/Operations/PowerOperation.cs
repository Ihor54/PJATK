using System;

namespace ChainOfResponsibility.Operations
{
    public class PowerOperation : IChain
    {
        private readonly IChain _next;


        public PowerOperation(IChain next = null)
        {
            _next = next;
        }

        public double? Calculate(Command command)
        {
            if (command.Operation == "**")
            {
                return Math.Pow(command.Number1, command.Number2);
            }
            else
            {
                return _next?.Calculate(command);
            }

           
        }
    }
}
