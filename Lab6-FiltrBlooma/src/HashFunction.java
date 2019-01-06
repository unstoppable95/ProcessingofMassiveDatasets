public class HashFunction {
    private long a;
    private long b;

    public HashFunction(long a, long b) {
        this.a = a;
        this.b = b;
    }

    public long hash(long value, long p) {
        return (this.a * value + this.b) % p;
    }
}