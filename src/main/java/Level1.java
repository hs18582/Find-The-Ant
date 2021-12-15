import javafx.animation.PathTransition;
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Line;
import javafx.scene.shape.LineTo;
import javafx.scene.shape.MoveTo;
import javafx.scene.shape.Path;
import javafx.stage.Stage;
import javafx.util.Duration;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Level1 extends Application {
    @Override
    public void start(Stage stage) throws FileNotFoundException {
        Image image = new Image(new FileInputStream("C:\\Users\\Shiva\\Dropbox\\Essex\\Yr 3\\CE301- Individual Capstone Project Challenge\\FindTheAnt\\src\\main\\java\\Images\\antright.png"));

        //Setting the image view
        ImageView imageView = new ImageView(image);

        //setting the fit height and width of the image view
        imageView.setFitHeight(100);
        imageView.setFitWidth(100);

        //Setting the preserve ratio of the image view
        imageView.setPreserveRatio(true);

        /// CREATING THE LINES FOR THE GRID
        Line straight = new Line(200, 0, 200, 600);
        Line straight1 = new Line(400, 0, 400, 600);
        Line straight2 = new Line(0, 200, 600, 200);
        Line straight3 = new Line(0, 400, 600, 400);


        //Creating a Path
        Path path = new Path();

        List<Integer> x = new ArrayList<>(Arrays.asList( 100, 300, 500));
        List<Integer> y = new ArrayList<>(Arrays.asList( 100, 300, 500));

        int Xindex = (int)(Math.random() * x.size());
        int Yindex = (int)(Math.random() * x.size());

        //Moving to the starting point
        MoveTo moveTo = new MoveTo(x.get(Xindex), y.get(Yindex));

        //Adding all the elements to the path
        path.getElements().add(moveTo);

        for(int i=0; i<20; i++){
            int X = (int)(Math.random() * x.size());
            int Y = (int)(Math.random() * x.size());
            LineTo line1 = new LineTo(x.get(X), y.get(Y));
            path.getElements().add(line1);
        }

        //Creating the path transition
        PathTransition pathTransition = new PathTransition();

        //Setting the duration of the transition
        pathTransition.setDuration(Duration.millis(40000));

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

        pathTransition.play();

        //Adding GridPane
        GridPane gridPane = new GridPane();

// 2D array of Buttons with value of 5,5
        Button[][] btn = new Button[3][3];

//Column is a vertical line and row is a horizontal line
//Two FOR loops used for creating 2D array of buttons with values i,j
        for (int i = 0; i < btn.length; i++) {
            for (int j = 0; j < btn.length; j++) {

//Initializing 2D buttons with values i,j
                btn[i][j] = new Button("" + i + "," + "" + j);
                btn[i][j].setPrefSize(200, 200);
                btn[i][j].addEventHandler(MouseEvent.MOUSE_CLICKED, e -> {
                    var button = (Button) e.getTarget();
                    button.setVisible(false);
                });

                gridPane.add(btn[i][j], i, j);
                //System.out.println(btn[i][j]);
                //System.out.println(i);
                //System.out.println(j);
            }
        }

        //Creating a Group object
        Group root = new Group(straight, straight1, straight2, straight3, imageView, gridPane);

        //Creating a scene object
        Scene scene = new Scene(root, 600, 600);
        scene.setFill(Color.GREEN);

        //Setting title to the Stage
        stage.setTitle("Find The Ant");

        //Adding scene to the stage
        stage.setScene(scene);

        //Displaying the contents of the stage
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }

}