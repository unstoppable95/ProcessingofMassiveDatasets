import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class FileManager {
    private String pathToFile;

    public FileManager(String pathToFile) {
        this.pathToFile = pathToFile;
    }

    public Map<Integer,ArrayList<Integer>>  makeUsersStructure() {
        Map<Integer,ArrayList<Integer>> userUniqueSongs = new HashMap<>();
        try {
            BufferedReader  reader = new BufferedReader(new FileReader(this.pathToFile));
            String line;
            reader.readLine();
            while ((line = reader.readLine()) != null) {

                int [] lineContent = Arrays.stream(line.split(",")).mapToInt(Integer::parseInt).toArray();

                if (userUniqueSongs.get(lineContent[0]) != null){
                    if (!userUniqueSongs.get(lineContent[0]).contains(lineContent[1])){
                        userUniqueSongs.get(lineContent[0]).add(lineContent[1]);
                    }
                }
                else{
                    ArrayList<Integer> tmp=new ArrayList();
                    tmp.add(lineContent[1]);
                    userUniqueSongs.put((lineContent[0]) , tmp);
                }

            }
            reader.close();
        }catch(IOException e ){
            e.printStackTrace();
        }
        return  userUniqueSongs;
    }

}