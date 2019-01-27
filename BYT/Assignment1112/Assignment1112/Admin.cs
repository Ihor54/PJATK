using System;
using System.Collections.Generic;
using System.Text;

namespace Assignment1112
{
    public class Admin: Employee
    {
        public List<Post> Posts { get; set; }

        public Admin(string name, string surname, string email, string phone, string login, string password, double salary) 
            : base(name, surname, email, phone, login, password, salary)
        {
        }
    }
}
