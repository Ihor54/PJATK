using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace ObjectPool
{
    public class RentalClub
    {
        private static RentalClub instance;

        private int _maxSize = 3;
        private int _counter = 0;
        private readonly List<Car> _carsAvailable = new List<Car>();
        private readonly List<Car> _carsInRent = new List<Car>();


        private RentalClub()
        {
            for (var i = 0; i < _maxSize; i++)
            {
                _carsAvailable.Add(new Car("BMW", 100));
            }
        }

        public static RentalClub Instance => instance ?? (instance = new RentalClub());

        public void SetMaximumSize(int num)
        {
            _maxSize = num;
        }

        public Car RentCar()
        {
            if (_carsInRent.Count < _maxSize)
            {
                var car = _carsAvailable.First();
                _carsAvailable.Remove(car);
                car.Start = DateTime.Now;
                _carsInRent.Add(car);
                Console.WriteLine("Enjoy your car.");
                return car;
            }

            Console.WriteLine("No cars available. Please come later.");
            return null;
        }

        public void ReturnCar(Car car)
        {
            var hours = (DateTime.Now - car.Start).Hours;
            var priceToPay = hours * car.Cost;
            Console.WriteLine($"You have to pay {priceToPay}$ for renting this car for {hours} hours");
            _carsInRent.Remove(car);
            _carsAvailable.Add(car);
        }

        

    }
}
