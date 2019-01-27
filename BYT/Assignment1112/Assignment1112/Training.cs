using System;
using System.Collections.Generic;
using System.Text;

namespace Assignment1112
{
    public class Training
    {
        public string Name { get; set; }
        public string Target { get; set; }
        public IList<string> Muscles { get; set; }
        public DateTime DateOfCreation { get; set; }
        public IList<Exercise> Exercises { get; set; }

        public Training(string name, string target, List<string> muscles, DateTime date, List<Exercise> exercises)
        {
            Name = name;
            Target = target;
            Muscles = muscles;
            DateOfCreation = date;
            Exercises = exercises;
        }

        public static IList<Training> GetLIstOfTrainings()
        {
            return new List<Training>();
        }
    }

    
}
