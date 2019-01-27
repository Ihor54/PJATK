using System;
using System.Collections.Generic;
using System.Text;

namespace Assignment1112
{
    public class ClientTraining
    {
        public DateTime Date { get; set; }
        public Client Client { get; set; }
        public List<ExerciseSummary> Summaries { get; set; }
        public List<Training> Trainings { get; set; }

        public ClientTraining(DateTime date, Client client)
        {
            Date = date;
            Client = client;
        }

        public static string GetProgressInfoForClient(Client client)
        {
            return "Progress info";
        }
    }
}
