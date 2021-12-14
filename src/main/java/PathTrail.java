import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.shape.LineTo;
import javafx.scene.shape.MoveTo;
import javafx.scene.shape.Path;
import javafx.stage.Stage;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PathTrail extends Application {
    @Override
    public void start(Stage stage) {
        //Creating a Path object
        Path path = new Path();


        List<Integer> x = new ArrayList<>(Arrays.asList( 100, 300, 500));
        List<Integer> y = new ArrayList<>(Arrays.asList( 100, 300, 500));


        int Xindex = (int)(Math.random() * x.size());
        int Yindex = (int)(Math.random() * x.size());

        System.out.println("Random Element is :"
                    + x.get(Xindex));

        System.out.println("Random Element is :"
                + y.get(Yindex));


        //Moving to the starting point
        MoveTo moveTo = new MoveTo();
        moveTo.setX(x.get(Xindex));
        moveTo.setY(y.get(Yindex));

        //Instantiating the LineTo class
        LineTo lineTo = new LineTo();
        int X = (int)(Math.random() * x.size());
        int Y = (int)(Math.random() * x.size());

        //Setting the Properties of the line element
        lineTo.setX(x.get(X));
        lineTo.setY(y.get(Y));

        //Adding the path elements to Observable list of the Path class
        path.getElements().add(moveTo);
        path.getElements().add(lineTo);

        //Creating a Group object
        Group root = new Group(path);

        //Creating a scene object
        Scene scene = new Scene(root, 600, 600);

        //Setting title to the Stage
        stage.setTitle("Drawing a Line");

        //Adding scene to the stage
        stage.setScene(scene);

        //Displaying the contents of the stage
        stage.show();
    }
    public static void main(String[] args){
        launch(args);
    }
}   