package ligaclass;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        Random r = new Random();
        File dir = new File("data/ProcessedData/RFInput/reducedTraining");
        File[] files = dir.listFiles();
        List<String> filesList = new LinkedList<>();
        for (File file: files) {
            if (!(file.getName().contains("15") || file.getName().contains("future") || file.getName().contains("reduced")))
                filesList.add(file.getName());
        }
        int[] numDeletedAtts = {5};
        int[] ntrees = {500};
        double[] avgPredictions = new double[filesList.size()];
        double[] avgPredictionsPurged = new double[18];
        boolean bcontinue = true;
        double maxmean = 0;
        List<Integer> purgedAtts = new LinkedList<>();
        purgedAtts.add(0);
        purgedAtts.add(1);
//        purgedAtts.add(2);
//        purgedAtts.add(3);
        purgedAtts.add(4);
        purgedAtts.add(5);
        purgedAtts.add(6);
//        purgedAtts.add(7);
        purgedAtts.add(8);
        purgedAtts.add(9);
//        purgedAtts.add(10);
//        purgedAtts.add(11);
//        purgedAtts.add(12);
        purgedAtts.add(13);
//        purgedAtts.add(14);
//        purgedAtts.add(15);
//        purgedAtts.add(16);
//        purgedAtts.add(17);

//        while (bcontinue) {
            for (int j = 0; j < 1; j++) {
                for (int i = 2; i < 5; i++) {
                    List<String> tlist = new LinkedList<>(filesList);
                    String testfile = tlist.remove(i);
//                    String testfile = "9_inFile_14-15";
//                    String testfile = "10_inFile_15-16";
                    avgPredictions[i] = cross_predict(tlist, testfile, "out.predict", ntrees, 5, numDeletedAtts, purgedAtts, j);
                }
                double finalAverage = 0;
                for (int i = 0; i < filesList.size(); i++) {
                    finalAverage += avgPredictions[i];
                }
                avgPredictionsPurged[j] = finalAverage;
                System.out.println(j + "Avg: " + avgPredictionsPurged[j]);
            }
            double maxlocalavg = 0;
            int maxlocalindex = 0;
            for (int j = 0; j < avgPredictionsPurged.length; j++) {
                if (maxlocalavg < avgPredictionsPurged[j]) {
                    maxlocalindex = j;
                    maxlocalavg = avgPredictionsPurged[j];
                }
            }
            if (maxlocalavg > maxmean)
                purgedAtts.add(maxlocalindex);
            else
                bcontinue = false;
