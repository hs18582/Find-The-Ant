// Java Program to create a AnchorPane, adding
// label and button to it and also setting the
// min height and width of AnchorPane then add
// it to the stage

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class AnchorPane_2 extends Application {

    // launch the application
    public void start(Stage stage)
    {

        try {

            // set title for the stage
            stage.setTitle("AnchorPane");

            // create a label
            Label label = new Label("this is AnchorPane example");

            // create a AnchorPane
            AnchorPane anchor_pane = new AnchorPane(label);

            // anchor to the label
            AnchorPane.setTopAnchor(label, 120.0);
            AnchorPane.setLeftAnchor(label, 10.0);
            AnchorPane.setRightAnchor(label, 230.0);
            AnchorPane.setBottomAnchor(label, 120.0);

            Button button = new Button("button ");

            // anchor to the button
            AnchorPane.setTopAnchor(button, 5.0);
            AnchorPane.setLeftAnchor(button, 220.0);
            AnchorPane.setRightAnchor(button, 110.0);
            AnchorPane.setBottomAnchor(button, 125.0);

            anchor_pane.getChildren().add(button);

            anchor_pane.setMinHeight(400);
            anchor_pane.setMinWidth(400);

            // create a scene
            Scene scene = new Scene(anchor_pane, 400, 300);

            // set the scene
            stage.setScene(scene);

            stage.show();
        }

        catch (Exception e) {

            System.out.println(e.getMessage());
        }
    }

    // Main Method
    public static void main(String args[])
    {

        // launch the application
        launch(args);
    }
}
