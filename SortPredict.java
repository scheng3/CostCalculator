public class SortPredict
{
	public static double timetrials(String alg, int N, int trials) {
		double total = 0.0;
		Double[] a = new Double[N];
		for (int t = 0; t < trials; t++) {
			for (int i = 0; i < N; i++) a[i] = StdRandom.uniform();
			total += time(alg, a); }
		return total; 
	}
		
	public static void main(String[] args)
	{
		String alg = args[0];
		int N = 1000;
		if (args.length > 1)
			N = Integer.parseInt(args[1]);
		int trials = 100;
		if (args.length > 2)
				trials = Integer.parseInt(args[2]);
		double ratio = timetrials(alg, 2*N, trials)/ timetrials(alg, N, trials);
		StdOut.printf("Ratio is %f\n", ratio);
		
		}

	
	}



public class testSubject
{
	int sum = 0;
	private int N;

	for (int n = N; n > 0; n /= 2) {
	     for(int i = 0; i < n; i++) {
	            sum++;
	     }
	}
	
}

public class Stopwatch
{
	private final long start;
	public Stopwatch()
	{ start = System.currentTimeMillis(); }
	public double elapsedTime()
	{
		long now = System.currentTimeMillis();
		return (now - start) / 1000.0;
		}
}






