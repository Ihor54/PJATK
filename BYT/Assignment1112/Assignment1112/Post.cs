using System;
using System.Collections.Generic;
using System.Text;

namespace Assignment1112
{
    public class Post
    {
        public string Type { get; set; }
        public string Content { get; set; }
        public Admin CreatedBy { get; set; }

        public Post(string type, string content, Admin createdBy)
        {
            Type = type;
            Content = content;
            CreatedBy = createdBy;
        }

        public static IList<Post> GetAllPosts()
        {
            return new List<Post>();
        }
    }
}
