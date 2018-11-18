using System;

namespace Mediator
{
    public class Soldier
    {
        public string Name { get;}
        public Position Position { get; set; }
        public Battlefield Battlefield { get; set; }

        public Soldier(string name, Position position)
        {
            Name = name;
            Position = position;
        }

        public void Send(string to, string message)
        {
            Battlefield.SendMessage(Name, to, message);
        }

        public void ThrowGrenade(Position destination)
        {
            Battlefield.ThrowGrenade(destination);
        }

        public void ReceiveMessage(string from, string message)
        {
            Console.WriteLine($"From {from} to {Name}: {message}");
        }

        public void ReceiveWarning(string message)
        {
            Console.WriteLine(message);
        }
    }
}