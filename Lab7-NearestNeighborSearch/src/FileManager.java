import java.io.*;
import java.util.*;

public class FileManager {
    private String pathToInputFile;

    public FileManager(String pathToFile) {
        this.pathToInputFile = pathToFile;
    }

    public Map<Integer, ArrayList<Integer>> makeUsersStructure() {
        Map<Integer, ArrayList<Integer>> userUniqueSongs = new HashMap<>();
        try {
            BufferedReader reader = new BufferedReader(new FileReader(this.pathToInputFile));
            String line;
            reader.readLine();
            while ((line = reader.readLine()) != null) {
                int[] lineContent = Arrays.stream(line.split(",")).mapToInt(Integer::parseInt).toArray();
                if (userUniqueSongs.get(lineContent[0]) != null) {
                    if (!userUniqueSongs.get(lineContent[0]).contains(lineContent[1])) {
                        userUniqueSongs.get(lineContent[0]).add(lineContent[1]);
                    }
                } else {
                    ArrayList<Integer> tmp = new ArrayList();
                    tmp.add(lineContent[1]);
                    userUniqueSongs.put((lineContent[0]), tmp);
                }
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return userUniqueSongs;
    }

    public void saveResultsToFile(int userId, ArrayList<ArrayList<Object>> userList) {

        try {
            FileWriter file = new FileWriter("Results.txt", true);
            BufferedWriter writer1 = new BufferedWriter(file);
            PrintWriter writer = new PrintWriter(writer1);
            writer.write("User = " + userId);
            writer.println();
            int numberOfIterations = (userList.size() < 100) ? userList.size() : 100;

            for (int i = 0; i < numberOfIterations; i++) {
                writer.write(String.format("%7d %.5f", userList.get(i).get(0), userList.get(i).get(1)));
                writer.println();
            }

            writer.println();
            writer.flush();
            writer.close();
        } catch (IOException e) {
            System.out.println("Wystąpił błąd przy zapisie pliku ");
        }

    }

}