import java.util.ArrayList;
import java.util.Comparator;

public class InstanceCompare implements Comparator<ArrayList<Object>> {
    public int compare(ArrayList<Object>a, ArrayList<Object> b) {
        if ((double)a.get(1)<(double) b.get(1)) return 1;
        if ((double)a.get(1) >(double) b.get(1)) return -1;
        else return 0;
    }
}