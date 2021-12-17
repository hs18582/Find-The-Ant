package FindTheAnt;

import javafx.scene.Group;
import javafx.scene.Node;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;

public class Button extends Node {

    public Button() {
        //Adding GridPane
        GridPane gridPane = new GridPane();

        // 2D array of Buttons with value of 5,5
        javafx.scene.control.Button[][] btn = new javafx.scene.control.Button[3][3];

//Column is a vertical line and row is a horizontal line
//Two FOR loops used for creating 2D array of buttons with values i,j
        for (int i = 0; i < btn.length; i++) {
            for (int j = 0; j < btn.length; j++) {

//Initializing 2D buttons with values i,j
                btn[i][j] = new javafx.scene.control.Button("" + i + "," + "" + j);
                btn[i][j].setPrefSize(200, 200);
                btn[i][j].addEventHandler(MouseEvent.MOUSE_CLICKED, e -> {
                    var button = (javafx.scene.control.Button) e.getTarget();
                    button.setVisible(false);
                });

                gridPane.add(btn[i][j], i, j);
                //System.out.println(btn[i][j]);
                //System.out.println(i);
                //System.out.println(j);
            }
            //Creating a Group object
            Group root = new Group(gridPane);
        }
    }
}
