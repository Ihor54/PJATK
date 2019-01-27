using System;
using System.Collections.Generic;
using System.Text;

namespace Assignment1112
{
    public class Client : Person
    {
        public List<Payment> Payments { get; set; }

        public Client(string name, string surname, string email, string phone, string login, string password)
            : base(name, surname, email, phone, login, password)
        {
        }
    }
}