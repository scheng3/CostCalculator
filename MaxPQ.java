public class MaxPQ<Key extends Comparable<Key>>
{
	private Key[] pq;
	private int N;
	public MaxPQ(int capacity)
	{ pq = (Key[]) new Comparable[capacity+1]; }
	public boolean isEmpty()
	{ return N == 0; }
	public void insert(Key key)
	public Key delMax()
	private void swim(int k)
	private void sink(int k)
	private boolean less(int i, int j)
	{ return pq[i].compareTo(pq[j]) < 0; }
	private void exch(int i, int j)
	{ Key t = pq[i]; pq[i] = pq[j]; pq[j] = t; }
	private void swim(int k)
	{
		while (k > 1 && less(k/3, k))
		{
			exch(k, k/3);
			k = k/3;
			}
		}
	public void insert(Key x)
	{
		pq[++N] = x;
		swim(N);
		}
	private void sink(int k)
	{
	while (3*k <= N)
	{
		int j = 3*k;
		if (j < N && less(j, j+1,j+2)) j++;
		if (!less(k, j)) break;
		exch(k, j);
		k = j;
		}
	}
	public Key delMax()
	{
		Key max = pq[1];
		exch(1, N--);
		sink(1);
		pq[N+1] = null;
		return max;
		} 
	public void sort(String[] a)
	{
	int N = a.length;
	MaxPQ<String> pq = new MaxPQ<String>();
	for (int i = 0; i < N; i++)
	pq.insert(a[i]);
	for (int i = N-1; i >= 0; i--)
	a[i] = pq.delMax();
	}
}
