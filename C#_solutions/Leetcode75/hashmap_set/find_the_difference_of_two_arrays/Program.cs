static IList<IList<int>> FindDifference(int[] nums1, int[] nums2) 
{
            HashSet<int> h1 = new HashSet<int>(nums1), h2 = new HashSet<int>(nums2);

        return new List<IList<int>> { 
            h1.Where(x => !h2.Contains(x)).ToList<int>(), 
            h2.Where(x => !h1.Contains(x)).ToList<int>() 
        };
}
        

