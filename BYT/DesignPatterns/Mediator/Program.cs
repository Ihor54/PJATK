using System;

namespace Mediator
{
    class Program
    {
        static void Main(string[] args)
        {
            Battlefield battlefield = new Battlefield();

            // Create participants and register them

            Soldier George = new Soldier("George", new Position(5, 4));
            Soldier Paul = new Soldier("Paul", new Position(10, 6));
            Soldier Ringo = new Soldier("Ringo", new Position(5, 11));
            Soldier John = new Soldier("John", new Position(7, 4));
            Soldier Yoko = new Soldier("Yoko", new Position(3, 1));

            battlefield.Register(George);
            battlefield.Register(Paul);
            battlefield.Register(Ringo);
            battlefield.Register(John);
            battlefield.Register(Yoko);

            // Chatting participants

            Yoko.Send("John", "Hi John!");
            Paul.Send("Ringo", "Give me ammo");
            Ringo.Send("George", "Need revive");
            Paul.Send("John", "Let's go to the safe zone");
            John.Send("Yoko", "Enemy ahead");

            Console.WriteLine();

            //throwing grenade
            John.ThrowGrenade(new Position(5, 3));
            

            Console.ReadKey();
        }
    }
}
