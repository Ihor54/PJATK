using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;

namespace Assignment1112
{
    public class Payment
    {
        public DateTime Date { get; set; }
        public string Description { get; set; }
        public double Amount { get; set; }
        public Client MadeBy { get; set; }


        public Payment(DateTime date, string description, double amount, Client madeBy)
        {
            Date = date;
            Description = description;
            Amount = amount;
            MadeBy = madeBy;
        }

        public static IList<Payment> AllPaymentsForClients()
        {
            return new List<Payment>();
        }

        public static double TotalAmountOfPayment()
        {
            return 10000;
        }
    }
}