//        }
        for (Integer i: purgedAtts)
            System.out.println(i);
        System.out.println(maxmean);
    }

    private static double cross_predict(List<String> trainFiles, String testFile, String predictFile,
                                  int[] ntrees, int nreps, int[] numDeletedAtts, List<Integer> purgedAtts, int rem) {
        int maxPredictions = 0;
        double predictionsSum = 0;
        int totalPrdictions = nreps * numDeletedAtts.length;
        for (int z = 0; z < ntrees.length; z++) {
            for (int x = 0; x < nreps; x++) {
                for (int y = 0; y < numDeletedAtts.length; y++) {
                    Random r = new Random();
                    List<String> lines = new LinkedList<>();
                    for (String trainFile: trainFiles) {
                        try (Stream<String> exampleLines =
                                     Files.lines(Paths.get("data/ProcessedData/RFInput/" + trainFile))) {
                            exampleLines.forEach(lines::add);
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    }
                    List<Integer> attributes = new LinkedList<>();
                    List<Integer[]> examples = new LinkedList<>();
                    for (int i = 0; i < lines.get(0).split(" ").length - 1; i++)
                        attributes.add(i);
                    for (String line : lines) {
                        String[] fields = line.split(" ");
                        Integer[] example = new Integer[fields.length];
                        for (int i = 1; i < fields.length; i++) {
                            int value = Integer.parseInt(fields[i].split(":")[1]);
                            example[i - 1] = value;
                        }
                        example[fields.length - 1] = Integer.parseInt(fields[0]);
                        examples.add(example);
                    }

                    try {
                        for (Integer m : purgedAtts)
                            attributes.remove(attributes.indexOf(m));
//                        attributes.remove(rem);
                    }
                    catch (Exception e) {}
//                    attributes.remove(6);
//                    attributes.remove(13);
//                    attributes.remove(1);
//                    attributes.remove(7);
//                    attributes.remove(6);
//                    attributes.remove(10);
//                    attributes.remove(4);
//                    attributes.remove(9);
//                    attributes.remove(0);
//                    attributes.remove(2);
                    if ((x == 0) && (z == 0) && (y == 0)) {
                        System.out.println(attributes);
                    }

                    List<Integer[]> resultsList = new LinkedList<>();
                    for (int i = 0; i < ntrees[z]; i++) {
                        List<Integer> nAttributes = new LinkedList<>(attributes);
                        List<Integer[]> nExamples = new LinkedList<>(examples);
                        int remEx = r.nextInt(examples.size() - 760);
                        for (int j = 0; j < attributes.size() - numDeletedAtts[y]; j++) {
                            nAttributes.remove(r.nextInt(nAttributes.size()));
                        }
                        for (int j = 0; j < remEx; j++) {
                            nExamples.remove(r.nextInt(nExamples.size()));
                        }
                        resultsList.add(getPredictions(nExamples, nAttributes, testFile));
                    }

                    Integer[] results = getMode(resultsList);

                    List<String> testLines = new LinkedList<>();
                    try (Stream<String> inLines =
                                 Files.lines(Paths.get("data/ProcessedData/RFInput/" + testFile))) {
                        inLines.forEach(testLines::add);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                    int matchCounter = 0;
                    for (int i = 0; i < results.length; i++) {
                        if (results[i] == Integer.parseInt(testLines.get(i).split(" ")[0]))
                            matchCounter++;
                    }
                    System.out.println(matchCounter + " " + x);
                    predictionsSum += matchCounter;
                    if (matchCounter > maxPredictions) {
                        maxPredictions = matchCounter;
                        List<String> predictions = new LinkedList<>();
                        for (Integer i : results)
                            predictions.add(i.toString());
//                        System.out.println(predictions);
                        Path outFile = Paths.get("data/Predictions/" + predictFile);
                        try {
                            Files.write(outFile, predictions, Charset.forName("UTF-8"));
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    }
                }
            }
        }
        return predictionsSum / totalPrdictions;
    }

    private static Integer[] getMode(List<Integer[]> resultsList) {
        int[][] counts = new int[resultsList.get(0).length][DecisionTreeNode.numClasses];
        for (Integer[] resultAry: resultsList) {
            for (int i = 0; i < resultAry.length; i++) {
                counts[i][resultAry[i]]++;
            }
        }
        Integer[] retAry = new Integer[resultsList.get(0).length];
        for (int i = 0; i < retAry.length; i++) {
            int max = counts[i][0];
            int maxIndex = 0;
            for (int j = 1; j < DecisionTreeNode.numClasses; j++) {
                if (max < counts[i][j]) {
                    max = counts[i][j];
                    maxIndex = j;
                }
            }
            retAry[i] = maxIndex;
        }
        return retAry;
    }

    private static Integer[] getPredictions(List<Integer[]> examples,
                                            List<Integer> attributes,
                                            String testFile) {
        DecisionTreeNode dt = new DecisionTreeNode(-1);
        dt.getMode(examples);
        dt.generateDTL(examples, attributes, dt.getMode(examples));
        //dt.printTree("");
        List<Integer[]> tests = new LinkedList<>();
        List<String> testLines = new LinkedList<>();
        try (Stream<String> inLines =
                     Files.lines(Paths.get("data/ProcessedData/RFInput/" + testFile))) {
            inLines.forEach(testLines::add);
        } catch (IOException e) {
            e.printStackTrace();
        }
        for (String line : testLines) {
            String[] fields = line.split(" ");
            Integer[] test = new Integer[fields.length - 1];
            for (int i = 1; i < fields.length; i++) {
                int value = Integer.parseInt(fields[i].split(":")[1]);
                test[i - 1] = value;
            }
            tests.add(test);
        }
        return dt.predict(tests);
    }
}
