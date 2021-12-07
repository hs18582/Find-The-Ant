package main.java.LayerHelp;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.Stage;

public class LayeredCanvas extends Application {

    @Override
    public void start(Stage primaryStage) {
        Canvas layer1 = new Canvas(600, 600);
        Canvas layer2 = new Canvas(600, 600);
        GraphicsContext gc1 = layer1.getGraphicsContext2D();
        GraphicsContext gc2 = layer2.getGraphicsContext2D();

        gc1.setFill(Color.GREEN);
        gc1.setFont(new Font("Comic sans MS", 100));
        gc1.fillText("BACKGROUND", 0, 100);
        gc1.fillText("LAYER", 0, 200);
        gc1.setFont(new Font(30));
        gc1.setFill(Color.RED);
        gc1.fillText("Hold a key", 0, 270);

        gc2.setFill(Color.BLUE);
        Pane root = new Pane(layer2,layer1 );
        Scene scene = new Scene(root);

        primaryStage.setScene(scene);
        primaryStage.show();

        scene.setOnKeyPressed((evt) -> {
            gc2.clearRect(0, 0, layer2.getWidth(), layer2.getHeight());
            gc2.fillOval(Math.random() * layer2.getWidth(), Math.random() * layer2.getHeight(), 20, 30);
        });
    }

    public static void main(String[] args) {
        launch(args);
    }

}