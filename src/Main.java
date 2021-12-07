package com.example.findtheant;

import javafx.animation.PathTransition;
import javafx.application.Application;
import javafx.event.EventHandler;

import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;

import javafx.scene.shape.Circle;
import javafx.scene.shape.LineTo;
import javafx.scene.shape.MoveTo;
import javafx.scene.shape.Path;
import javafx.stage.Stage;
import javafx.util.Duration;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class Main extends Application {
    @Override
    public void start(Stage stage) throws FileNotFoundException {
        Image image = new Image(new FileInputStream("M:\\Year 3\\CE301 Individual Capstone Project Challenge\\FindTheAnt\\src\\main\\java\\com\\example\\findtheant\\antright.png"));

        //Setting the image view
        ImageView imageView = new ImageView(image);

        //setting the fit height and width of the image view
        imageView.setFitHeight(100);
        imageView.setFitWidth(100);

        //Setting the preserve ratio of the image view
        imageView.setPreserveRatio(true);

        //Creating a Path
        Path path = new Path();

        //Moving to the staring point
        MoveTo moveTo = new MoveTo(100, 100);

        //Creating 1st line
        LineTo line1 = new LineTo(300, 100);

        //Creating 2nd line
        LineTo line2 = new LineTo(300,300);

        //Creating 3rd line
        LineTo line3 = new LineTo(100,300);

        //Creating 4th line
        LineTo line4 = new LineTo(100, 500);

        //Creating 5th line
        LineTo line5 = new LineTo(300, 500);

        //Creating 5th line
        LineTo line6 = new LineTo(500, 500);

        //Creating 5th line
        LineTo line7 = new LineTo(500, 300);

        //Creating 5th line
        LineTo line8 = new LineTo(500, 100);

        //Adding all the elements to the path
        path.getElements().add(moveTo);
        path.getElements().addAll(line1, line2, line3, line4, line5, line6, line7, line8);

        //Creating the path transition
        PathTransition pathTransition = new PathTransition();

        //Setting the duration of the transition
        pathTransition.setDuration(Duration.millis(1000));

        //Setting the node for the transition
        pathTransition.setNode(imageView);

        //Setting the path for the transition
        pathTransition.setPath(path);

        //Setting the orientation of the path
        pathTransition.setOrientation(
                PathTransition.OrientationType.ORTHOGONAL_TO_TANGENT);

        //Setting the cycle count for the transition
        pathTransition.setCycleCount(50);

        //Setting auto reverse value to true
        pathTransition.setAutoReverse(false);

        //Creating play button
        Button playButton = new Button("Play");
        playButton.setLayoutX(300);
        playButton.setLayoutY(250);

        playButton.setOnMouseClicked((new EventHandler<MouseEvent>() {
            public void handle(MouseEvent event) {
                System.out.println("Hello World");
                pathTransition.play();
            }
        }));

        //Creating stop button
        Button stopButton = new Button("stop");
        stopButton.setLayoutX(100);
        stopButton.setLayoutY(250);

        stopButton.setOnMouseClicked((new EventHandler<MouseEvent>() {
            public void handle(MouseEvent event) {
                System.out.println("Hello World");
                pathTransition.stop();
            }
        }));
        //Creating a Group object
        Group root = new Group(imageView, playButton, stopButton);

        //Creating a scene object
        Scene scene = new Scene(root, 600, 600);
        scene.setFill(Color.LAVENDER);

        //Setting title to the Stage
        stage.setTitle("Convenience Methods Example");

        //Adding scene to the stage
        stage.setScene(scene);

        //Displaying the contents of the stage
        stage.show();
    }
    public static void main(String args[]){
        launch(args);
    }
}