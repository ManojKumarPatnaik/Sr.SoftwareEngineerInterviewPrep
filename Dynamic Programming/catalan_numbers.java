class catalan_numbers{ 

	static int findCatalanNum(int n) { 
		int catalan[] = new int[n+2]; 
		catalan[0] = 1; 
		catalan[1] = 1; 

		for(int i=2; i<=n; i++) { 
			catalan[i] = 0; 
			for (int j=0; j<i; j++) { 
				catalan[i] += catalan[j]*catalan[i-j-1]; 
			} 
		} 
		return catalan[n]; 
	} 

	public static void main(String[] args) { 
		for(int i=0; i<10; i++) { 
			System.out.print(findCatalanNum(i)+" "); 
		} 
	} 
} 
