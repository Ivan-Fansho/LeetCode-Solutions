static string ReverseWords(string input)
{
    string[] words = input.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);

    Array.Reverse(words);

    return string.Join(" ", words).Trim();
}

string input = "a good   example";
        
        // Call the method to reverse words
string reversed = ReverseWords(input);
        
        // Output the result
Console.WriteLine(reversed);