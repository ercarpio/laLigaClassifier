package ligaclass;

import java.util.*;

/**
 * Created by ecarpio
 */
public class DecisionTreeNode {
  public static final int numClasses = 3;
  private List<DecisionTreeNode> children;
  private int attributeId;
  private int classId;
  private int value;

  public DecisionTreeNode(int value){
    this.children = new LinkedList<>();
    this.attributeId = -1;
    this.classId = -1;
    this.value = value;
  }

  public int getMode(List<Integer[]> examples) {
    int[] counts = new int[numClasses];
    for (Integer[] example: examples) {
      counts[example[example.length - 1]]++;
    }
    int max = counts[0];
    int maxIndex = 0;
    for (int i = 1; i < numClasses; i++) {
      if (max < counts[i]) {
        max = counts[i];
        maxIndex = i;
      }
    }
    return maxIndex;
  }

  public void generateDTL(List<Integer[]> examples,
                                      List<Integer> attributes, int mode) {
    if (examples.isEmpty())
      this.classId = mode;
    else if (getClassCounts(examples) == 1)
      this.classId = getFirstClass(examples);
    else if (attributes.isEmpty())
      this.classId = getMode(examples);
    else {
      Map<Integer, List<Integer>> bestAtt =
              ChooseAttribute(attributes, examples);
      List<Integer> valList = Collections.emptyList();
      for (Map.Entry<Integer, List<Integer>> e: bestAtt.entrySet()) {
        this.attributeId = e.getKey();
        valList = e.getValue();
      }
      for (Integer i: valList) {
        List<Integer[]> nExamples = getExamplesByVal(i, this.attributeId, examples);
        List<Integer> nAttributes =
                getRemainingAttributes(this.attributeId, attributes);
        DecisionTreeNode newdt = new DecisionTreeNode(i);
        newdt.generateDTL(nExamples, nAttributes, getMode(examples));
        this.children.add(newdt);
      }
    }
  }

  private Map<Integer,List<Integer>> ChooseAttribute(
          List<Integer> attributes, List<Integer[]> examples) {
    Map<Integer, List<Integer>> retMap = new HashMap<>();
    double minRemaining = 1000;
    int minAttId = -1;
    Map<Integer, Integer> valList = new HashMap<>();
    for (Integer i: attributes) {
      List<Map<Integer, Integer>> counts = new LinkedList<>();
      for (int j = 0; j < numClasses; j++)
        counts.add(new HashMap<>());
      for (Integer[] example: examples) {
        Integer putReturn = counts.get(example[example.length - 1]).putIfAbsent(example[i], 1);
        if (putReturn != null)
          counts.get(example[example.length - 1]).replace(example[i], putReturn, putReturn + 1);
      }
      double remaining = 0;
      double Ivalue = 0;
      Map<Integer, Integer> attrSum = new HashMap<>();
      double currAttrSum = 0;
      for (Map<Integer, Integer> e: counts) {
        for (Map.Entry<Integer, Integer> k: e.entrySet()) {
          Integer putReturn = attrSum.putIfAbsent(k.getKey(), k.getValue());
          if (putReturn != null)
            attrSum.replace(k.getKey(), putReturn, putReturn + k.getValue());
        }
      }
      Map<Integer, Double> partialSum = new HashMap<>();
      for (Map<Integer, Integer> e: counts) {
        for (Map.Entry<Integer, Integer> k: e.entrySet()) {
          currAttrSum = attrSum.get(k.getKey());
          Ivalue = (currAttrSum / examples.size()) * (-(k.getValue() / currAttrSum)) *
                  (Math.log(k.getValue() / currAttrSum) / Math.log(2));
          Double putReturn = partialSum.putIfAbsent(k.getKey(), Ivalue);
          if (putReturn != null) {
            partialSum.replace(k.getKey(), putReturn, putReturn + Ivalue);
          }
        }
      }
      for (Double d: partialSum.values()) {
        remaining += d;
      }
      if (remaining < minRemaining) {
        minRemaining = remaining;
        minAttId = i;
        for (int j = 0; j < numClasses; j++)
          valList.putAll(counts.get(j));
      }
    }
    retMap.put(minAttId, new LinkedList<>(valList.keySet()));
    return retMap;
  }

  private List<Integer[]> getExamplesByVal(Integer i, Integer attr,
                                           List<Integer[]> examples) {
    List<Integer[]> retList = new LinkedList<>();
    for (Integer[] example: examples) {
      if (example[attr].equals(i))
        retList.add(example);
    }
    return retList;
  }

  private List<Integer> getRemainingAttributes(int attributeId,
                                               List<Integer> attributes) {
    List<Integer> retList = new LinkedList<>(attributes);
    retList.remove(retList.indexOf(attributeId));
    return retList;
  }

  private int getFirstClass(List<Integer[]> examples) {
    Integer[] firstExample = examples.get(0);
    return firstExample[firstExample.length - 1];
  }

  private int getClassCounts(List<Integer[]> examples) {
    Integer[] firstExample = examples.get(0);
    int firstClassId = firstExample[firstExample.length - 1];
    for (Integer[] example: examples) {
      if (firstClassId != example[example.length - 1])
        return 0;
    }
    return 1;
  }

  public int getClassId() {
    return classId;
  }

  public Integer[] predict(List<Integer[]> tests) {
    Integer[] retVals = new Integer[tests.size()];
    for (int i = 0; i < tests.size(); i++) {
      Integer[] test = tests.get(i);
      retVals[i] = findClass(test, this);
    }
    return retVals;
  }

  private int findClass(Integer[] test, DecisionTreeNode dt) {
    if (dt.children.size() == 0)
      return dt.classId;
    else {
      for (DecisionTreeNode child: dt.children) {
        if (test[dt.attributeId] == child.value) {
          return findClass(test, child);
        }
      }
      int minDiff = 1000;
      DecisionTreeNode minDiffChild = null;
      for (DecisionTreeNode child: dt.children) {
        if (Math.abs(test[dt.attributeId] - child.value) < minDiff) {
          minDiff = Math.abs(test[dt.attributeId] - child.value);
          minDiffChild = child;
        }
      }
      return findClass(test, minDiffChild);
    }
  }

  public void printTree(String indentation) {
    if (this.children.size() == 0)
      System.out.println(indentation + "Class: " + this.classId);
    else {
      System.out.println(indentation + "Attribute: " + this.attributeId + " Value: " + this.value);
      for (DecisionTreeNode child: this.children) {
        child.printTree(indentation + "\t");
      }
    }
  }
}
