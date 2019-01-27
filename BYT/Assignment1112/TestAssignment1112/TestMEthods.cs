using System;
using Assignment1112;
using Xunit;

namespace TestAssignment1112
{
    public class TestMethods
    {

        [Fact]
        public void TestClientTraining()
        {
            var client = new Client("Bob", "Brown", "bob.brown@gmail.com", "+48123456789", "login", "password");

            Assert.Equal("Progress info", ClientTraining.GetProgressInfoForClient(client));
        }

        [Fact]
        public void TestExerciseSummaryConstructor_Takes_1_value()
        {
            var x = new ExerciseSummary(13, null);
            Assert.Null(x.Time);
            Assert.Equal(13, x.Weight);
        }

        [Fact]
        public void TestExerciseSummaryConstructor_ThrowsException()
        {
            Assert.Throws<ArgumentException>(delegate { new ExerciseSummary(null, null); });
            Assert.Throws<ArgumentException>(delegate { new ExerciseSummary(12, 13.1); });
        }

        [Fact]
        public void TestPersonConstructor()
        {
            Assert.Throws<ArgumentException>(delegate
            {
                new Person("Bob", "Brown", "123", "6789", "login", "password");
            });
            Assert.Throws<ArgumentException>(delegate
            {
                new Person("Bob", "Brown", "bob.brown@gmail.com", "6789", "login", "password");
            });
            Assert.Throws<ArgumentException>(delegate
            {
                new Person("Bob", "Brown", "123", "+48123456789", "login", "password");
            });
        }

        [Fact]
        public void TestPayment_TotalAmount()
        {
            Assert.Equal(10000, Payment.TotalAmountOfPayment());
        }
    }
}