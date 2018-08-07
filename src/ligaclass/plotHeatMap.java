package ligaclass;

import org.jfree.chart.ChartUtilities;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.NumberAxis;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.LookupPaintScale;
import org.jfree.chart.renderer.xy.XYBlockRenderer;
import org.jfree.data.DomainOrder;
import org.jfree.data.general.DatasetChangeListener;
import org.jfree.data.general.DatasetGroup;
import org.jfree.data.xy.DefaultXYZDataset;
import org.jfree.data.xy.XYZDataset;
import org.jfree.ui.RectangleInsets;

import java.awt.*;
import java.io.File;
import java.io.IOException;

/**
 * Created by ecarpio
 */
public class plotHeatMap {
  public static void main(String[] args) throws IOException {
    DefaultXYZDataset ds = new DefaultXYZDataset();
    double[][] vals = {
            {5500, 4000, 4500, 6000, 5000, 4000, 4000, 4500, 5000, 5500, 6000, 4500, 5500, 5000, 6000} ,
            {6, 6, 6, 6, 6, 5, 4, 4, 4, 4, 4, 5, 5, 5, 5} ,
            {196, 197, 197, 197, 198, 200, 200, 200, 200, 200, 200, 201, 201, 202, 202}};
    ds.addSeries("S1", vals);
    createChart(ds);
  }

  private static XYZDataset createDataset() {
    return new XYZDataset() {
      public int getSeriesCount() {
        return 1;
      }
      public int getItemCount(int series) {
        return 10000;
      }
      public Number getX(int series, int item) {
        return new Double(getXValue(series, item));
      }
      public double getXValue(int series, int item) {
        return item / 100 - 50;
      }
      public Number getY(int series, int item) {
        return new Double(getYValue(series, item));
      }
      public double getYValue(int series, int item) {
        return item - (item / 100) * 100 - 50;
      }
      public Number getZ(int series, int item) {
        return new Double(getZValue(series, item));
      }
      public double getZValue(int series, int item) {
        double x = getXValue(series, item);
        double y = getYValue(series, item);
        return Math.sin(Math.sqrt(x * x + y * y) / 5.0);
      }
      public void addChangeListener(DatasetChangeListener listener) {
        // ignore - this dataset never changes
      }
      public void removeChangeListener(DatasetChangeListener listener) {
        // ignore
      }
      public DatasetGroup getGroup() {
        return null;
      }
      public void setGroup(DatasetGroup group) {
        // ignore
      }
      public Comparable getSeriesKey(int series) {
        return "sin(sqrt(x + y))";
      }
      public int indexOf(Comparable seriesKey) {
        return 0;
      }
      public DomainOrder getDomainOrder() {
        return DomainOrder.ASCENDING;
      }
    };
  }

  private static void createChart(XYZDataset dataset) {
    NumberAxis xAxis = new NumberAxis("Number of Trees");
    xAxis.setLowerMargin(0.0);
    xAxis.setUpperMargin(0.0);
    xAxis.setRange(4000, 6000);
    NumberAxis yAxis = new NumberAxis("Number of Parameters");
    yAxis.setAutoRangeIncludesZero(false);
    yAxis.setLowerMargin(0.0);
    yAxis.setUpperMargin(0.0);
    yAxis.setStandardTickUnits(NumberAxis.createIntegerTickUnits());
    XYBlockRenderer renderer = new XYBlockRenderer();
    renderer.setBlockWidth(500);
    renderer.setBlockHeight(2);
    LookupPaintScale paintScale = new LookupPaintScale(174, 210,
            Color.red);
    paintScale.add(188, Color.orange);
    paintScale.add(194, Color.yellow);
    paintScale.add(199, Color.green);
    paintScale.add(202, Color.blue);
    renderer.setPaintScale(paintScale);
    XYPlot plot = new XYPlot(dataset, xAxis, yAxis, renderer);
    plot.setBackgroundPaint(Color.white);
    plot.setDomainGridlinePaint(Color.black);
    plot.setRangeGridlinePaint(Color.black);
    plot.setForegroundAlpha(0.80f);
    plot.setAxisOffset(new RectangleInsets(5, 5, 5, 5));
    JFreeChart chart = new JFreeChart("Optimum Number of Trees vs Number of Parameters Grid Search", plot);
    chart.removeLegend();
    chart.setBackgroundPaint(Color.white);

    File file = new File("out.png");
    try {
      ChartUtilities.saveChartAsPNG(file, chart, 725, 550);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
