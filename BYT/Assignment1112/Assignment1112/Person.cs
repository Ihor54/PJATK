using System;
using System.Text.RegularExpressions;

namespace Assignment1112
{
    public class Person
    {
        private readonly string _emailPattern =
            @"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$";

        private readonly string _phonePattern = @"^[+]{1}[0-9]{11}$";

        private string _email;

        private string _phone;

        public Person(string name, string surname, string email, string phone, string login, string password)
        {
            FirstName = name;
            LastName = surname;
            Email = email;
            Phone = phone;
            Login = login;
            Password = password;
        }

        public string FirstName { get; set; }
        public string LastName { get; set; }

        public string Email
        {
            get => _email;
            set
            {
                var pattern = new Regex(_emailPattern);
                if (pattern.Match(value).Success)
                    _email = value;
                else
                    throw new ArgumentException("Email doesn't match the proper format");
            }
        }

        public string Phone
        {
            get => _phone;

            set
            {
                var pattern = new Regex(_phonePattern);
                if (pattern.Match(value).Success)
                    _phone = value;
                else
                    throw new ArgumentException("Phone doesn't match the proper format");
            }
        }

        public string Login { get; set; }
        public string Password { get; set; }
    }
}