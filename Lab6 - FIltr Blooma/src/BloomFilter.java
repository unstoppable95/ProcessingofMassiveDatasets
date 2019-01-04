import java.math.BigInteger;
import java.util.ArrayList;
import java.util.BitSet;
import java.util.Random;

public class BloomFilter {

	private int size,k,n,range,prime;
	private BitSet vector;
	private ArrayList<HashFunction> functions = new ArrayList<>();
	
	public BloomFilter(int size, int k,int n,int range) {
		this.size = size;
		this.k = k;
		this.n=n;
		this.range=range;
		this.vector = new BitSet(size);
		this.prime = this.findPrimeNumber();
		prepareHashFunctions();
	}


	public void add(int key) {
		int position;

		for(HashFunction function : this.functions) {
			position = this.generateHash(key, function);
			this.vector.set(position);
		}
	}

	public Boolean contains(int key) {
		int position;
		boolean inVector = true;

		for(HashFunction function : this.functions) {
			position = this.generateHash(key, function);

			if (!this.vector.get(position)) {
				inVector = false;
				break;
			}
		}
		return inVector;
	}

	private int generateHash(int value, HashFunction function) {
		return (int)(function.hash(value, this.prime) % this.size);
	}

	private int findPrimeNumber() {
		BigInteger value = new BigInteger(String.valueOf(this.range));
		return value.nextProbablePrime().intValue();
	}

	private void prepareHashFunctions() {
		Random rand = new Random(0);

		for(int i = 1; i <= this.k; ++i) {
			int a = rand.nextInt(this.prime - 1) + 1;
			int b = rand.nextInt(this.prime);
			HashFunction hashFunction = new HashFunction(a, b);
			this.functions.add(hashFunction);
		}
	}

}
