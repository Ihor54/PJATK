using System;
using System.Collections.Generic;
using System.Text;

namespace Assignment1112
{
    public class ExerciseSummary
    {
        public double? Weight { get; set; }
        public double? Time { get; set; }

        public ExerciseSummary(double? weight, double? time)
        {
            if ((weight == null && time == null) || (weight != null && time != null))
            {
                throw new ArgumentException("One parameters should be set");
            }

            if (weight != null)
            {
                Weight = weight;
            } else
            {
                Time = time;
            }
        }
    }
}
