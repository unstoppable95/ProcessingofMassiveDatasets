import java.util.*;

public class Main {

    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();

        FileManager manager = new FileManager("./data/facts-nns.csv");
        Map<Integer, ArrayList<Integer>> userUniqueSongs = manager.makeUsersStructure();

        for (Map.Entry<Integer, ArrayList<Integer>> user : userUniqueSongs.entrySet()) {
            if (user.getKey() <= 100) {
                ArrayList<ArrayList<Object>> userList = new ArrayList<>();

                for (Map.Entry<Integer, ArrayList<Integer>> userTmp : userUniqueSongs.entrySet()) {
                    int intersectVal = 0;
                    if (user.getValue().size() <= userTmp.getValue().size()) {
                        for (Integer songId : user.getValue()) {
                            if (userTmp.getValue().contains(songId)) {
                                intersectVal++;
                            }
                        }
                    } else {
                        for (Integer songId : userTmp.getValue()) {
                            if (user.getValue().contains(songId)) {
                                intersectVal++;
                            }
                        }
                    }

                    int sumJaccard = userTmp.getValue().size() + user.getValue().size() - intersectVal;
                    if (sumJaccard != 0 && intersectVal != 0) {
                        double jaccardRat = (double) intersectVal / (double) sumJaccard;
                        ArrayList<Object> listInner = new ArrayList();
                        listInner.add(userTmp.getKey());
                        listInner.add(jaccardRat);
                        userList.add(listInner);
                    }

                }

                Collections.sort(userList, new Comparator<ArrayList<Object>>() {
                    @Override
                    public int compare(ArrayList<Object> a, ArrayList<Object> b) {
                        if ((double) a.get(1) < (double) b.get(1)) return 1;
                        if ((double) a.get(1) > (double) b.get(1)) return -1;
                        else return 0;
                    }
                });

                manager.saveResultsToFile(user.getKey(), userList);
            }
        }

        long estimatedTime = System.currentTimeMillis() - startTime;
        System.out.println("Total time: " + estimatedTime/1000 + " seconds ");
    }

}
