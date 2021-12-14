import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class GridPaneMain extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    public void start(Stage primaryStage) {
        primaryStage.setTitle("GridPane example");

//Adding GridPane
        GridPane gridPane = new GridPane();

// 2D array of Buttons with value of 5,5
        Button[][] btn = new Button[3][3];

//Column is a vertical line and row is a horizontal line
//Two FOR loops used for creating 2D array of buttons with values i,j
        for(int i=0; i<btn.length; i++){
            for(int j=0; j<btn.length;j++){

//Initializing 2D buttons with values i,j
                btn[i][j] = new Button(""+i+","+""+j);
               btn[i][j].setPrefSize(300, 300);
                gridPane.add(btn[i][j], i, j);
            }
        }

//Adding GridPane to the scene
        Scene scene = new Scene(gridPane);
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}