import java.util.ArrayList;
import java.util.Map;

public class Main {



    public static void main(String[] args) {

        FileManager manager= new FileManager("./data/facts-nns.csv");


        Map<Integer, ArrayList<Integer>> userUniqueSongs = manager.makeUsersStructure();

        for (Map.Entry<Integer,ArrayList<Integer>> user: userUniqueSongs.entrySet()) {
            if (user.getKey() <= 1) {
                ArrayList<ArrayList<Object>> userList= new ArrayList<>();

                for (Map.Entry<Integer, ArrayList<Integer>> userTmp : userUniqueSongs.entrySet()) {
                    int intersectVal = 0;

                    if (user.getValue().size() <= userTmp.getValue().size()) {

                        for (Integer songId : user.getValue()) {
                            //jesli maja wspolne elementy
                            if (userTmp.getValue().contains(songId)) {
                                intersectVal++;
                            }
                        }
                    } else {

                        for (Integer songId : userTmp.getValue()) {
                            //jesli maja wspolne elementy
                            if (user.getValue().contains(songId)) {
                                intersectVal++;
                            }
                        }
                    }

                    int sumJacckard = userTmp.getValue().size() + user.getValue().size() - intersectVal;

                    if (sumJacckard != 0 && intersectVal != 0) {
                        double jacckardRat = (double)intersectVal / (double)sumJacckard;
                        ArrayList<Object> listInner = new ArrayList();
                        listInner.add(userTmp.getKey());
                        listInner.add(jacckardRat);
                        userList.add(listInner);
                    }

                }
                InstanceCompare sort = new InstanceCompare();
                userList.sort(sort);
                for(int i =0 ; i<=100; i++){
                    System.out.println(userList.get(i).get(0) +" " + userList.get(i).get(1));
                }
            }
        }

    }


}
