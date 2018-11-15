namespace ChainOfResponsibility
{
    public interface IChain
    {
        double? Calculate(Command command);
    }
}
