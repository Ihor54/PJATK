using System;
using System.Collections.Generic;
using System.Text;

namespace Assignment1112
{
    public class Employee: Person
    {
        public double Salary { get; set; }
        public Employee(string name, string surname, string email, string phone, string login, string password, double salary) 
            : base(name, surname, email, phone, login, password)
        {
            Salary = salary;
        }
    }
}
