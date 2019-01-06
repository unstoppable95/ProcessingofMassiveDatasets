import java.util.*;

public class Main {

    private static void  shorterAlgoritmTime(FileManager manager,Comparator myComparator){
        long startTime,totalTime;

        startTime = System.currentTimeMillis();


        Map<Integer, ArrayList<Integer>> userUniqueSongs= manager.makeUsersStructure();
        Map<Integer, ArrayList<Integer>> songsUniqueUsers = manager.makeSongsStructure();
        totalTime = System.currentTimeMillis() - startTime;
        System.out.println("Reading data time: " + totalTime / 1000 + " seconds ");


        startTime = System.currentTimeMillis();

        for (Map.Entry<Integer, ArrayList<Integer>> user : userUniqueSongs.entrySet()) {
            if (user.getKey() <= 100) {
                ArrayList<ArrayList<Object>> userList = new ArrayList<>();
                HashSet<Integer> uniqueNeighbours = new HashSet<>();

                for (int song : user.getValue()) {
                    for (int userIdTmp : songsUniqueUsers.get(song)) {
                        if (!uniqueNeighbours.contains(userIdTmp)) {

                            uniqueNeighbours.add(userIdTmp);
                            ArrayList<Integer> songsTmp = userUniqueSongs.get(userIdTmp);
                            int intersectVal = 0;

                            if (user.getValue().size() <= songsTmp.size()) {
                                for (Integer songId : user.getValue()) {
                                    if (songsTmp.contains(songId)) {
                                        intersectVal++;
                                    }
                                }
                            } else {
                                for (Integer songId : songsTmp) {
                                    if (user.getValue().contains(songId)) {
                                        intersectVal++;
                                    }
                                }
                            }

                            int sumJaccard = songsTmp.size() + user.getValue().size() - intersectVal;
                            if (sumJaccard != 0 && intersectVal != 0) {
                                double jaccardRat = (double) intersectVal / (double) sumJaccard;
                                ArrayList<Object> listInner = new ArrayList();
                                listInner.add(userIdTmp);
                                listInner.add(jaccardRat);
                                userList.add(listInner);
                            }
                        }
                    }
                }

                Collections.sort(userList,myComparator);
                manager.saveResultsToFile(user.getKey(), userList);
            }
        }

        totalTime = System.currentTimeMillis() - startTime;
        System.out.println("Total algorithm time without reading data : " + totalTime / 1000 + " seconds ");
    }

//    private static void shorterReadDataTime(FileManager manager, Comparator myComparator){
//        long startTime = System.currentTimeMillis();
//
//        Map<Integer, ArrayList<Integer>> userUniqueSongs = manager.makeUsersStructure();
//
//        for (Map.Entry<Integer, ArrayList<Integer>> user : userUniqueSongs.entrySet()) {
//            if (user.getKey() <= 100) {
//                ArrayList<ArrayList<Object>> userList = new ArrayList<>();
//
//                for (Map.Entry<Integer, ArrayList<Integer>> userTmp : userUniqueSongs.entrySet()) {
//                    int intersectVal = 0;
//
//                    if (user.getValue().size() <= userTmp.getValue().size()) {
//                        for (Integer songId : user.getValue()) {
//                            if (userTmp.getValue().contains(songId)) {
//                                intersectVal++;
//                            }
//                        }
//                    } else {
//                        for (Integer songId : userTmp.getValue()) {
//                            if (user.getValue().contains(songId)) {
//                                intersectVal++;
//                            }
//                        }
//                    }
//
//                    int sumJaccard = userTmp.getValue().size() + user.getValue().size() - intersectVal;
//                    if (sumJaccard != 0 && intersectVal != 0) {
//                        double jaccardRat = (double) intersectVal / (double) sumJaccard;
//                        ArrayList<Object> listInner = new ArrayList();
//                        listInner.add(userTmp.getKey());
//                        listInner.add(jaccardRat);
//                        userList.add(listInner);
//                    }
//
//                }
//
//                Collections.sort(userList,myComparator );
//                manager.saveResultsToFile(user.getKey(), userList);
//            }
//        }
//
//        long estimatedTime = System.currentTimeMillis() - startTime;
//        System.out.println("Total time: " + estimatedTime/1000 + " seconds ");
//    }

    public static void main(String[] args) {
        FileManager manager = new FileManager("./data/facts-nns.csv");
        Comparator myComparator = new Comparator<ArrayList<Object>>() {
            @Override
            public int compare(ArrayList<Object> a, ArrayList<Object> b) {
                if ((double) a.get(1) < (double) b.get(1)) return 1;
                if ((double) a.get(1) > (double) b.get(1)) return -1;
                else return 0;
            }
        };
        shorterAlgoritmTime(manager,myComparator);
    }

}