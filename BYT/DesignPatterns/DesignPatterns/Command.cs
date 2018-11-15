namespace ChainOfResponsibility
{
    public class Command
    {
        public double Number1 { get; set; }
        public double Number2 { get; set; }
        public string Operation { get; set; }

        public Command(double number1, string operation, double number2)
        {
            Number1 = number1;
            Number2 = number2;
            Operation = operation;
        }

        public Command(string command)
        {
            var elems = command.Split(" ");
            Number1 = double.Parse(elems[0]);
            Operation = elems[1];
            Number2 = double.Parse(elems[2]);
        }

        public override string ToString()
        {
            return $"{Number1} {Operation} {Number2}";
        }
    }
}
