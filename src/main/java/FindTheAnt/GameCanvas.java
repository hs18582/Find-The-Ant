package FindTheAnt;

import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;

public class GameCanvas {
    public int width;
    public int height;
    public int radius;


    public Color background;

    public Canvas canvas;
    GraphicsContext gc;

    public GameCanvas(int width, int height) {
        this.width = width;
        this.height = height;
        this.background = Color.GREEN;
        canvas = new Canvas(width, height);
        gc = canvas.getGraphicsContext2D();
    }

    public void draw() {
        gc.setFill(background);
        gc.fillRect(0,0,width,height);

        // vertical lines
        gc.setStroke(Color.BLACK);
        for(int i = 0 ; i <= width ; i+=200){
            gc.strokeLine(i, 0, i, height - (height%50));
        }

        // horizontal lines
        gc.setStroke(Color.BLACK);
        for(int i = 200 ; i <= height ; i+=200){
            gc.strokeLine(0, i, width, i);
        }


    }

}
