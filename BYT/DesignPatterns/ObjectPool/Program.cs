using System;

namespace ObjectPool
{
    class Program
    {
        static void Main(string[] args)
        {
            var rentalClub = RentalClub.Instance;

            var carForBob = rentalClub.RentCar();
            var carForJohn = rentalClub.RentCar();
            var carForJane = rentalClub.RentCar();
            var carForKate = rentalClub.RentCar();

            rentalClub.ReturnCar(carForJohn);
            carForKate = rentalClub.RentCar();

            rentalClub.SetMaximumSize(2);
            carForJohn = rentalClub.RentCar();
            
            Console.ReadKey();
        }
    }
}
