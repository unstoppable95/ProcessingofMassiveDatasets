import java.math.BigInteger;
import java.util.ArrayList;
import java.util.BitSet;
import java.util.Random;

public class BloomFilter {

	private int m,k,n,range,p;
	private BitSet vector;
	private ArrayList<HashFunction> functions = new ArrayList<>();
	
	public BloomFilter(int m, int k,int n,int range) {
		this.m = m;
		this.k = k;
		this.n=n;
		this.range=range;
		this.vector = new BitSet(m);
		findNextPrime(this.range);
		makeFunctions();
	}

	public void add(int value) {
		int position;

		for(HashFunction function : this.functions) {
			position = this.generateHash(value, function);
			this.vector.set(position);
		}
	}

	public Boolean contains(int value) {
		int position;
		boolean inVector = true;

		for(HashFunction function : this.functions) {
			position = this.generateHash(value, function);

			if (!this.vector.get(position)) {
				inVector = false;
				break;
			}
		}
		return inVector;
	}

	private int generateHash(int value, HashFunction function) {
		return (int)(function.hash(value, this.p) % this.m);
	}

	private void findNextPrime(int number) {
		BigInteger value = new BigInteger(String.valueOf(number));
		this.p=value.nextProbablePrime().intValue();
	}

	private void makeFunctions() {
		Random rand = new Random(0);

		for(int i = 1; i <= this.k; ++i) {
			int a = rand.nextInt(this.p - 1) + 1;
			int b = rand.nextInt(this.p);
			HashFunction hashFunction = new HashFunction(a, b);
			this.functions.add(hashFunction);
		}
	}

}
