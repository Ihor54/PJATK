using System;
using System.Collections.Generic;
using System.Text;

namespace Mediator
{
    public abstract class Mediator
    {
        public abstract void Register(Soldier soldier);
        public abstract void SendMessage(
            string from, string to, string message);
        public abstract void SendWarning(string to, string message);
        public abstract void ThrowGrenade(Position position);
    }
}
