namespace ChainOfResponsibility.Operations
{
    public class MultiplyOperation: IChain
    {
        private readonly IChain _next;


        public MultiplyOperation(IChain next = null)
        {
            _next = next;
        }

        public double? Calculate(Command command)
        {
            if (command.Operation == "*")
            {
                return command.Number1 * command.Number2;
            }
            else
            {
                return _next?.Calculate(command);
            }
        }
    }
}
