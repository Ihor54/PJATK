using System;
using System.Collections.Generic;
using System.Reflection.Metadata;
using System.Text;

namespace Assignment1112
{
    public class Coach: Employee
    {
        public string Specialization { get; set; }

        public IList<ClientTraining> ClientTrainings { get; set; }

        public Coach(string name, string surname, string email, string phone, string login, string password, double salary, string specialization) 
            : base(name, surname, email, phone, login, password, salary)
        {
            Specialization = specialization;
        }

        public static IList<Coach> GetListOfCoaches()
        {
            return new List<Coach>();
        }
    }
}
