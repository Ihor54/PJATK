using System;
using System.Collections.Generic;

namespace Mediator
{
    public class Battlefield : Mediator
    {
        private readonly Dictionary<string, Soldier> _soldiers = new Dictionary<string, Soldier>();
        private const int GrenadeRadius = 5;

        public override void Register(Soldier soldier)
        {
            if (!_soldiers.ContainsValue(soldier))
            {
                _soldiers[soldier.Name] = soldier;
            }

            soldier.Battlefield = this;
        }

        public override void SendMessage(string from, string to, string message)
        {
            var soldier = _soldiers[to];
            soldier?.ReceiveMessage(from, message);
        }

        public override void SendWarning(string to, string message)
        {
            var soldier = _soldiers[to];
            soldier?.ReceiveWarning(message);
        }

        public override void ThrowGrenade(Position position)
        {
            foreach (var soldier in _soldiers)
            {
                var grenadeDistance = Position.CalcDistance(soldier.Value.Position, position);
                if (grenadeDistance < GrenadeRadius)
                {
                    this.SendWarning(soldier.Key, $"{soldier.Value.Name}, be carefull. You are in the explosion radius.");
                }
            }
        }
    }
}
