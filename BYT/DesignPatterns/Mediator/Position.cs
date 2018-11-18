using System;
using System.Collections.Generic;
using System.Text;

namespace Mediator
{
    public class Position
    {
        public int X { get; set; }
        public int Y { get; set; }

        public Position(int x, int y)
        {
            X = x;
            Y = y;
        }


        public static double CalcDistance(Position position1, Position position2)
        {
            return Math.Sqrt(Math.Pow(position2.X - position1.X, 2) +
                             Math.Pow(position2.Y - position1.Y, 2));
        }
    }
}
