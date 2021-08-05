class MinChairs
{
	private static int minChairs(int[] S, int[] E) 
	{
		Arrays.sort(S);
		Arrays.sort(E);

		int i=0, j=0;
		int maxChairs=1;
		int count =0;

		while(i<S.length) 
		{
			if(S[i] <E[j]) 
			{
				count++;
				if(count>chairs)				
					maxChairs = count;
				i++;
			}
			else
			{
				count--;
				j++;
			}
		}
		return maxChairs;
	}
	public static void main(String[] args)
    {
		int S[] = {1, 2, 10, 5, 5};
		int E[] = {4, 5, 12, 9, 12};
		System.out.println(minChairs(S, E));
    }
}
