using System;
using System.Collections.Generic;
using System.Text;

namespace ObjectPool
{
    public class Car
    {
        public string Name { get; set; }
        public int Cost { get; set; }
        public DateTime Start { get; set; }

        public Car(string name, int cost)
        {
            Name = name;
            Cost = cost;
        }


    }
}
