using System;
using System.Collections.Generic;
using System.Text;
using System.Text.RegularExpressions;

namespace Assignment1112
{
    public class Exercise
    {
        public string Name { get; set; }
        public int NumberOfSets { get; set; }
        public int NumberOfReps { get; set; }

        public List<ExerciseSummary> Summaries { get; set; }

        public Exercise(string name, int sets, int reps)
        {
            Name = name;
            NumberOfSets = sets;
            NumberOfReps = reps;
        }

    }
}
